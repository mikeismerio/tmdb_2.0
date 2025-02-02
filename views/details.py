# views/details.py
import streamlit as st
from utils import get_image_url

def app():
    if st.session_state.get("selected_item"):
        item = st.session_state.selected_item
        base_url = "https://image.tmdb.org/t/p/w500"

        # Mostrar imagen de fondo si existe
        if item.get('backdrop_path'):
            st.image(base_url + item['backdrop_path'], use_container_width=True)

        # Mostrar detalles en dos columnas
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(get_image_url(item.get('poster_path')), width=250)
        with col2:
            title = item.get('title', item.get('original_name', 'Desconocido'))
            st.markdown(f"# {title}")
            st.markdown(f"**Rating:** {item.get('vote_average', 'N/A')} ⭐ ({item.get('vote_count', 0)} votos)")
            st.markdown(f"**Géneros:** {item.get('genres', 'No disponible')}")
            st.markdown(f"**Descripción:** {item.get('overview', 'No disponible')}")
            st.markdown(f"**Popularidad:** {item.get('popularity', 'N/A')}")
            st.markdown(f"**Idioma original:** {item.get('original_language', 'N/A').upper()}")

    if st.button("Volver a la Página Principal"):
        st.session_state.page = "home"
