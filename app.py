import streamlit as st

# Titre de l'application
st.title("Mon application de jeu")
# Affichage d'une image
st.image("image.png", caption="Une image pour vous inspirer")
# Formulaire pour obtenir les informations de l'utilisateur
nom_utilisateur = st.text_input("Entrez votre nom")
difficulte = st.selectbox("Choisissez votre niveau de difficulté", ["Facile", "Moyen", "Difficile"])

# Affichage des informations de l'utilisateur
st.write("Bienvenue", nom_utilisateur, "!")
st.write("Vous avez choisi le niveau de difficulté", difficulte)

# Définition des défis en fonction du niveau de difficulté
if difficulte == "Facile":
    st.write("Défi facile : dessinez une image de vous-même")
elif difficulte == "Moyen":
    st.write("Défi moyen : écrivez un paragraphe sur votre plus grande peur")
else:
    st.write("Défi difficile : contactez quelqu'un que vous n'avez pas parlé depuis longtemps")

# Bouton pour commencer le jeu
if st.button("Commencer le jeu"):
    st.write("Le jeu commence !")
