# main.py
import streamlit as st
from pages import home, series, movies, details

# Configurar la página (por ejemplo, en modo Wide)
st.set_page_config(page_title="Inicio", page_icon="🏠", layout="wide")

# Inicializar el estado de la sesión si aún no está definido
if "page" not in st.session_state:
    st.session_state.page = "home"

# Enrutamiento entre páginas
if st.session_state.page == "home":
    home.app()
elif st.session_state.page == "series":
    series.app()
elif st.session_state.page == "movies":
    movies.app()
elif st.session_state.page == "details":
    details.app()
