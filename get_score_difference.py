from calculate_overall_score import calculate_overall_score

def get_score_difference(start_report, end_report, score_type, subject):
    # Finds score difference between start score and end score

    if score_type == "Overall":
        start_score = calculate_overall_score(subject[start_report["type"]][start_report["grade"]][start_report["semester"]])
        end_score = calculate_overall_score(subject[end_report["type"]][end_report["grade"]][end_report["semester"]])
    else:
        start_score = subject[start_report["type"]][start_report["grade"]][start_report["semester"]][score_type]
        end_score = subject[end_report["type"]][end_report["grade"]][end_report["semester"]][score_type]

    # If score doesn't exist, the difference is 0
    if start_score == None or end_score == None:
        return 0

    # Calculates difference and rounds to 2 decimal places
    difference = round(end_score - start_score, 2)

    return difference