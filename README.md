# ATS
Ce projet consiste en la création d'un système de suivi des candidatures (ATS) simple en Python. L'objectif est de permettre aux candidats de soumettre leur CV sous forme de fichier Word, qui sera ensuite analysé pour évaluer leur adéquation à un poste de développeur Front-End. Le système se base sur une série de mots-clés liés aux compétences techniques (HTML, CSS, JavaScript, React, etc.) et aux soft skills (Agile, communication, travail en équipe) présents dans le CV. Le score total est calculé en fonction de la présence de ces mots-clés et permet de déterminer si la candidature est acceptée ou refusée.

## Fonctionnalités principales :
- Téléchargement du CV : L'utilisateur soumet son CV au format Word.
- Analyse de contenu : Le programme parcourt le texte du CV pour rechercher des mots-clés liés aux compétences techniques et soft skills d'un développeur Front-End.
- Calcul du score : Un score est attribué en fonction de la fréquence des mots-clés trouvés. La pondération varie en fonction de l'importance des compétences.
- Résultats : Le système retourne un score global et indique si la candidature est acceptée ou refusée, en fonction d'un score minimal défini.

## Compétences évaluées :
Compétences techniques : HTML, CSS, JavaScript, React, Vue.js, Node.js, Git, Responsive Design, UX/UI Design, REST APIs, et bien plus.
Soft skills : Agile, communication, esprit d'équipe, résolution de problèmes, créativité, etc.

## Instructions d'installation :
- Clonez le repository :
git clone https://github.com/votre-utilisateur/ATS.git

## Installez les dépendances :
pip install python-docx

## Lancez le programme :
python ats.py
Entrez le nom de votre fichier CV et obtenez votre score !
