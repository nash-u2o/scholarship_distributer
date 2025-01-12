# TO DO: Get the actual data I can expect. Can't do much until I know what I'm dealing with

import csv
import os
import sys

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# import numpy as np
import pandas as pd
from munkres import DISALLOWED, Munkres
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
    # make everything lowercase
    scholarships = scholarships.map(lambda x: x.lower() if isinstance(x, str) else x)

    cols = scholarships.columns
    identifier = cols[0]
    rows = scholarships.iterrows()

    scholarship_reqs = {}
    for index, row in rows:
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
                    # qualified_scholarship.append(DISALLOWED)
                    break

            # # NEW
            """
            Never reached unless student does qualify.
            #CHANGE HOW THIS WORKS
            """
            # student = student_df.iloc[index]
            # remaining_student_scholarship = student["VALUE"]
            # scholarship_amount = scholarship_reqs[key]["VALUE"]
            # # if qualify <= 0:
            # # qualified_scholarship.append(np.Inf)
            # if qualify > 0:
            #     weight = (
            #         scholarship_amount
            #         if remaining_student_scholarship > scholarship_amount
            #         else remaining_student_scholarship
            #     )
            #     weight *= -1
            #     qualified_scholarship.append(weight)
            # END NEW

            qualified_scholarship.append(qualify)
        matrix.append(qualified_scholarship)
    return matrix


