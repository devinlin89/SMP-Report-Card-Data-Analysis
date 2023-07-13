import sys
from most_change import best_improving, worst_regressing
from best_worst import best_subject, worst_subject
from open_json import open_json

sys.stdout = open('output.txt','wt')

print("# SMP Report Card Data Analysis")
print()
print()

# Opens the JSON files
report_card = open_json("report_card")
subjects_report = open_json("subjects_report")

semesters = (
    ("final_report", "grade_7", "semester_1"),
    ("final_report", "grade_7", "semester_2"),
    ("final_report", "grade_8", "semester_1"),
    ("final_report", "grade_8", "semester_2"),
    ("final_report", "grade_9", "semester_1"),
    ("final_report", "grade_9", "semester_2"),
)

start_report = semesters[0]
end_report = semesters[-1]
score_types = ("Knowledge", "Skill", "Attitude", "Overall")

def subject_improvement(start, end, score_type, subjects_report):
    # Prints out the best improving and worst regressing subject of a certain score type

    # Finds best improving subject and worst regressing subject
    best_improving_subject = best_improving(start, end, score_type, subjects_report)
    worst_regressing_subject = worst_regressing(start, end, score_type, subjects_report)

    print(f"*Best Improving Subject In {score_type}:*")
    print("Subject: ", best_improving_subject["subject"])
    print("Score difference: ", best_improving_subject["score_difference"])
    print("Starting Score: ", best_improving_subject["start_score"])
    print("Ending Score: ", best_improving_subject["end_score"])
    print()

    print(f"*Worst Regressing Subject In {score_type}:*")
    print("Subject: ", worst_regressing_subject["subject"])
    print("Score difference: ", worst_regressing_subject["score_difference"])
    print("Starting Score: ", worst_regressing_subject["start_score"])
    print("Ending Score: ", worst_regressing_subject["end_score"])
    print()

print("## Improvement and Regression")
print()

for score_type in score_types:
    subject_improvement(start_report, end_report, score_type , subjects_report)

def subject_best_worst(semester, score_type, subjects_report):
    # Prints out the best improving and worst regressing subject of a certain score type

    # Finds best improving subject and worst regressing subject
    best_scoring_subject = best_subject(semester, score_type, subjects_report)
    worst_scoring_subject = worst_subject(semester, score_type, subjects_report)

    print(f"*Best Subject In {score_type}:*")
    print("Subject: ", best_scoring_subject["subject"])
    print("Score difference: ", best_scoring_subject["score"])
    print()

    print(f"*Worst Subject In {score_type}:*")
    print("Subject: ", worst_scoring_subject["subject"])
    print("Score difference: ", worst_scoring_subject["score"])
    print()

print("## Best and Worst")
print()

for semester in semesters:
    print()

    report_type = semester[0].replace('_', ' ').title()
    grade = semester[1].replace('_', ' ').title()
    semester_num = semester[2].replace('_', ' ').title()

    print(f"### {report_type} of {grade} {semester_num}:")
    print()
    for score_type in score_types:
        subject_best_worst(semester, score_type , subjects_report)