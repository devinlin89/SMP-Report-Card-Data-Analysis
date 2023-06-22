from most_change import best_improving
from most_change import worst_regressing
from open_json import open_json

report_card = open_json("report_card")
subjects_report = open_json("subjects_report")

def subject_improvement(start, end, score_type, subjects_report):
    improving_subject = best_improving(start, end, score_type, subjects_report)
    regressing_subject = worst_regressing(start, end, score_type, subjects_report)

    print(f"Best Improving Subject In {score_type}:")
    print("Subject: ", improving_subject["subject"])
    print("Score difference: ", improving_subject["score_difference"])
    print("Starting Score: ", improving_subject["start_score"])
    print("Ending Score: ", improving_subject["end_score"])
    print()

    print(f"Worst Regressing Subject In {score_type}:")
    print("Subject: ", regressing_subject["subject"])
    print("Score difference: ", regressing_subject["score_difference"])
    print("Starting Score: ", regressing_subject["start_score"])
    print("Ending Score: ", regressing_subject["end_score"])
    print()


start_report = ("final_report", "grade_7", "semester_1")
end_report = ("final_report", "grade_9", "semester_2")
score_types = ["Knowledge", "Skill", "Attitude"]

for score_type in score_types:
    subject_improvement(start_report, end_report, score_type , subjects_report)
print(best_improving(("final_report", "grade_7", "semester_1"), ("final_report", "grade_9", "semester_2"), "Knowledge", subjects_report))
print(worst_regressing(("final_report", "grade_7", "semester_1"), ("final_report", "grade_9", "semester_2"), "Knowledge", subjects_report))
