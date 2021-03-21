import streamlit as st

def app():
    st.write("""
    # Que area y metodo de aprendizaje es para ti?
    ### Realiza este test y descubrelo!  
      
    """)


    games_type = st.selectbox(
        'Con que tipo de juegos de diviertes mas?',
        ('Construccion', 'Rompecabezas',
        'Videojuegos', 'Juegos de mesa',
        'Juegos de rol', 'No me gusta jugar')
    )

    like_reading = st.selectbox(
        'Te gusta leer?',
        ('Si', 'No')
    )

    like_movies = st.selectbox(
        'Te gusta ver series, peliculas, anime, etc?',
        ('Si', 'No')
    )

    like_puzzles = st.selectbox(
        'Te gusta armar rompecabezas?',
        ('Si', 'No')
    )

    like_problems_solving = st.selectbox(
        'Si tienes algun problema, prefieres resolverlo tu o pedir ayuda?',
        ('Prefiero resolverlo yo', 'Prefiero pedir ayuda')
    )

    fav_subject = st.selectbox(
        'Que materia del colegio te parece mas interesante? Cual te gusta mas?',
        ('Biologia', 'Lenguaje', 'Matematicas')
    )

    no_fav_subject = st.selectbox(
        'Que materia del colegio no te gusta?',
        ('Biologia', 'Lenguaje', 'Matematicas')
    )
