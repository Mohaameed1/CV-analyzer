def extract_weighted_skills(text, skills_dict):
    score = 0
    found = []

    for skill, weight in skills_dict.items():
        if skill.lower() in text:
            score += weight
            found.append(skill)

    return score, found


def calculate_weighted_score(score, max_score):
    return int((score / max_score) * 100) if max_score > 0 else 0
