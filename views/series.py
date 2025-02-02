# views/series.py
import streamlit as st
import pandas as pd
from config import TABLE_SHOWS
from database import fetch_data
from utils import get_image_url

def app():
    st.header("Buscar Series")
    st.sidebar.header("Filtros de Búsqueda (Series)")
    
    # Obtener los filtros de búsqueda del sidebar o del session_state
    genre_input = st.sidebar.text_input("Género", st.session_state.get("genre_input", ""))
    title_input = st.sidebar.text_input("Título / Nombre Original", st.session_state.get("title_input", ""))
    overview_input = st.sidebar.text_input("Descripción / Sinopsis", st.session_state.get("overview_input", ""))
    search_button = st.sidebar.button("Buscar Series")

    if search_button:
        # Actualizar el session_state con los filtros actuales
        st.session_state.genre_input = genre_input
        st.session_state.title_input = title_input
        st.session_state.overview_input = overview_input

        # Consulta SQL optimizada
        show_query = f"""
            SELECT TOP 10 *
            FROM {TABLE_SHOWS}
            WHERE vote_average IS NOT NULL
            ORDER BY vote_average DESC
        """
        show_data = fetch_data(show_query)

        # Depurar: mostrar las columnas recibidas (para verificar nombres)
        st.write("Columnas recibidas:", show_data.columns.tolist())

        # Aplicar filtros solo si el DataFrame no está vacío
        if not show_data.empty:
            # Si se proporciona un filtro, se genera la serie booleana; si no, se genera una serie de True
            filter_genres = (
                show_data["genres"].str.contains(genre_input, case=False, na=False)
                if genre_input
                else pd.Series([True] * len(show_data), index=show_data.index)
            )
            filter_title = (
                show_data["original_name"].str.contains(title_input, case=False, na=False)
                if title_input
                else pd.Series([True] * len(show_data), index=show_data.index)
            )
            filter_overview = (
                show_data["overview"].str.contains(overview_input, case=False, na=False)
                if overview_input
                else pd.Series([True] * len(show_data), index=show_data.index)
            )

            show_data = show_data[filter_genres & filter_title & filter_overview]

        # Mostrar los resultados
        if not show_data.empty:
            st.subheader("Resultados - Series")
            cols_shows = st.columns(2)
            for i, row in enumerate(show_data.itertuples()):
                with cols_shows[i % 2]:
                    st.image(get_image_url(row.poster_path), width=200)
                    year = str(row.first_air_date)[:4] if pd.notna(row.first_air_date) else "N/A"
                    if st.button(f"{row.original_name} ({year})", key=f"show_{row.Index}"):
                        st.session_state.selected_item = row._asdict()
                        st.session_state.page = "details"
        else:
            st.warning("No se encontraron series para los filtros seleccionados.")

    if st.button("Volver a la Página Principal"):
        st.session_state.page = "home"
