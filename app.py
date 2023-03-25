import streamlit as st

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
nom_recherche = st.text_input("Entrez le nom de la personne que vous cherchez")
niveau_anxiete_recherche = st.selectbox("À quel niveau d'anxiété cette personne doit-elle être ?", ["Pas du tout", "Un peu", "Assez", "Très"])

# Bouton pour rechercher une personne
if st.button("Rechercher une personne"):
    st.write("Voici les résultats de votre recherche :")
    # Requête à une base de données (hypothétique) pour trouver une personne correspondant aux critères de recherche
    # Affichage des résultats de la recherche
    st.write("Nom : Jane Doe")
    st.write("Âge : 28 ans")
    st.write("Niveau d'anxiété : Assez")
    st.write("Description : Je suis une personne calme et réfléchie, j'aime aider les autres à surmonter leurs peurs.")

    # Bouton pour contacter la personne
    if st.button("Contacter cette personne"):
        st.write("Vous avez contacté Jane Doe !")
