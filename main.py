import streamlit as st

import home
import quizz
from subjects import programming

PAGES = {
    "Inicio": home,
    "Test": quizz,
    "Programacion": programming
}

st.sidebar.title('Learnip')
selection = st.sidebar.radio("Ir a...", list(PAGES.keys()))
page = PAGES[selection]
page.app()





