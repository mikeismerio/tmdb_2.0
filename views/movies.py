# views/movies.py
import streamlit as st

def app():
    st.header("Página de Búsqueda de Películas 🎥")

    st.markdown("Aquí podrás buscar películas más adelante.")
    
    if st.button("Volver al inicio"):
        st.session_state.page = "home"
