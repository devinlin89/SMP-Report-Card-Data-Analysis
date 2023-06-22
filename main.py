from most_change import best_improving
from most_change import worst_regressing
from open_json import open_json

# Opens the JSON files
report_card = open_json("report_card")
subjects_report = open_json("subjects_report")

start_report = ("final_report", "grade_7", "semester_1")
end_report = ("final_report", "grade_9", "semester_2")
score_types = ("Knowledge", "Skill", "Attitude")

def subject_improvement(start, end, score_type, subjects_report):
    # Prints out the best improving and worst regressing subject of a certain score type

    # Finds best improving subject and worst regressing subject
    best_improving_subject = best_improving(start, end, score_type, subjects_report)
    worst_regressing_subject = worst_regressing(start, end, score_type, subjects_report)

    print(f"Best Improving Subject In {score_type}:")
    print("Subject: ", best_improving_subject["subject"])
    print("Score difference: ", best_improving_subject["score_difference"])
    print("Starting Score: ", best_improving_subject["start_score"])
    print("Ending Score: ", best_improving_subject["end_score"])
    print()

    print(f"Worst Regressing Subject In {score_type}:")
    print("Subject: ", worst_regressing_subject["subject"])
    print("Score difference: ", worst_regressing_subject["score_difference"])
    print("Starting Score: ", worst_regressing_subject["start_score"])
    print("Ending Score: ", worst_regressing_subject["end_score"])
    print()

for score_type in score_types:
    subject_improvement(start_report, end_report, score_type , subjects_report)