# TO DO: Get the actual data I can expect. Can't do much until I know what I'm dealing with

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
            qualify = 1  # Maybe add to qualify for preferences

            scholarship = scholarship_reqs[key]
            for attr in scholarship:
                # Scholarship attribute block
                if scholarship[attr] != "":
                    # If version conflicts aren't an error, use match-case
                    if attr == "ACT":
                        if int(student[attr]) < int(scholarship[attr]):
                            qualify -= 1
                    elif attr == "CHURCH":
                        if student[attr] != scholarship[attr]:
                            qualify -= 1
                    # Classify gender by first letter. To be safe, strip leading and trailing spaces off
                    elif attr == "GENDER":
                        if (
                            str.strip(student[attr])[0]
                            != str.strip(scholarship[attr])[0]
                        ):
                            qualify -= 1
                    elif attr == "GPA":
                        if float(student[attr]) < float(scholarship[attr]):
                            qualify -= 1
                    elif attr == "HIGH SCHOOL":
                        if student[attr] != scholarship[attr]:
                            qualify -= 1
                    elif attr == "MAJOR":
                        if (
                            scholarship[attr] != "unrestricted"
                            and student[attr] != scholarship[attr]
                        ):
                            qualify -= 1
                    elif attr == "MARRIED":
                        if student[attr] != scholarship[attr]:
                            qualify -= 1
                    elif attr == "MINISTRY":
                        if student[attr] != scholarship[attr]:
                            qualify -= 1
                    elif attr == "MINISTRY DEPENDENT":
                        if student[attr] != scholarship[attr]:
                            qualify -= 1
                    elif attr == "NEED":
                        if (
                            scholarship[attr] == "yes"
                            and student[attr] != scholarship[attr]
                        ):
                            qualify -= 1
                    elif attr == "MINORITY":
                        if (
                            scholarship[attr] == "yes"
                            and student[attr] != scholarship[attr]
                        ):
                            qualify -= 1
                    elif attr == "STATE":
                        if student[attr] != scholarship[attr]:
                            qualify -= 1

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


def save_csv(headers, data, name: str):
    i = 0
    while True:
        file_str = f"{name}.csv" if i == 0 else f"{name}({i}).csv"
        if not os.path.exists(file_str):
            with open(file_str, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(data)
            break
        else:
            i += 1


# Scholarship path then student path
if __name__ == "__main__":
    # For now, run using python main.py <scholarship_path> <student_path>
    # No error detection right now. Will need some eventually
    if len(sys.argv) < 3:
        print("Invalid arguments")
    else:
        scholarship_path = sys.argv[1]
        student_path = sys.argv[2]

        scholarships = pd.read_csv(scholarship_path)

        # print(scholarship_path)
        scholarship_reqs = preprocess(scholarship_path)
        scholarship_names = list(scholarship_reqs.keys())

        # students = pd.read_excel(student_path)
        students = pd.read_csv(student_path)
        students.fillna(value="", inplace=True)
        students = students.map(lambda x: x.lower() if isinstance(x, str) else x)

        matrix = qualify_matrix(scholarship_reqs, students)

        # Hungarian Matches
        # row_ind, col_ind = linear_sum_assignment(matrix, maximize=True)

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

        matches = []
        subgraphs = qualify_graph(scholarship_reqs, students, matrix)
        for graph in subgraphs:
            matches.append(nx.algorithms.bipartite.hopcroft_karp_matching(graph))

        # print("\nHopcroft-karp Matches: ")
        # filtered_matches = {}
        # i = num_matches = 0
        # for match in matches:
        #     # Eliminate duplicates
        #     filtered_matches[i] = {u: v for u, v in match.items() if u < v}
        #     for key in filtered_matches[i]:
        #         print(f"{key}: {filtered_matches[i][key]}")
        #         num_matches += 1
        #     i += 1
        # print(num_matches)

        blossom_matches = []
        print("Finding the most optimal matches")
        for graph in subgraphs:
            blossom_matches.append(max_weight_matching(graph))

        print("\n\n\nBlossom Matches")

        csv_headers = [
            "SCHOLARSHIP",
            "STUDENT",
            "ACT",
            "CHURCH",
            "GENDER",
            "GPA",
            "HIGH SCHOOL",
            "MAJOR",
            "MARRIED",
            "MINISTRY",
            "MINISTRY DEPENDENT",
            "NEED",
            "MINORITY",
            "STATE",
        ]

        csv_data = []

        num_matches = 0
        for match in blossom_matches:
            for tuple in match:
                # Tuple 0 is a scholarship. Else tuple[0] is a student
                # Very proprietary and inefficient testing code

                res = ["" for i in range(len(csv_headers))]

                scholarship_name = ""
                student_name = ""

                if "sch" in tuple[0]:
                    student_name = tuple[1]
                    scholarship_name = tuple[0]
                else:
                    student_name = tuple[0]
                    scholarship_name = tuple[1]

                print(f"{scholarship_name} {student_name}")
                num_matches += 1

                res[0] = scholarship_name
                res[1] = student_name

                scholarship = scholarships[scholarships["ID"] == scholarship_name]
                student = students[students["ID"] == student_name]
                for label, value in scholarship.items():
                    if value.iloc[0] != "":
                        try:
                            index = csv_headers.index(label)
                            res[index] = (
                                f"Scholarship: {value.iloc[0]} Student: {student[label].iloc[0]}"
                            )
                        except:
                            pass

                csv_data.append(res)
        print(num_matches)
        # save_csv(headers=csv_headers, data=csv_data, name="sample_matches")
