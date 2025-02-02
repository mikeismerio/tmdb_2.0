# views/movies.py
import streamlit as st
import pandas as pd
from config import TABLE_MOVIES
from database import fetch_data
from utils import get_image_url

def app():
    st.header("Buscar Películas")
    st.sidebar.header("Filtros de Búsqueda (Películas)")

    genre_input = st.sidebar.text_input("Género", st.session_state.get("genre_input", ""))
    title_input = st.sidebar.text_input("Título", st.session_state.get("title_input", ""))
    overview_input = st.sidebar.text_input("Descripción / Sinopsis", st.session_state.get("overview_input", ""))
    exclude_adult = st.sidebar.checkbox("Excluir contenido adulto", value=st.session_state.get("exclude_adult", True))
    search_button = st.sidebar.button("Buscar Películas")

    if search_button:
        st.session_state.genre_input = genre_input
        st.session_state.title_input = title_input
        st.session_state.overview_input = overview_input
        st.session_state.exclude_adult = exclude_adult

        # Consulta SQL optimizada
        movie_query = f"""
            SELECT TOP 10 *
            FROM {TABLE_MOVIES}
            WHERE vote_average IS NOT NULL
            ORDER BY vote_average DESC
        """
        movie_data = fetch_data(movie_query)

        if not movie_data.empty:
            movie_data = movie_data[
                (movie_data['genres'].str.contains(genre_input, case=False, na=False) if genre_input else True) &
                (movie_data['title'].str.contains(title_input, case=False, na=False) if title_input else True) &
                (movie_data['overview'].str.contains(overview_input, case=False, na=False) if overview_input else True)
            ]
            if exclude_adult:
                movie_data = movie_data[movie_data['adult'] == 0]

        if not movie_data.empty:
            st.subheader("Resultados - Películas")
            cols_movies = st.columns(2)
            for i, row in enumerate(movie_data.itertuples()):
                with cols_movies[i % 2]:
                    st.image(get_image_url(row.poster_path), width=200)
                    year = str(row.release_date)[:4] if pd.notna(row.release_date) else "N/A"
                    if st.button(f"{row.title} ({year})", key=f"movie_{row.Index}"):
                        st.session_state.selected_item = row._asdict()
                        st.session_state.page = "details"
        else:
            st.warning("No se encontraron películas para los filtros seleccionados.")

    if st.button("Volver a la Página Principal"):
        st.session_state.page = "home"
