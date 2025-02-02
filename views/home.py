# views/home.py
import streamlit as st
from config import table
from database import fetch_data
from utils import get_image_url

def filter_top_shows(df, genre):
    """Filtra y ordena los 10 mejores shows según el género."""
    if genre:
        filtered_shows = df[df['genres'].str.contains(genre, case=False, na=False)]
        top_shows = filtered_shows.sort_values(by='vote_average', ascending=False).head(10)
        if not top_shows.empty:
            base_url = "https://image.tmdb.org/t/p/w500"
            top_shows = top_shows.copy()  # Evitar advertencias de pandas
            top_shows['image_url'] = base_url + top_shows['poster_path']
            return top_shows[top_shows['image_url'].notna()]
    return pd.DataFrame()

def app():
    st.title("Top Shows")
    
    # Consulta los datos de la tabla
    query = f"SELECT * FROM {table}"
    df = fetch_data(query)

    # Input para el género
    genre_input = st.text_input("Introduce el Género:")

    if genre_input:
        top_shows = filter_top_shows(df, genre_input)

        if not top_shows.empty:
            cols_per_row = 5
            cols = st.columns(cols_per_row)

            # Mostrar cada show en una columna
            for index, row in enumerate(top_shows.itertuples()):
                with cols[index % cols_per_row]:
                    st.image(row.image_url, use_container_width=True)
                    first_air_year = str(row.first_air_date)[:4] if row.first_air_date else "N/A"
                    button_label = f"{row.name} ({first_air_year})"

                    # Generar una clave única para el botón
                    button_key = f"btn_{row.Index}_{row.id}"

                    if st.button(button_label, key=button_key):
                        # Guardar la serie seleccionada en session_state y navegar a detalles
                        st.session_state.selected_movie = row._asdict()  # Convertir en diccionario
                        st.session_state.page = "details"
                        st.experimental_rerun()  # Forzar navegación
        else:
            st.warning("No se encontraron resultados para el género ingresado.")
    else:
        st.info("Introduce un género para buscar los Top 10 Shows.")
