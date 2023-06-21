from get_score_difference import get_score_difference

def find_subject(start_report, end_report, score_type, subjects_report, compare_func):
    # Finds best improving or worst regressing subject score depending on the lambda function inputted

    best_subject = ""
    best_score = None

    # Loops through every subject
    for subject_name, subject in subjects_report.items():
        # Checks if subject is in both start grade and end grade

        if (
            start_report["grade"] in subject[start_report["type"]] and
            end_report["grade"] in subject[end_report["type"]]
        ):
            # Calculates score difference between start grade and end grade
            difference = get_score_difference(start_report, end_report, score_type, subject)

            # If the loop is in the first iteration,
            # the difference of the first subject will replace the best_score and best_subject

            # Further iterations of the loop will replace it if it's lower or higher
            # Depending on the lambda function in the parameters
            if best_score is None or compare_func(difference, best_score):
                best_score = difference
                best_subject = subject_name

    return best_subject