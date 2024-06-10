import streamlit as st
import streamlit_tags as stt
import pandas as pd

st.title('Recettes et sentiments')
st.subheader('Tell us what you would like to eat and will recommand you a recipe')
st.text('Get a recipe recommandation based on: ')

tags_data = {
    'Categorie': ['Fruit', 'Légume', 'Boisson'],
    'Tags': [['Pomme', 'Banane', 'Orange'], ['Carotte', 'Brocoli', 'Épinard'], ['Eau', 'Jus', 'Soda']]
}
df_tags = pd.DataFrame(tags_data)

ingredients_list = ['Poulet', 'Boeuf', 'Agneau', 'Carotte', 'Brocoli', 'Poivron', 'Sel', 'Poivre', 'Paprika']

modelSelection = st.radio(label='',
                          options=['Tags only', 'Ingredients only', 'Tags & ingredients'],
                          horizontal=True,
                          )

# Affichage conditionnel basé sur la sélection du modèle
if modelSelection == 'Tags only':
    # Afficher un nombre d'inputs de tags pour chaque catégorie de tag
    tag_inputs = {}
    for index, row in df_tags.iterrows():
        tag_inputs[row['Categorie']] = stt.st_tags(
            label=f'Sélectionnez des tags pour {row["Categorie"]}',
            suggestions=row['Tags'],
        )

    if st.button('Soumettre Tags'):
        for category, tags in tag_inputs.items():
            st.write(f'Vous avez entré pour {category} : {tags}')

elif modelSelection == 'Ingredients only':
    # Afficher un input pour les ingrédients
    ingredients_input = stt.st_tags(
        label='Sélectionnez des ingrédients',
        suggestions=ingredients_list,
    )

    if st.button('Soumettre Ingrédients'):
        st.write(f'Vous avez entré les ingrédients : {ingredients_input}')

elif modelSelection == 'Tags & ingredients':
    # Entrée de texte pour les tags et les ingrédients
    tag_inputs = {}
    for index, row in df_tags.iterrows():
        tag_inputs[row['Categorie']] = stt.st_tags(
            label=f'Sélectionnez des tags pour {row["Categorie"]}',
            suggestions=row['Tags'],
        )

    ingredients_input = stt.st_tags(
        label='Sélectionnez des ingrédients',
        suggestions=ingredients_list,
    )

    if st.button('Soumettre Tout'):
        for category, tags in tag_inputs.items():
            st.write(f'Vous avez entré pour {category} : {tags}')
        st.write(f'Vous avez entré les ingrédients : {ingredients_input}')
