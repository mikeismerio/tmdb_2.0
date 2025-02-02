import streamlit as st
from multiapp import MultiApp
from views import home, series, movies

# Crear la instancia MultiApp
app = MultiApp()

# Agregar las aplicaciones
app.add_app("Página de Inicio", home.app)
app.add_app("Buscar Series 📺", series.app)
app.add_app("Buscar Películas 🎥", movies.app)

# Ejecutar la aplicación
app.run()
