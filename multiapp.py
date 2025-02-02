import streamlit as st

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Registra una nueva aplicación."""
        self.apps.append({"title": title, "function": func})

    def run(self):
        # Crear un menú desplegable en la barra lateral
        app = st.sidebar.selectbox(
            'Navegar a:',
            self.apps,
            format_func=lambda app: app['title']
        )

        # Ejecutar la función de la aplicación seleccionada
        app['function']()
