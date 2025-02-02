# main.py
import streamlit as st

# Configurar la página
st.set_page_config(page_title="Inicio", page_icon="🏠", layout="wide")

# Inicializar el estado de la sesión para navegación
if "page" not in st.session_state:
    st.session_state.page = "home"
if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

# Importar las vistas
from views import home, details

# Enrutamiento según el valor en st.session_state.page
if st.session_state.page == "home":
    home.app()
elif st.session_state.page == "details":
    details.app()
