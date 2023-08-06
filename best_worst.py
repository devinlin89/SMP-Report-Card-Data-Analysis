from find_subject import find_subject
from find_subject import find_subject_change

def best_subject(semester, score_type, subjects_report):
    # Finds best improving score subject
    report_semester = {"type": semester[0], "grade": semester[1], "semester": semester[2]}

    return find_subject(report_semester, score_type, subjects_report, lambda a, b: a > b)

def worst_subject(semester, score_type, subjects_report):
    # Finds worst regressing score subject
    report_semester = {"type": semester[0], "grade": semester[1], "semester": semester[2]}

    return find_subject(report_semester, score_type, subjects_report, lambda a, b: a < b)

def best_improving(start, end, score_type, subjects_report):
    # Finds best improving score subject
    start_report = {"type": start[0], "grade": start[1], "semester": start[2]}
    end_report = {"type": end[0], "grade": end[1], "semester": end[2]}
    return find_subject_change(start_report, end_report, score_type, subjects_report, lambda a, b: a > b)

def worst_regressing(start, end, score_type, subjects_report):
    # Finds worst regressing score subject
    start_report = {"type": start[0], "grade": start[1], "semester": start[2]}
    end_report = {"type": end[0], "grade": end[1], "semester": end[2]}
    return find_subject_change(start_report, end_report, score_type, subjects_report, lambda a, b: a < b)