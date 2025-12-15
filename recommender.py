def generate_advice(score, found_skills, all_skills):
    advice = []

    missing_skills = list(set(all_skills) - set(found_skills))

    if score < 50:
        advice.append("Ajoutez davantage de compétences techniques pertinentes.")
    elif score < 75:
        advice.append("Votre CV est bon, mais peut être renforcé avec plus de mots-clés techniques.")
    else:
        advice.append("Excellent CV bien aligné avec le poste.")

    if missing_skills:
        advice.append(
            "Compétences à ajouter ou mettre en valeur : " +
            ", ".join(missing_skills)
        )

    return advice
