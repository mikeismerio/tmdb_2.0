# views/details.py
import streamlit as st
from utils import get_image_url

def app():
    if "selected_movie" not in st.session_state or st.session_state.selected_movie is None:
        st.warning("No se ha seleccionado ninguna serie.")
        if st.button("Volver a la lista"):
            st.session_state.page = "home"
            st.experimental_rerun()
        return

    movie = st.session_state.selected_movie  # Recuperar el show seleccionado como diccionario
    base_url = "https://image.tmdb.org/t/p/w500"

    # Mostrar imagen de fondo si se dispone de 'backdrop_path'
    if movie.get('backdrop_path'):
        st.image(base_url + movie['backdrop_path'], use_column_width=True)

    # Diseño en dos columnas: imagen y detalles
    col1, col2 = st.columns([1, 2])
    with col1:
        if movie.get('poster_path'):
            st.image(get_image_url(movie['poster_path']), width=250)
        else:
            st.warning("No hay imagen disponible.")

    with col2:
        year = str(movie['first_air_date'])[:4] if movie.get('first_air_date') else "N/A"
        st.markdown(f"# {movie['name']} ({year})")
        st.markdown(f"**Rating:** {movie['vote_average']:.2f} ⭐ ({movie['vote_count']} votos)")
        st.markdown(f"**Idioma original:** {movie['original_language'].upper() if movie.get('original_language') else 'N/A'}")
        st.markdown(f"**Número de temporadas:** {movie.get('number_of_seasons', 'N/A')}")
        st.markdown(f"**Número de episodios:** {movie.get('number_of_episodes', 'N/A')}")
        st.markdown(f"**Popularidad:** {movie.get('popularity', 'N/A')}")
        st.markdown(f"**Estado:** {movie.get('status', 'N/A')}")
        st.markdown(f"**En producción:** {'Sí' if movie.get('in_production') else 'No'}")
        st.markdown(f"**Géneros:** {movie.get('genres', 'No disponible')}")
        st.markdown(f"**Creador(es):** {movie.get('created_by', 'No disponible')}")
        st.markdown("### Descripción")
        st.markdown(movie.get('overview', "No disponible"))

    st.markdown("---")
    if st.button("Volver a la lista"):
        st.session_state.page = "home"
        st.experimental_rerun()
