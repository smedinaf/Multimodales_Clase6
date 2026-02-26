import streamlit as st
from PIL import Image

st.title("La mini app de Sofi")
st.header("En esta página Sofi está cocinando su primera app")
st.write("La app se está cocinando")
image = Image.open('conejito.jpg')
st.image(image, caption = "Conejito feliz")


texto = st.text_input('Escribe el nombre de tu animal favorito', 'Mi animal fav')
st.write('El animal favorito del usuario es', texto)
