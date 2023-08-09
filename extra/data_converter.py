from open_json import open_json
import json

def data_converter(output_file: str):
    # Opens the report_card.json file
    data = open_json("report_card")

    # Create a new dictionary to store the converted data
    converted_data = {}

    # Extract and convert subject details
    for report_type_name, report_type in data.items():
        for grade_name, grade in report_type.items():
            for semester_name, semester in grade.items():
                 if semester_name != "subjects":
                    for subject_name, subject_details in semester["subjects"].items():
                        if subject_details is not None:
                            # Check if the subject exists in the converted data dictionary
                            if subject_name not in converted_data:
                                converted_data[subject_name] = {}

                            # Check if the report type exists for the subject
                            if report_type_name not in converted_data[subject_name]:
                                converted_data[subject_name][report_type_name] = {}

                            # Check if the grade exists for the report type
                            if grade_name not in converted_data[subject_name][report_type_name]:
                               converted_data[subject_name][report_type_name][grade_name] = {}

                            # Check if the semester exists for the grade
                            if semester_name not in converted_data[subject_name][report_type_name][grade_name]:
                                converted_data[subject_name][report_type_name][grade_name][semester_name] = {}

                            # Store the subject details under the semester
                            converted_data[subject_name][report_type_name][grade_name][semester_name] = subject_details

    # Write the converted data to a new JSON file
    with open(output_file, 'w') as file:
        json.dump(converted_data, file, indent=4)

# Define the output file path
output_file = "data/subjects_report.json"

data_converter(output_file)

# I'm a lazy ass programmer so this was written by ChatGPT
# I also apologize for the excessive loops, but this will realistically be run like 20 times
# smh