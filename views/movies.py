# views/movies.py
import streamlit as st
from config import table
from database import fetch_data
from utils import get_image_url

def filter_top_movies(df, genre):
    """Filtra y ordena las 10 mejores películas según el género."""
    if genre:
        filtered_movies = df[df['genres'].str.contains(genre, case=False, na=False)]
        top_movies = filtered_movies.sort_values(by='vote_average', ascending=False).head(10)
        if not top_movies.empty:
            base_url = "https://image.tmdb.org/t/p/w500"
            top_movies = top_movies.copy()
            top_movies['image_url'] = base_url + top_movies['poster_path']
            return top_movies[top_movies['image_url'].notna()]
    return pd.DataFrame()

def app():
    st.header("Buscar Películas 🎥")
    st.sidebar.header("Filtros de Búsqueda (Películas)")

    genre_input = st.sidebar.text_input("Introduce el Género:")

    # Consulta los datos de la tabla
    query = f"SELECT * FROM {table}"
    df = fetch_data(query)

    if genre_input:
        top_movies = filter_top_movies(df, genre_input)
        
        if not top_movies.empty:
            cols_per_row = 5
            cols = st.columns(cols_per_row)
            
            # Mostrar cada película en una columna
            for index, row in enumerate(top_movies.itertuples()):
                with cols[index % cols_per_row]:
                    st.image(row.image_url, use_container_width=True)
                    release_year = str(row.release_date)[:4] if row.release_date else "N/A"
                    button_label = f"{row.title} ({release_year})"

                    # Generar una clave única para el botón
                    button_key = f"btn_{row.Index}_{row.id}"

                    if st.button(button_label, key=button_key):
                        st.session_state.selected_movie = row._asdict()  # Convertir en diccionario
                        st.session_state.page = "details"
                        return  # Volver al flujo principal
        else:
            st.warning("No se encontraron resultados para el género ingresado.")
    else:
        st.info("Introduce un género para buscar las Top 10 Películas.")
    
    if st.button("Volver al inicio"):
        st.session_state.page = "home"
