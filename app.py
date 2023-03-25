import streamlit as st

# Définition d'une liste de personnes
personnes = [
    {"nom": "Jane Doe", "age": 28, "niveau_anxiete": "Assez", "description": "Je suis une personne calme et réfléchie, j'aime aider les autres à surmonter leurs peurs."},
    {"nom": "John Smith", "age": 35, "niveau_anxiete": "Très", "description": "Je suis un passionné de sports extrêmes et j'aime défier mes limites."},
    {"nom": "Alice Johnson", "age": 42, "niveau_anxiete": "Un peu", "description": "Je suis une personne optimiste qui aime découvrir de nouvelles choses."},
    {"nom": "Bob Brown", "age": 50, "niveau_anxiete": "Pas du tout", "description": "Je suis une personne très détendue qui ne se laisse pas facilement stresser."},
    {"nom": "Sarah Lee", "age": 25, "niveau_anxiete": "Assez", "description": "Je suis une personne créative qui trouve souvent des solutions originales aux problèmes."},
]

# Titre de l'application
st.title("Mon application de jeu")
st.image("image.png", caption="Une image pour vous inspirer")

# Formulaire pour obtenir les informations de l'utilisateur
nom_utilisateur = st.text_input("Entrez votre nom")
age_utilisateur = st.number_input("Entrez votre âge")
niveau_anxiete = st.selectbox("À quel point vous sentez-vous anxieux en général ?", ["Pas du tout", "Un peu", "Assez", "Très"])

# Affichage des informations de l'utilisateur
st.write("Bienvenue", nom_utilisateur, "!")
st.write("Vous avez", age_utilisateur, "ans et vous vous sentez", niveau_anxiete, "anxieux en général.")

# Définition des défis en fonction du niveau d'anxiété de l'utilisateur
if niveau_anxiete == "Pas du tout":
    st.write("Défi facile : dessinez une image de vous-même")
elif niveau_anxiete == "Un peu":
    st.write("Défi moyen : écrivez un paragraphe sur votre plus grande peur")
elif niveau_anxiete == "Assez":
    st.write("Défi difficile : contactez quelqu'un que vous n'avez pas parlé depuis longtemps")
else:
    st.write("Défi très difficile : donnez un discours en public")

# Section pour la mise en relation entre personnes
st.header("Mise en relation avec d'autres joueurs")
st.write("Si vous avez besoin d'aide pour relever votre défi, vous pouvez vous connecter avec d'autres joueurs dans cette section.")

# Formulaire pour la mise en relation
niveau_anxiete_recherche = st.selectbox("À quel niveau d'anxiété cette personne doit-elle être ?", ["Pas du tout", "Un peu", "Assez", "Très"])

# Bouton pour rechercher des personnes
if st.button("Rechercher des personnes"):
    st.write("Voici les résultats de votre recherche :")
    # Tri des personnes en fonction du niveau d'anxiété
    personnes_filtrees = [personne for personne in personnes if personne["niveau_anxiete"] == niveau_anxiete_recherche]
    # Affichage des personnes filtrées
    if len(personnes_filtrees) == 0:
        st.write("Aucune personne correspondant aux critères de recherche n'a été trouvée.")
    else:
        for personne in personnes_filtrees:
           st.write(personnes[])
