# TO DO: Fix column naming

import csv
import os
import sys

import matplotlib.pyplot as plt
import networkx as nx

# import numpy as np
import pandas as pd
from networkx import max_weight_matching
from scipy.optimize import linear_sum_assignment


def preprocess(scholarship_path: str) -> dict:
    print("Preprocessing Scholarships")

    # Read scholarships and students in as dataframes
    # scholarships = pd.read_excel(scholarship_path)
    scholarships = pd.read_csv(scholarship_path)

    # Fill nan columns with empty space
    # Deal with deprecation warning
    scholarships.fillna(value="", inplace=True)
    scholarships = scholarships.map(lambda x: x.lower() if isinstance(x, str) else x)

    cols = scholarships.columns
    identifier = cols[0]
    rows = scholarships.iterrows()

    scholarship_reqs = {}
    for index, row in rows:
        # print(row)
        row_name = row[identifier]
        measured_attributes = {}
        for column in cols:
            # If attribute in scholarship exists
            if row[column] != "" and column != "identifier":
                # Fix this later to accomodate columns with multiple entries by splitting row[column] and processing it that way
                measured_attributes[column] = row[column]
        scholarship_reqs[row_name] = measured_attributes

    return scholarship_reqs


# ACT, CHURCH, COUNTY, GENDER, GPA, HIGH SCHOOL, MAJOR, MARRIED, MINISTRY, MINISTRY DEPENDENT, NEED, MINORITY, STATE
def qualify_matrix(scholarship_reqs: dict, student_df: pd.DataFrame) -> list[list]:
    print("Creating the qualification matrix")
    matrix = []
    students = student_df.iterrows()

    for index, student in students:
        # Student block
        # if disqualify, subtract. Add for preference later
        qualified_scholarship = []
        for key in scholarship_reqs:
            # Scholarship block
            qualify = 1

            scholarship = scholarship_reqs[key]
            for attr in scholarship:
                # Scholarship attribute block

                # Skip mismatched columns or Scholarship. Probably not needed. Deal w/ later
                if scholarship[attr] == "" or attr == "Scholarship":
                    continue

                # Deal with case sensitivity later
                if attr == "NEED":
                    if scholarship[attr] == "yes" and student[attr] != "yes":
                        qualify -= 1
                elif attr == "MAJOR":
                    # Now that every student has a more general major assignment, this should work better
                    if scholarship[attr] != "unrestricted" and scholarship[attr] != "":
                        if student[attr] not in scholarship[attr]:
                            qualify -= 1
                elif attr == "GENDER":
                    # Just compare first character (for now)
                    if scholarship[attr] != "":
                        if student[attr] != scholarship[attr][0]:
                            qualify -= 1
                # elif attr == "Classification": Doesn't seem to matter for us
                #     if student[attr] not in scholarship[attr]:
                #         qualify -= 1
                elif attr == "GPA":
                    # Try except in case a type conversion goes wrong
                    if scholarship[attr] != "":
                        if student[attr] == "":
                            qualify -= 1
                        else:
                            try:
                                if float(student[attr]) < float(scholarship[attr]):
                                    qualify -= 1
                            except:
                                qualify -= 1
                elif attr == "HIGH SCHOOL":
                    if (
                        scholarship[attr] != ""
                        and student[attr] not in scholarship[attr]
                    ):
                        qualify -= 1
                elif attr == "MINISTRY":
                    if (
                        scholarship[attr] == "call to ministry"
                        and student[attr] != "yes"
                    ):
                        qualify -= 1
                # IGNORE FOR NOW
                # Religion qualifications may fall under other religion qualifications and not register. Baptist is Christian, etc...
                # elif attr == "Religion":  # Oh boy there's a lot of those...
                #     if student[attr] != scholarship[attr]:
                #         qualify -= 1

                # elif attr =

                # Failed scholarship. May need to modify for preferences later
                if qualify <= 0:
                    break
            qualified_scholarship.append(qualify)
        matrix.append(qualified_scholarship)
    return matrix


