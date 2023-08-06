from open_json import open_json

def print_all_subjects():
    # Opens the report_card.json file
    report_card = open_json("report_card")

    # Goes through mid reports and final reports
    for report_type_name, report_type in report_card.items():
        report_type_name = report_type_name.replace("_", " ").title()

        # Goes through every grade from 7 to 9
        for grade_name, grade in report_type.items():
            grade_name = grade_name.replace("_", " ").title()

            # Goes through semester 1 and 2 for every grade
            for semester_name, semester in grade.items():
                semester_name = semester_name.replace("_", " ").title()

                print(f"Report Type: {report_type_name}")
                print(f"Grade: {grade_name}")
                print(f"Semester: {semester_name}")
                print()
                print("Subject Details:")

                # Prints out knowledge, skill, and attitude scores of the subject
                for subject_name, subject_details in semester["subjects"].items():

                    # Unless the subject is null
                    if subject_details is not None:
                        print(f"  Subject: {subject_name}")
                        for key, value in subject_details.items():
                            print(f"    {key}: {value}")
                print()

print_all_subjects()

# I'm a lazy ass programmer so this was written by ChatGPT
# I also apologize for the excessive loops, but this will realistically be run like 20 times
# smh