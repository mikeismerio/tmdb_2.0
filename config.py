# config.py
import os

# =================== Configuración de Base de Datos ===================
server = "nwn7f7ze6vtuxen5age454nhca-colrz4odas5unhn7cagatohexq.datawarehouse.fabric.microsoft.com"
database = "TMDB"
driver = "ODBC Driver 17 for SQL Server"
table = "tmdb_shows_clean"  # Tabla a consultar

# Obtener credenciales desde variables de entorno (o Streamlit Secrets)
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASS")

# Cadena de conexión
CONNECTION_STRING = (
    f"mssql+pyodbc://{USER}:{PASSWORD}@{server}/{database}?"
    f"driver={driver}&Authentication=ActiveDirectoryPassword"
)
