# config.py
import os

# URL de la imagen de portada
PORTADA_URL = "https://raw.githubusercontent.com/mikeismerio/tmdb_shows/main/home.jpg"

# =================== Configuración de Base de Datos ===================
SERVER = "nwn7f7ze6vtuxen5age454nhca-colrz4odas5unhn7cagatohexq.datawarehouse.fabric.microsoft.com"
DATABASE = "TMDB"
DRIVER = "ODBC Driver 17 for SQL Server"
TABLE_SHOWS = "tmdb_shows_clean"
TABLE_MOVIES = "tmdb_movies_clean"

# Credenciales (se asumen almacenadas en variables de entorno o en Streamlit Secrets)
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASS")

# Cadena de conexión
CONNECTION_STRING = (
    f"mssql+pyodbc://{USER}:{PASSWORD}@{SERVER}/{DATABASE}?"
    f"driver={DRIVER}&Authentication=ActiveDirectoryPassword"
)
