from most_change import best_improving
from most_change import worst_regressing
from open_json import open_json

report_card = open_json("report_card")
subjects_report = open_json("subjects_report")

print(best_improving(("final_report", "grade_7", "semester_1"), ("final_report", "grade_9", "semester_2"), "Knowledge", subjects_report))
print(worst_regressing(("final_report", "grade_7", "semester_1"), ("final_report", "grade_9", "semester_2"), "Knowledge", subjects_report))