def qualify_graph(
    scholarship_reqs: dict, students_df: pd.DataFrame, matrix: list[list]
) -> list[nx.Graph]:

    print("Creating the graph")
    graph = nx.Graph()
    # print(matrix)

    identifier = students_df.columns[0]

    # Add scholarship nodes
    for key in scholarship_reqs:
        # Will probably want to use and id later. Probably best to make scholarship_reqs based on a primary key later
        graph.add_node(key, name=key)

    # Add student nodes
    rows = students_df.iterrows()
    for index, student in rows:
        # graph.add_node(student["Person Banner ID"], name=student["Person Banner ID"])
        graph.add_node(student[identifier], name=student[identifier])

    # Connect qualified student nodes to scholarships
    scholarship_names = list(scholarship_reqs.keys())
    # print(students_df["Person Banner ID"])
    # print(scholarship_names.loc[:, "Person Banner ID"])
    for i in range(len(matrix)):
        student_qual_list = matrix[i]
        for j in range(len(student_qual_list)):
            scholarship_qual = matrix[i][j]
            if (
                scholarship_qual == 1
            ):  # This can probably be removed if we are using max_weight_matching
                # graph.add_edge(student, scholarship)
                # print(students_df.iloc[i]["Person Banner ID"], scholarship_names[j])
                graph.add_edge(
                    # students_df.iloc[i]["Person Banner ID"],
                    students_df.iloc[i][identifier],
                    scholarship_names[j],
                    weight=scholarship_qual,
                )

    # Remove isolated nodes
    isolated_nodes = list(nx.isolates(graph))
    graph.remove_nodes_from(isolated_nodes)

    # Create subgraphs
    components = nx.connected_components(graph)
    subgraphs = [graph.subgraph(c).copy() for c in components]

    for graph in subgraphs:
        nx.draw(graph, with_labels=True, font_size=10, node_size=500)
        plt.show()

    return subgraphs


# Scholarship path then student path
if __name__ == "__main__":
    # For now, run using python main.py <scholarship_path> <student_path>
    # No error detection right now. Will need some eventually
    if len(sys.argv) < 3:
        print("Invalid arguments")
    else:
        scholarship_path = sys.argv[1]
        student_path = sys.argv[2]

        # print(scholarship_path)
        scholarship_reqs = preprocess(scholarship_path)
        scholarship_names = list(scholarship_reqs.keys())

        # students = pd.read_excel(student_path)
        students = pd.read_csv(student_path)
        students.fillna(value="", inplace=True)
        students = students.map(lambda x: x.lower() if isinstance(x, str) else x)

        matrix = qualify_matrix(scholarship_reqs, students)
        # for row in matrix:
        #     print(row)
        # print()

        row_ind, col_ind = linear_sum_assignment(matrix, maximize=True)

        # The current way this works is a great example of why the linear_sum_assignment
        # doesn't work. It will still give out every scholarship even if they aren't qualified for
        # because it is just cost based
        # for i in range(len(row_ind)):
        #     print(
        #         "Scholarship:",
        #         scholarship_names[col_ind[i]],
        #         "  Student: ",
        #         students.iloc[row_ind[i]]["Person Banner ID"],
        #         "  value: ",
        #         matrix[i][col_ind[i]],
        #     )

        subgraphs = qualify_graph(scholarship_reqs, students, matrix)

        matches = []
        for graph in subgraphs:
            matches.append(nx.algorithms.bipartite.hopcroft_karp_matching(graph))

        # print("\nHopcroft-karp Matches: ")
        # filtered_matches = {}
        # i = 0
        # for match in matches:
        #     # Eliminate duplicates
        #     filtered_matches[i] = {u: v for u, v in match.items() if u < v}
        #     for key in filtered_matches[i]:
        #         print(f"{key}: {filtered_matches[i][key]}")
        #     i += 1

        blossom_matches = []
        print("Finding the most optimal matches")
        for graph in subgraphs:
            blossom_matches.append(max_weight_matching(graph))

        print("\n\n\n\nBlossom Matches")
        for match in blossom_matches:
            for tuple in match:
                print(f"{tuple[1]}: {tuple[0]}")

        # with open("output.csv", "w", newline="") as file:
        #     fieldnames = ["student", "scholarship"]
        #     writer = csv.DictWriter(
        #         file,
        #     )
