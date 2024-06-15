import streamlit as st
from deep_translator import GoogleTranslator
import joblib
import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD


# Chargement des modèles pré-entraînés
amazon_ratings = pd.read_csv('e_commerce_recommendation_data.csv')
model_search = joblib.load(filename='search_recom.joblib')
vectorizer = joblib.load(filename='vecto.joblib')

# Fonctions de recommandation

def cluster_product_return(product):
    Y = vectorizer.transform([product])
    prediction = model_search.predict(Y)
    predict_prod = amazon_ratings[amazon_ratings['cluster'] == prediction[0]]['clean_product_name']
    return predict_prod.unique()[:10]

def correleted_product_return(product_id):
    amazon_ratings['rating'] = pd.to_numeric(amazon_ratings['rating'], errors='coerce')
    ratings_utility_matrix = amazon_ratings.pivot_table(values='rating', index='user_id', columns='product_id', fill_value=0)
    X = ratings_utility_matrix.T

    SVD = TruncatedSVD(n_components=10)
    decomposed_matrix = SVD.fit_transform(X)
    correlation_matrix = np.corrcoef(decomposed_matrix)

    product_names = list(X.index)
    product_ID = product_names.index(product_id)
    Recommend = list(X.index[correlation_matrix[product_ID] > 0.90])
    Recommend.remove(product_id)
    return Recommend

# Points d'extrémité de l'API RESTful


def search_recommendation(text):
        traduction = GoogleTranslator(source='auto', target='en').translate(text)
        pred = cluster_product_return(traduction)
        return pred
def related_product_recommendation(product_id):
    if product_id:
        recommendations = correleted_product_return(product_id)
        return recommendations
    else:
        return ''

# Interface utilisateur Streamlit

st.title('Recommandations de Produits 1')
produit=(amazon_ratings[amazon_ratings['product_id'] == 'B002PD61Y4']['product_name']).unique()
st.write(produit)
bt=st.button('Consulter')
if bt:
    st.write('suggestion 1')
    st.write(correleted_product_return('B002PD61Y4'))
    st.write("")

st.title('Recommandations de Produits 2')
text=st.text_input('rechercher un produit')
bt2=st.button('rechercher')
if bt2:
    st.write(search_recommendation(text))