import streamlit as st

# Inyectar CSS para ocultar el menú de navegación multipágina en la sidebar
hide_sidebar_nav_style = """
    <style>
    [data-testid="stSidebarNav"] { 
        display: none; 
    }
    </style>
"""
st.markdown(hide_sidebar_nav_style, unsafe_allow_html=True)

# Configurar la página
st.set_page_config(page_title="Inicio", page_icon="🏠", layout="wide")

# Inicializar el estado de la sesión si aún no existe
if "page" not in st.session_state:
    st.session_state.page = "home"

# Importar las páginas (estos módulos se encuentran en la carpeta 'pages')
from pages import home, series, movies, details

# Enrutamiento manual entre páginas según el valor en st.session_state.page
if st.session_state.page == "home":
    home.app()
elif st.session_state.page == "series":
    series.app()
elif st.session_state.page == "movies":
    movies.app()
elif st.session_state.page == "details":
    details.app()
