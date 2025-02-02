# pages/home.py
import streamlit as st
from config import PORTADA_URL

def app():
    st.image(PORTADA_URL, use_container_width=True)
    st.markdown("## ¡Bienvenido a la plataforma de películas y series!")
    st.markdown("Selecciona una de las opciones a continuación:")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Buscar Series"):
            st.session_state.page = "series"
    with col2:
        if st.button("Buscar Películas"):
            st.session_state.page = "movies"
