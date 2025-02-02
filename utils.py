# utils.py
import pandas as pd

def get_image_url(poster_path):
    """Devuelve la URL de la imagen o una imagen de marcador de posición."""
    if pd.notna(poster_path) and poster_path:
        return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return "https://via.placeholder.com/200?text=No+Image"
