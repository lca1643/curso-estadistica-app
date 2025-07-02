# app.py (Este es el código para tu rama PRINCIPAL/main)

import streamlit as st

# --- 1. Configuración de la Página ---
# Es importante que esta sea la primera instrucción de Streamlit
st.set_page_config(
    page_title="Curso de Estadística con Python",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- 2. Título y Bienvenida ---
st.title("📚 Curso de Fundamentos de Estadística")

st.markdown(
    """
    **Autor:** Luis Corona Alcantar  
    **Correo:** _lcas1643@gmail.com_
    """
)

st.markdown("---")

st.header("¡Bienvenido!")

st.write(
    "Esta es la aplicación web que acompaña al curso de Fundamentos de Estadística. "
    "Aquí encontrarás todas las herramientas interactivas que hemos construido a lo largo de los capítulos."
)

# --- 3. Instrucciones Clave de Uso ---
st.info(
    """
    👈 **Para comenzar, utiliza el menú de navegación en la barra lateral izquierda.**

    Selecciona el capítulo o la herramienta que deseas explorar.
    """
)
    
    ¡Y mucho más!
    """
)

st.success("¡Explora, experimenta y aprende!")
