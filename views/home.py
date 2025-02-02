# views/home.py
import streamlit as st

def app():
    st.title("Bienvenido a la Plataforma de Entretenimiento 🎬")

    st.markdown("Elige una de las opciones para comenzar:")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Buscar Series 📺"):
            st.session_state.page = "series"
    with col2:
        if st.button("Buscar Películas 🎥"):
            st.session_state.page = "movies"
