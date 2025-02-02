# views/series.py
import streamlit as st

def app():
    st.header("Página de Búsqueda de Series 📺")

    st.markdown("Aquí podrás buscar series más adelante.")
    
    if st.button("Volver al inicio"):
        st.session_state.page = "home"
