import streamlit as st

# Configurar la página
st.set_page_config(page_title="Navegación Básica", page_icon="🎬", layout="wide")

# Inicializar el estado de la sesión para navegación
if "page" not in st.session_state:
    st.session_state.page = "home"

# Importar las vistas
from views import home, series, movies

# Enrutamiento entre páginas
if st.session_state.page == "home":
    home.app()
elif st.session_state.page == "series":
    series.app()
elif st.session_state.page == "movies":
    movies.app()
