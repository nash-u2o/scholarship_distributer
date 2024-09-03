import os
import sys

import matplotlib.pyplot as plt
import networkx as nx

# import numpy as np
import pandas as pd
from scipy.optimize import linear_sum_assignment


def preprocess(scholarship_path: str) -> dict:
    # Read scholarships and students in as dataframes
    scholarships = pd.read_excel(scholarship_path)
    # Fill nan columns with False
    scholarships.fillna(value=False, inplace=True)

    cols = scholarships.columns
    rows = scholarships.iterrows()

    scholarship_reqs = {}
    for index, row in rows:
        row_name = row["Scholarship"]

        measured_attributes = {}
        for column in cols:
            # If attribute in scholarship is not False
            if row[column] is not False and column != "Scholarship":
                # Fix this later to accomodate columns with multiple entries by splitting row[column] and processing it that way
                measured_attributes[column] = row[column]
        scholarship_reqs[row_name] = measured_attributes

    return scholarship_reqs


def qualify_matrix(scholarship_reqs: dict, student_df: pd.DataFrame) -> list[list]:
    matrix = []
    students = student_df.iterrows()

    for index, student in students:
        # Student block
        # if qualify, append a 1. At any failure, append 0 and continue
        qualified_scholarship = []
        for key in scholarship_reqs:
            # Scholarship block
            qualify = 1
            scholarship = scholarship_reqs[key]
            for attr in scholarship:
                # Scholarship attribute block
                if scholarship[attr] == False or attr == "Scholarship":
                    continue

                # Deal with case sensitivity later
                if attr == "Need":
                    if scholarship[attr] == "Yes" and student[attr] != "Yes":
                        qualify = 0
                elif attr == "Major":  # Accomodate multiple majors later
                    if student[attr] != scholarship[attr]:
                        qualify = 0
                elif attr == "Gender":
                    if student[attr] != scholarship[attr]:
                        qualify = 0
                elif attr == "Classification":
                    if student[attr] != scholarship[attr]:
                        qualify = 0
                elif attr == "GPA":
                    # Try except in case a type conversion goes wrong
                    try:
                        if float(student[attr]) < float(scholarship[attr]):
                            qualify = 0
                    except:
                        qualify = 0
                # Religion qualifications may fall under other religion qualifications and not register. Baptist is Christian, etc...
                elif attr == "Religion":
                    if student[attr] != scholarship[attr]:
                        qualify = 0

                # Failed scholarship
                if qualify == 0:
                    break
            qualified_scholarship.append(qualify)
        matrix.append(qualified_scholarship)
    return matrix


def qualify_graph(
    scholarship_reqs: dict, students_df: pd.DataFrame, matrix: list[list]
) -> list[nx.Graph]:
    graph = nx.Graph()

    # Add scholarship nodes
    for key in scholarship_reqs:
        # Will probably want to use and id later. Probably best to make scholarship_reqs based on a primary key later
        graph.add_node(key, name=key)

    # Add student nodes
    rows = students_df.iterrows()
    for index, student in rows:
        graph.add_node(student["Student Name"], name=student["Student Name"])

    # Connect qualified student nodes to scholarships
    scholarship_names = list(scholarship_reqs.keys())
    for i in range(len(matrix)):
        student_qual_list = matrix[i]
        for j in range(len(student_qual_list)):
            scholarship_qual = matrix[i][j]
            if scholarship_qual == 1:
                # graph.add_edge(student, scholarship)
                graph.add_edge(
                    students_df.iloc[i]["Student Name"], scholarship_names[j]
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


if __name__ == "__main__":
    # For now, run using python main.py <scholarship_path> <student_path>
    # No error detection right now. Will need some eventually
    if len(sys.argv) < 3:
        print("Invalid arguments")
    else:
        scholarship_path = sys.argv[1]
        student_path = sys.argv[2]

        scholarship_reqs = preprocess(scholarship_path)
        scholarship_names = list(scholarship_reqs.keys())

        students = pd.read_excel(student_path)
        students.fillna(value=False, inplace=True)

        matrix = qualify_matrix(scholarship_reqs, students)
        for row in matrix:
            print(row)
        print()

        row_ind, col_ind = linear_sum_assignment(matrix, maximize=True)

        # The current way this works is a great example of why the linear_sum_assignment
        # doesn't work. It will still give out every scholarship even if they aren't qualified for
        # because it is just cost based
        for i in range(len(row_ind)):
            print(
                "Scholarship:",
                scholarship_names[col_ind[i]],
                "  Student: ",
                students.iloc[row_ind[i]]["Student Name"],
                "  value: ",
                matrix[i][col_ind[i]],
            )

        subgraphs = qualify_graph(scholarship_reqs, students, matrix)

        matches = []
        for graph in subgraphs:
            matches.append(nx.algorithms.bipartite.hopcroft_karp_matching(graph))

        print("\nHopcroft-karp Matches: ")
        filtered_matches = {}
        i = 0
        for match in matches:
            # Eliminate duplicates
            filtered_matches[i] = {u: v for u, v in match.items() if u < v}
            for key in filtered_matches[i]:
                print(f"{key}: {filtered_matches[i][key]}")
            i += 1