def qualify_graph(
    scholarship_reqs: dict, students_df: pd.DataFrame, matrix: list[list]
) -> list[nx.Graph]:

    graph = nx.Graph()

    identifier = students_df.columns[0]

    # Add scholarship nodes
    for key in scholarship_reqs:
        # Will probably want to use and id later. Probably best to make scholarship_reqs based on a primary key later
        graph.add_node(key, name=key, amount=scholarship_reqs[key]["VALUE"])
    # Add student nodes
    rows = students_df.iterrows()
    for index, student in rows:
        graph.add_node(student[identifier], name=student[identifier])

    # Connect qualified student nodes to scholarships
    scholarship_names = list(scholarship_reqs.keys())

    for i in range(len(matrix)):
        student_qual_list = matrix[i]
        for j in range(len(student_qual_list)):
            scholarship_qual = matrix[i][j]
            if scholarship_qual == 1:
                student = students_df.iloc[i]
                name = student[identifier]
                remaining_student_scholarship = student["VALUE"]
                scholarship_amount = scholarship_reqs[scholarship_names[j]]["VALUE"]
                weight = (
                    scholarship_amount
                    if remaining_student_scholarship > scholarship_amount
                    else remaining_student_scholarship
                )
                graph.add_edge(
                    name,
                    scholarship_names[j],
                    weight=weight,
                )

    # Remove isolated nodes
    isolated_nodes = list(nx.isolates(graph))
    graph.remove_nodes_from(isolated_nodes)

    # Create subgraphs
    components = nx.connected_components(graph)
    subgraphs = [graph.subgraph(c).copy() for c in components]

    # Make a horrible looking plot of the graph
    # for graph in subgraphs:
    #     nx.draw(graph, with_labels=True, font_size=10, node_size=500)
    #     plt.show()

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

        scholarship_reqs = preprocess(scholarship_path)
        scholarship_names = list(scholarship_reqs.keys())

        # students = pd.read_excel(student_path)
        students = pd.read_csv(student_path)

        student_names = list(students["ID"])

        match_dict = {name: [] for name in list(students["ID"])}

        students.fillna(value="", inplace=True)
        students = students.map(lambda x: x.lower() if isinstance(x, str) else x)

        # Start Blossom
        blossom_matches = []
        print("Finding the most optimal matches")

        flag = True
        empty_count = 0
        while flag:
            print("run while")
            matrix = qualify_matrix(scholarship_reqs, students)
            subgraphs = qualify_graph(scholarship_reqs, students, matrix)

            empty_count = 0
            if len(subgraphs) == 0:
                break
            for graph in subgraphs:
                # blossom_matches.append(max_weight_matching(graph))
                matchings = max_weight_matching(graph)
                if len(matchings) == 0:
                    empty_count += 1

                stu_name = ""
                schol_name = ""
                for match in matchings:
                    if match[0] in student_names:
                        stu_name = match[0]
                        schol_name = match[1]
                    elif match[1] in student_names:
                        stu_name = match[1]
                        schol_name = match[0]
                    else:
                        raise ValueError(
                            "Invalid matching. Student name not in initial data."
                        )
                    match_dict[stu_name].append(schol_name)

                    # This is TERRIBLY slow but works
                    students.loc[
                        students["ID"] == stu_name, "VALUE"
                    ] -= scholarship_reqs[schol_name]["VALUE"]
                    students = students[students["VALUE"] > 0]
                    del scholarship_reqs[schol_name]

            # If all graphs are empty (there are no matches)
            if empty_count == len(graph):
                break

        print("\n\n\nBlossom Matches")

        assigned = 0
        for key in match_dict:
            assigned += len(match_dict[key])
            if len(match_dict[key]) >= 1:
                print(f"{key}: {match_dict[key]}")
        # End blossom

        # print(assigned)

        # BREAK BETWEEN STUFF

        # TO DO: Swap to minimize, set 0s to infinity, negate weight, and run multiple times. Sound simple enough?

        # Hungarian Matches
        # matrix = qualify_matrix(scholarship_reqs, students)
        # # print(matrix)
        # for row in matrix:
        #     print(row)
        # # row_ind, col_ind = linear_sum_assignment(matrix, maximize=True)

        # # New method
        # # Initialize Munkres algorithm
        # m = Munkres()

        # print("before compute")
        # # Perform the assignment (minimization on negated values)
        # indexes = m.compute(matrix)
        # print("after compute")

        # # Display the assignments
        # total_cost = 0
        # for row, column in indexes:
        #     value = matrix[row][column]
        #     total_cost += value
        #     print(f"({row}, {column}) -> {value}")

        # print(f"Total cost: {total_cost}")

        # The current way this works is a great example of why the linear_sum_assignment
        # doesn't work. It will still give out every scholarship even if they aren't qualified for
        # because it is just cost based

        # for i in range(len(row_ind)):
        #     print(
        #         "Scholarship:",
        #         scholarship_names[col_ind[i]],
        #         "  Student: ",
        #         # students.iloc[row_ind[i]]["Person Banner ID"],
        #         student_names[i],
        #         "  value: ",
        #         matrix[i][col_ind[i]],
        #     )

        # matches = []
        # subgraphs = qualify_graph(scholarship_reqs, students, matrix)
        # for graph in subgraphs:
        #     matches.append(nx.algorithms.bipartite.hopcroft_karp_matching(graph))

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

        # csv_headers = [
        #     "SCHOLARSHIP",
        #     "STUDENT",
        #     "ACT",
        #     "CHURCH",
        #     "GENDER",
        #     "GPA",
        #     "HIGH SCHOOL",
        #     "MAJOR",
        #     "MARRIED",
        #     "MINISTRY",
        #     "MINISTRY DEPENDENT",
        #     "NEED",
        #     "MINORITY",
        #     "STATE",
        # ]

        # csv_data = []

        # num_matches = 0
        # for match in blossom_matches:
        #     for tuple in match:
        #         # Tuple 0 is a scholarship. Else tuple[0] is a student
        #         # Very proprietary and inefficient testing code

        #         res = ["" for i in range(len(csv_headers))]

        #         scholarship_name = ""
        #         student_name = ""

        #         if "sch" in tuple[0]:
        #             student_name = tuple[1]
        #             scholarship_name = tuple[0]
        #         else:
        #             student_name = tuple[0]
        #             scholarship_name = tuple[1]

        #         print(f"{scholarship_name} {student_name}")
        #         num_matches += 1

        #         res[0] = scholarship_name
        #         res[1] = student_name

        #         scholarship = scholarships[scholarships["ID"] == scholarship_name]
        #         student = students[students["ID"] == student_name]
        #         for label, value in scholarship.items():
        #             if value.iloc[0] != "":
        #                 try:
        #                     index = csv_headers.index(label)
        #                     res[index] = (
        #                         f"Scholarship: {value.iloc[0]} Student: {student[label].iloc[0]}"
        #                     )
        #                 except:
        #                     pass

        #         csv_data.append(res)
        # print(num_matches)
        # # save_csv(headers=csv_headers, data=csv_data, name="sample_matches")
