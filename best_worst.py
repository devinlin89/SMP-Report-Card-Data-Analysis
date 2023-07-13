from find_subject import find_subject

def best_subject(semester, score_type, subjects_report):
    # Finds best improving score subject
    report_semester = {"type": semester[0], "grade": semester[1], "semester": semester[2]}

    return find_subject(report_semester, score_type, subjects_report, lambda a, b: a > b)

def worst_subject(semester, score_type, subjects_report):
    # Finds worst regressing score subject
    report_semester = {"type": semester[0], "grade": semester[1], "semester": semester[2]}

    return find_subject(report_semester, score_type, subjects_report, lambda a, b: a < b)