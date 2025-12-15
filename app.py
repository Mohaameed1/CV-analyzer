from cv_parser import extract_text_from_pdf
from scorer import extract_weighted_skills, calculate_weighted_score
from recommender import generate_advice
from similarity import compute_similarity


# ==============================
# 1️⃣ Charger le CV
# ==============================
cv_text = extract_text_from_pdf("cv.pdf")


# ==============================
# 2️⃣ Charger l’offre d’emploi
# ==============================
with open("job_offer.txt", "r", encoding="utf-8") as f:
    job_text = f.read().lower()


# ==============================
# 3️⃣ Charger les compétences pondérées
# Format : skill:poids
# ==============================
skills = {}
max_score = 0

with open("data/job_keywords.txt", "r", encoding="utf-8") as f:
    for line in f:
        skill, weight = line.strip().split(":")
        weight = int(weight)
        skills[skill.lower()] = weight
        max_score += weight


# ==============================
# 4️⃣ Analyse des compétences
# ==============================
weighted_score, found_skills = extract_weighted_skills(cv_text, skills)
final_score = calculate_weighted_score(weighted_score, max_score)


# ==============================
# 5️⃣ Similarité CV ↔ Offre (ML)
# ==============================
similarity_score = compute_similarity(cv_text, job_text)


# ==============================
# 6️⃣ Générer les conseils IA
# ==============================
advice = generate_advice(final_score, found_skills, list(skills.keys()))


# ==============================
# 7️⃣ Affichage final
# ==============================
print("\n===== ANALYSE DU CV =====\n")

print("Compétences trouvées :")
print(found_skills)

print(f"\nScore compétences pondéré : {final_score} / 100")
print(f"Compatibilité avec l’offre : {similarity_score} %")

print("\nConseils IA :")
for a in advice:
    print("-", a)
