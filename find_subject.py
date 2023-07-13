from get_score_difference import get_score_difference
from calculate_overall_score import calculate_overall_score

def find_subject(report_semester, score_type, subjects_report, compare_func):
    # Finds best or worst subject score depending on the lambda function inputted

    best_subject = ""
    best_score = None

    # Loops through every subject
    for subject_name, subject in subjects_report.items():

        # Checks if subject is in both start grade and end grade
        if report_semester["grade"] in subject.get(report_semester["type"], {}):

            # Checks if score_type is overall
            if score_type == "Overall":
                overall_score = calculate_overall_score(subject[report_semester["type"]][report_semester["grade"]][report_semester["semester"]])
                if overall_score is None:
                    continue  # Skip subjects with missing scores for overall calculation
                current_score = round(overall_score, 2)
            else:
                current_score = subject[report_semester["type"]][report_semester["grade"]][report_semester["semester"]].get(score_type)

            # If the loop is in the first iteration,
            # the score of the first subject will replace the best_score and best_subject

            # Further iterations of the loop will replace it if it's lower or higher
            # Depending on the lambda function in the parameters
            if current_score is not None and (best_score is None or compare_func(current_score, best_score)):
                best_score = current_score
                best_subject = subject_name

    subject_dict = {
        "subject": best_subject,
        "score": best_score,
    }

    return subject_dict

def find_subject_change(start_report, end_report, score_type, subjects_report, compare_func):
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

    if score_type == "Overall":
        start_score = round(calculate_overall_score(subjects_report[best_subject][start_report["type"]][start_report["grade"]][start_report["semester"]]), 2)
        end_score = round(calculate_overall_score(subjects_report[best_subject][end_report["type"]][end_report["grade"]][end_report["semester"]]), 2)
    else:
        start_score = round(subjects_report[best_subject][start_report["type"]][start_report["grade"]][start_report["semester"]][score_type], 2)
        end_score = round(subjects_report[best_subject][end_report["type"]][end_report["grade"]][end_report["semester"]][score_type], 2)

    subject_dict = {
        "subject": best_subject,
        "score_difference": best_score,
        "start_score": start_score,
        "end_score": end_score
    }

    return subject_dict