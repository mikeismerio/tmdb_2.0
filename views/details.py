# views/details.py
import streamlit as st
from utils import get_image_url

def app():
    # Verificar si existe un elemento seleccionado
    if "selected_item" not in st.session_state or not st.session_state.selected_item:
        st.warning("No se encontró un elemento seleccionado. Regresa y selecciona un elemento.")
        return  # Finaliza la ejecución de la vista si no hay elemento seleccionado

    # Depuración: mostrar el contenido del elemento seleccionado para verificar sus claves
    st.write("Elemento seleccionado:", st.session_state.selected_item)
    
    item = st.session_state.selected_item
    base_url = "https://image.tmdb.org/t/p/w500"

    # Mostrar imagen de fondo si existe (puede que en algunos casos no haya 'backdrop_path')
    if item.get('backdrop_path'):
        st.image(base_url + item['backdrop_path'], use_container_width=True)

    # Mostrar detalles en dos columnas
    col1, col2 = st.columns([1, 2])
    with col1:
        # Se utiliza 'poster_path'; si está vacío, get_image_url devuelve una imagen de marcador
        st.image(get_image_url(item.get('poster_path')), width=250)
    with col2:
        # Para el título, se usa 'title' y, en caso de que no exista, se recurre a 'original_name'
        title = item.get('title', item.get('original_name', 'Desconocido'))
        st.markdown(f"# {title}")
        st.markdown(f"**Rating:** {item.get('vote_average', 'N/A')} ⭐ ({item.get('vote_count', 0)} votos)")
        st.markdown(f"**Géneros:** {item.get('genres', 'No disponible')}")
        st.markdown(f"**Descripción:** {item.get('overview', 'No disponible')}")
        st.markdown(f"**Popularidad:** {item.get('popularity', 'N/A')}")
        st.markdown(f"**Idioma original:** {item.get('original_language', 'N/A').upper()}")

    if st.button("Volver a la Página Principal"):
        st.session_state.page = "home"
