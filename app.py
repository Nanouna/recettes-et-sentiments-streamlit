import streamlit as st
import streamlit_tags as stt
import pandas as pd
import requests

tags_data = {
    'Categorie': ['Cuisine type', 'Diet type', 'Type', 'Occasion', 'Equipment'],
    'Tags': [['african',
        'american','amish mennonite','angolan','argentine',
        'asian','australian','austrian','beijing','belgian'
        'brazilian','british columbian','cajun','californian',
        'cambodian','canadian','cantonese','caribbean',
        'central american','chilean','chinese','colombian',
        'congolese','costa rican','creole','cuban',
        'czech','danish','dutch','ecuadorean',
        'egyptian','english','ethiopian','european',
        'filipino','finnish','french','georgian',
        'german','greek','guatemalan','hawaiian',
        'honduran','hunan','hungarian','icelandic',
        'indian','indonesian','iranian persian','iraqi',
        'irish','italian','japanese','jewish ashkenazi',
        'jewish sephardi','korean','laotian','lebanese',
        'libyan','malaysian','mexican','micro melanesia',
        'middle eastern','middle eastern main dish',
        'midwestern','mongolian','moroccan','namibian',
        'native american','nepalese','new zealand','nigerian',
        'north american','northeastern united states',
        'norwegian','oaxacan','ontario','pacific northwest',
        'pakistani','palestinian','pennsylvania dutch','peruvian',
        'polish','polynesian','portuguese','puerto rican',
        'quebec','russian','saudi arabian','scandinavian',
        'scottish','somalian','south african','south american',
        'south west pacific','southern united states',
        'southwestern united states','spanish','sudanese','swedish',
        'swiss','szechuan','tex mex','thai',
        'turkish','venezuelan','vietnamese','welsh'],
             ['dairy free','diabetic','dietary','egg free','eggs dairy',
        'free of something','gluten free','healthy','high calcium',
        'high fiber','high in something',
        'high in something diabetic friendly','high protein',
        'kosher','lactose','low calorie','low carb',
        'low cholesterol','low fat','low in something','low protein',
        'low saturated fat','low sodium','no shell fish','non alcoholic',
        'nut free','vegan','vegetarian','very low carbs'],
             ['appetizers','baking','beverages',
        'breakfast casseroles','breakfast eggs',
        'breakfast potatoes','brewing','broil','brownies',
        'burgers','cake fillings and frostings',
        'cakes','canning','casseroles','celebrity',
        'cheesecake','chutneys','clear soups','cobblers and crisps',
        'coffee cakes','college','comfort food','cookies and brownies',
        'cooking mixes','copycat','course','crock pot main dish',
        'crock pot slow cooker','crusts pastry dough 2',
        'cupcakes','curries','deep fry','desserts',
        'desserts easy','desserts fruit','dips','dips lunch snacks',
        'dips summer','drop cookies','fall','fillings and frostings chocolate',
        'finger food','flat shapes','from scratch','frozen desserts',
        'garnishes','granola and porridge','grilling','ham and bean soup',
        'hand formed cookies','heirloom historical','herb and spice mixes','ice cream',
        'inexpensive','infant baby friendly','jams and preserves','jellies',
        'kid friendly','lamb sheep main dish','lasagna','leftovers',
        'lunch','macaroni and cheese','main dish','main dish beef',
        'main dish chicken','main dish pasta','main dish pork','main dish seafood',
        'main ingredient','marinades and rubs','marinara sauce','mashed potatoes',
        'meatballs','meatloaf','muffins','mushroom soup',
        'no cook','novelty','number of servings','oamc freezer make ahead',
        'omelets and frittatas','one dish meal','pancakes and waffles','pasta rice and grains',
        'pasta salad','pies','pies and tarts','pitted fruit',
        'pizza','pot pie','pot roast','potluck',
        'preparation','prepared potatoes','presentation','puddings and mousses',
        'pumpkin bread','punch','quiche','quick breads',
        'ragu recipe contest','roast','roast beef comfort food','roast beef main dish',
        'rolled cookies','rolls biscuits','salad dressings','salsas',
        'saltwater fish','sandwiches','sauces','savory',
        'savory pies','savory sauces','scones','seafood',
        'seasonal','served cold','served hot','shakes',
        'shrimp main dish','side dishes','side dishes beans','simply potatoes',
        'smoothies','snacks','snacks kid friendly',
        'snacks sweet','sole and flounder','soul','soups stews',
        'spaghetti sauce','spicy','spreads','spring',
        'steam','stews','stews poultry','stir fry',
        'stocks','stuffings dressings','sugar cookies','summer',
        'sweet','sweet sauces','tarts','technique',
        'toddler friendly','tropical fruit','turkey burgers','vegetables',
        'veggie burgers','water bath','wings','winter'],
             ['april fools day','barbecue',
        'birthday','breakfast','brunch','camping',
        'chinese new year','christmas','cinco de mayo','cocktails',
        'dinner party','easter','fathers day','for 1 or 2',
        'for large groups','gifts','halloween','halloween cakes',
        'halloween cocktails','halloween cupcakes','hanukkah','holiday event',
        'independence day','kwanzaa','labor day','mardi gras carnival',
        'memorial day','mothers day','new years','passover',
        'picnic','ramadan','romantic','rosh hashanah',
        'served hot new years','st patricks day','superbowl','taste mood',
        'thanksgiving','to go','valentines day','wedding','weeknight'],
             ['bread machine',
        'brown bag','dehydrator','food processor blender','freezer',
        'microwave','mixer','oven','pressure canning',
        'pressure cooker','refrigerator','small appliance','smoker',
        'stove top','time to make','unprocessed freezer']]
}

