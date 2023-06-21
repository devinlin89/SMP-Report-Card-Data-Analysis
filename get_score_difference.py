def get_score_difference(start_report, end_report, score_type, subject):
    # Finds score difference between start score and end score

    start_score = subject[start_report["type"]][start_report["grade"]][start_report["semester"]][score_type]
    end_score = subject[end_report["type"]][end_report["grade"]][end_report["semester"]][score_type]

    return end_score - start_score