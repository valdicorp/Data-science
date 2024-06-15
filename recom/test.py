import streamlit as st
from pages import home, product

st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à", ("Catalogue de Produits", "Description du Produit"))

# Définir la logique de navigation
if "selected_product" not in st.session_state:
    st.session_state.selected_product = None

if page == "Catalogue de Produits":
    home.home()
elif page == "Description du Produit":
    product.product()
