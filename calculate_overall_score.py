def calculate_overall_score(subject):
    # Calculates overall score of subject by finding average of all scores.
    # Attitude is multiplied by 25

    knowledge_score = subject["Knowledge"]
    skill_score = subject["Skill"]
    attitude_score = subject["Attitude"]

    if skill_score is None or attitude_score is None:
        return knowledge_score

    overall_score = (knowledge_score + skill_score + (attitude_score * 25)) / 3

    return overall_score