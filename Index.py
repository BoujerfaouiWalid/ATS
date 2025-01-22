import os
import re
from docx import Document

# Liste des mots-clés et leur pondération pour un développeur Front-End
keywords = {
    "html": 5,
    "css": 5,
    "javascript": 5,
    "react": 6,
    "vue.js": 6,
    "angular": 6,
    "bootstrap": 4,
    "git": 5,
    "responsive design": 4,
    "ux/ui design": 5,
    "node.js": 6,
    "rest apis": 5,
    "webpack": 4,
    "sass": 4,
    "agile": 3,
    "esprit d'équipe": 3,
    "communication": 3,
    "anglais": 4,
    "résolution de problèmes": 3,
    "créativité": 2,
    "collaboration": 3
}

# Score minimal pour être accepté
score_minimal = 30

# Fonction pour lire le contenu d'un fichier Word
def read_word(file_name):
    try:
        # Chemin du bureau
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, file_name)

        # Vérifie si le fichier existe
        if not os.path.exists(file_path):
            print(f"Fichier '{file_name}' introuvable sur le bureau.")
            return ""

        # Ouvre et lit le fichier Word
        doc = Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + " "
        return text.lower()  # Convertir en minuscules pour la comparaison
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return ""

# Fonction pour calculer le score d'un fichier
def calculate_score(text_content, keywords):
    score = 0
    for keyword, weight in keywords.items():
        # Vérifie si le mot-clé est présent dans le texte
        if re.search(rf"\b{keyword.lower()}\b", text_content):
            score += weight  # Ajouter la pondération du mot-clé une seule fois
    return score

# Programme principal
def main():
    print("Bienvenue dans le système ATS (Applicant Tracking System) pour un développeur Front-End.")
    print("Entrez le **nom du fichier Word** (exemple : CV.docx) situé sur votre bureau :")
    file_name = input("Nom du fichier : ").strip()

    # Lire le fichier Word
    text_content = read_word(file_name)
    if not text_content:  # Si le contenu du fichier est vide ou le fichier est introuvable
        print("Impossible d'analyser le fichier. Vérifiez le nom et assurez-vous qu'il est sur votre bureau.")
        return

    # Calculer le score
    score = calculate_score(text_content, keywords)

    # Afficher le score et le résultat
    print(f"\nVotre score sur 70 est : {score}")
    if score >= score_minimal:
        print("Félicitations ! Vous êtes accepté.")
    else:
        print("Désolé, votre candidature a été refusée. Améliorez votre CV en incluant des compétences pertinentes.")

# Exécuter le programme
if __name__ == "__main__":
    main()
