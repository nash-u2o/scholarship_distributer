import csv
import os

from scholarship import create_scholarship
from student import create_student

# Order of attributes: ACT, CHURCH, COUNTY, GENDER, GPA, HIGH SCHOOL, MAJOR, MARRIED, MINISTRY, MINISTRY DEPENDENT, NEED, MINORITY, STATE


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


if __name__ == "__main__":
    # leave out columns that just don't matter that much. Right now: county
    headers = [
        "ID",
        "ACT",
        "CHURCH",
        # "COUNTY",
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
    student_rows = create_student(100)
    save_csv(headers, student_rows, "random_students")
    scholarship_rows = create_scholarship(50)
    save_csv(headers, scholarship_rows, "random_scholarships")
