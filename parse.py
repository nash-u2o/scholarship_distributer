import json
import os
import sys

import pandas as pd


def save_file(data):
    i = 0
    while True:
        file_str = (
            "scholarship_options.json" if i == 0 else f"scholarship_options({i}).json"
        )
        if not os.path.exists(file_str):
            with open(file_str, "w") as file:
                json.dump(data, file, indent=4)
                break
        else:
            i += 1


if __name__ == "__main__":
    if len(sys.argv) == 2:
        scholarship_path = sys.argv[1]
        scholarships = pd.read_excel(scholarship_path)
        scholarships.fillna(value=False, inplace=True)

        attrs = [
            "NEED",
            "DEPARTMENT",
            "MAJOR",
            "MINISTRY",
            "GENDER",
            "RELIGION",
            "CLASSIFICATION",
            "MARRIED",
            "RESIDENCE",
            "HIGH SCHOOL",
            "DESIGNATION",
            "ADMIT",
        ]

        # attrs = [
        #     "Need",
        #     "Lookup US County US State",
        #     "Application Academic Program",
        #     "Person Sex",
        #     "Schools GPA",
        #     "Addresses County",
        #     "Person Religion",
        #     "Call to Ministry",
        #     "Schools Name",
        #     "Application Church Name",
        #     "Person Marital Status",
        # ]
        cols = scholarships.columns
        rows = scholarships.iterrows()

        scholarship_options = {x: [] for x in attrs}
        print(scholarship_options)

        for index, row in rows:
            for key in scholarship_options:
                if key == "MAJOR" and row[key] is not False:
                    lower = str(row[key]).lower()
                    clean_string = lower.replace(" or ", ",").split(",")
                    for item in clean_string:
                        item = item.strip()
                        if item != "" and item not in scholarship_options[key]:
                            scholarship_options[key].append(item)
                elif (
                    row[key] is not False
                    and str(row[key]).lower() not in scholarship_options[key]
                ):
                    scholarship_options[key].append(str(row[key]).lower())

        save_file(scholarship_options)

        # for key in scholarship_options:
        #     print(key)
        #     print(scholarship_options[key])
        #     print()
