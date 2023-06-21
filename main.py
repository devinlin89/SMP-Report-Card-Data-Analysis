from best_improving import best_improving_knowledge
from open_json import open_json

report_card = open_json("report_card")
subjects_report = open_json("subjects_report")

print(best_improving_knowledge(("mid_report", "grade_7", "semester_1"), ("mid_report", "grade_9", "semester_2"), "Knowledge", subjects_report))