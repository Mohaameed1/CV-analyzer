# CV Analyzer IA 🚀

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Machine Learning](https://img.shields.io/badge/ML-TF--IDF-green)
![NLP](https://img.shields.io/badge/NLP-spaCy-orange)

## Description
CV Analyzer est un **système intelligent en Python** capable d’analyser automatiquement un CV PDF, calculer un score pondéré en fonction des compétences, mesurer la compatibilité avec une offre d’emploi et générer des recommandations personnalisées.

C’est un projet parfait pour les développeurs ou ingénieurs souhaitant démontrer leur maîtrise de :
- NLP (Natural Language Processing)
- Machine Learning (TF-IDF)
- Traitement de fichiers PDF
- Analyse de CV / matching emploi

---

## Fonctionnalités

- Extraction automatique de texte depuis un CV PDF
- Détection des compétences clés avec pondération
- Calcul d’un score global (/100)
- Mesure de la compatibilité CV ↔ offre d’emploi
- Génération de conseils personnalisés pour améliorer le CV

---

## Installation

1. Cloner le dépôt :

```bash
git clone https://github.com/Mohaameed1/cv-analyzer-ia.git
cd cv-analyzer-ia

2.Créer un environnement virtuel :

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


3.Installer les dépendances :

pip install -r requirements.txt

4.Utilisation
python app.py

5.Structure du projet
cv-analyzer/
│
├── app.py
├── cv_parser.py
├── scorer.py
├── recommender.py
├── similarity.py
├── cv.pdf
├── job_offer.txt
└── data/
    └── job_keywords.txt

.............A propos...................

Projet développé par Mohamed Amorri.
Idéal pour démontrer des compétences en Python, NLP, ML et développement de projets IA.
