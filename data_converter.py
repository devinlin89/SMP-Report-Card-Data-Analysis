from open_json import open_json

def data_converter():
    report_card = open_json("report_card")

    for report_type_name, report_type in report_card.items():
        report_type_name = report_type_name.replace("_", " ").title()

        for grade_name, grade in report_type.items():
            grade_name = grade_name.replace("_", " ").title()

            for semester_name, semester in grade.items():
                semester_name = semester_name.replace("_", " ").title()

                print(f"Report Type: {report_type_name}")
                print(f"Grade: {grade_name}")
                print(f"Semester: {semester_name}")
                print()
                print("Subject Details:")
                for subject_name, subject_details in semester["subjects"].items():
                    if subject_details is not None:
                        print(f"  Subject: {subject_name}")
                        for key, value in subject_details.items():
                            print(f"    {key}: {value}")
                print()

data_converter()