df_tags = pd.DataFrame(tags_data)

# Exemple de liste d'ingrédients
ingredients_list = ['Poulet', 'Boeuf', 'Agneau', 'Carotte', 'Brocoli', 'Poivron', 'Sel', 'Poivre', 'Paprika']

# Dictionnaire de recettes
recipe_data = {
    'cream cheese bacon croissant': 414376,
    'cheesy meatball basil tomato sauce': 331985,
    'ramen sesame oriental salad': 420508,
    'fantasy peanut butter fudge': 271993,
    'honey roast onion': 80377,
    'turkey curry peanut sauce': 143495,
    'perfect honey cake': 139651,
    'walnut icebox kipfels': 265656,
    'brown rice jambalaya': 74579,
    'spice baby carrot': 226276,
    'coffee banana scone': 257068,
    'koolaid pie': 106096,
    'mozzarella tomato salad italian basil salad dress': 289599,
    'east meet west vegetable soba stir fry': 380551,
    'guilt free onion soup crock pot': 275840,
    'grandma norwegian kringla': 347906,
    'moo goo gai pan mah gu gai pin': 100359,
    'chicken potato florentine soup olive garden': 471979,
    'baked salmon black olive salsa': 164804,
    'razzy martini': 321267,
    'pineapple souffle': 339840,
    'surdyk greek orzo salad': 131009,
    'best potato chip cooky': 122964,
    'ratatouille bake weight watcher': 412275,
    'quick easy diabetic tiramisu': 115213,
    'dessert cake namur gateau namurois': 425018,
    'utterly deadly southern pecan pie': 101954,
    'dream coffee cake': 372510,
}

def display_results(results):
    suggestions = results.get('suggestions', [])
    for suggestion in suggestions:
        recipe_id, recipe_name, recipe_url = suggestion
        st.markdown(f"""
            <div style="border: 1px solid #ddd; border-radius: 10px; padding: 10px; margin: 10px 0;">
                <a href="{recipe_url}" target="_blank" style="text-decoration: none;">
                    <h3>{recipe_name}</h3>
                    <p>ID: {recipe_id}</p>
                </a>
            </div>
        """, unsafe_allow_html=True)

# Initialisation de l'état de la session pour suivre la page courante
if 'page' not in st.session_state:
    st.session_state.page = "Accueil"

# Barre latérale pour la navigation avec des boutons
st.sidebar.title("Recettes et sentiments")
if st.sidebar.button("Accueil"):
    st.session_state.page = "Accueil"
if st.sidebar.button("Recommander une recette"):
    st.session_state.page = "Recommander une recette"

