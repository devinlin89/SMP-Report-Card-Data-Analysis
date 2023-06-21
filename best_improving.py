def best_improving_knowledge (start: tuple[str, str, str], end: tuple[str, str, str], score_type, subjects_report):
    start_report_type, start_report_grade, start_report_semester = start
    end_report_type, end_report_grade, end_report_semester = end

    best_improving_subject = ""
    best_improving_score = 0

    for subject_name, subject in subjects_report.items():
        print(subject_name)

        if start_report_grade in subject[start_report_type] and (end_report_grade in subject[end_report_type]):
            start_score = subject[start_report_type][start_report_grade][start_report_semester][score_type]
            end_score = subject[end_report_type][end_report_grade][end_report_semester][score_type]

        difference = end_score - start_score

        if difference > best_improving_score:
            best_improving_score = difference
            best_improving_subject = subject_name

    return best_improving_subject