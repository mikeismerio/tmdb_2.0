# main.py
import streamlit as st

# Configurar la página
st.set_page_config(page_title="Inicio", page_icon="🏠", layout="wide")

# Inicializar el estado de la sesión (si no existen)
if "page" not in st.session_state:
    st.session_state.page = "home"
if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None
if "search_genre" not in st.session_state:
    st.session_state.search_genre = ""

# Importar las vistas desde la carpeta 'views'
from views import home, details

# Enrutamiento manual según el valor de st.session_state.page
if st.session_state.page == "home":
    home.app()
elif st.session_state.page == "details":
    details.app()