# Fonction pour valider les tags
def validate_tags(selected_tags, valid_tags):
    return all(tag in valid_tags for tag in selected_tags)

# Affichage conditionnel basé sur la page sélectionnée
if st.session_state.page == "Accueil":
    st.header("Bienvenue sur l'application Recettes et sentiments")
    # Formulaire avec un champ de saisie auto-complété basé sur les clés du dictionnaire recipe_data
    recipe_name = st.selectbox('Choisissez une recette:', list(recipe_data.keys()))

    if st.button('Submit'):
        recipe_id = recipe_data.get(recipe_name, None)
        if recipe_id is not None:
            # Construire l'URL avec l'ID de recette sélectionnée
            url = f"https://recettes-et-sentiments-api-p4x6pl7fiq-ew.a.run.app/model_w2vec_similar_to_recipe?recipe_id={recipe_id}"
            # Envoyer la requête GET
            response = requests.get(url)
            if response.status_code == 200:
                results = response.json()
                display_results(results)
            else:
                st.error(f"Erreur lors de la requête : {response.status_code}")
        else:
            st.error("Recette non trouvée")

elif st.session_state.page == "Recommander une recette":
    st.header('Tell us what you would like to eat and we will recommend you a recipe')
    st.subheader('Get a recipe recommendation based on: ')

    # Radio button pour la sélection du modèle
    modelSelection = st.radio(label='',
                              options=['By tags', 'By ingredients', 'By tags & ingredients'],
                              horizontal=True)

    # Affichage conditionnel basé sur la sélection du modèle
    if modelSelection == 'By tags':
        tag_inputs = {}
        for index, row in df_tags.iterrows():
            tag_inputs[row['Categorie']] = stt.st_tags(
                label=f'Sélect {row["Categorie"]} tags',
                suggestions=row['Tags'],
            )

        if st.button('Soumettre Tags'):
            query = []
            for category, tags in tag_inputs.items():
                if validate_tags(tags, df_tags.loc[df_tags['Categorie'] == category, 'Tags'].values[0]):
                    query.extend(tags)

            # Construire l'URL de requête
            query_str = "%20".join(query)
            url = f"https://recettes-et-sentiments-api-p4x6pl7fiq-ew.a.run.app/model_w2vec_query_recipe?query={query_str}"
            # Envoyer la requête GET
            response = requests.get(url)
            if response.status_code == 200:
                results = response.json()
                display_results(results)
            else:
                st.error(f"Erreur lors de la requête : {response.status_code}")

    elif modelSelection == 'By ingredients':
        ingredients_input = stt.st_tags(
            label='Sélectionnez des ingrédients',
            suggestions=ingredients_list,
        )

        if st.button('Soumettre Ingrédients'):
            if validate_tags(ingredients_input, ingredients_list):
                query_str = "%20".join(ingredients_input)
                url = f"https://recettes-et-sentiments-api-p4x6pl7fiq-ew.a.run.app/model_w2vec_query_recipe?query={query_str}"
                response = requests.get(url)
                if response.status_code == 200:
                    results = response.json()
                    display_results(results)
                else:
                    st.error(f"Erreur lors de la requête : {response.status_code}")
            else:
                st.error('Vous avez entré un ou plusieurs ingrédients invalides')

    elif modelSelection == 'By tags & ingredients':
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
            all_valid = True
            query = []
            for category, tags in tag_inputs.items():
                if validate_tags(tags, df_tags.loc[df_tags['Categorie'] == category, 'Tags'].values[0]):
                    query.extend(tags)
                else:
                    st.error(f'Vous avez entré un ou plusieurs tags invalides pour {category}')
                    all_valid = False

            if validate_tags(ingredients_input, ingredients_list):
                query.extend(ingredients_input)
            else:
                st.error('Vous avez entré un ou plusieurs ingrédients invalides')
                all_valid = False

            if all_valid:
                query_str = "%20".join(query)
                url = f"https://recettes-et-sentiments-api-p4x6pl7fiq-ew.a.run.app/model_w2vec_query_recipe?query={query_str}"
                response = requests.get(url)
                if response.status_code == 200:
                    results = response.json()
                    display_results(results)
                else:
                    st.error(f"Erreur lors de la requête : {response.status_code}")
