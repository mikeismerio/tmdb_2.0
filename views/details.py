# views/details.py
import streamlit as st
from utils import get_image_url

def app():
    # Verificar que se haya seleccionado un show
    if "selected_movie" not in st.session_state or st.session_state.selected_movie is None:
        st.warning("No se ha seleccionado ninguna serie.")
        if st.button("Volver a la lista"):
            st.session_state.page = "home"
            st.experimental_rerun()
        return

    movie = st.session_state.selected_movie
    base_url = "https://image.tmdb.org/t/p/w500"

    # Mostrar imagen de fondo si se dispone de 'backdrop_path'
    if hasattr(movie, 'backdrop_path') and movie.backdrop_path:
        st.image(base_url + movie.backdrop_path, use_column_width=True)

    # Diseño en dos columnas: imagen y detalles
    col1, col2 = st.columns([1, 2])
    with col1:
        if hasattr(movie, 'poster_path') and movie.poster_path:
            st.image(base_url + movie.poster_path, width=250)
        else:
            st.warning("No hay imagen disponible.")
    with col2:
        if hasattr(movie, 'first_air_date') and movie.first_air_date:
            year = str(movie.first_air_date)[:4]
        else:
            year = "N/A"
        st.markdown(f"# {movie.name} ({year})")
        st.markdown(f"**Rating:** {movie.vote_average:.2f} ⭐ ({movie.vote_count} votos)")
        st.markdown(f"**Idioma original:** {movie.original_language.upper() if hasattr(movie, 'original_language') and movie.original_language else 'N/A'}")
        st.markdown(f"**Número de temporadas:** {movie.number_of_seasons if hasattr(movie, 'number_of_seasons') else 'N/A'}")
        st.markdown(f"**Número de episodios:** {movie.number_of_episodes if hasattr(movie, 'number_of_episodes') else 'N/A'}")
        st.markdown(f"**Popularidad:** {movie.popularity if hasattr(movie, 'popularity') else 'N/A'}")
        st.markdown(f"**Estado:** {movie.status if hasattr(movie, 'status') else 'N/A'}")
        st.markdown(f"**En producción:** {'Sí' if hasattr(movie, 'in_production') and movie.in_production else 'No'}")
        st.markdown(f"**Géneros:** {movie.genres if hasattr(movie, 'genres') else 'No disponible'}")
        st.markdown(f"**Creador(es):** {movie.created_by if hasattr(movie, 'created_by') else 'No disponible'}")
        st.markdown("### Descripción")
        st.markdown(movie.overview if hasattr(movie, 'overview') and movie.overview else "No disponible")

    st.markdown("---")
    if st.button("Volver a la lista"):
        st.session_state.page = "home"
        st.experimental_rerun()
