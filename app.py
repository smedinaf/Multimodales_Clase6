import streamlit as st
from PIL import Image

st.title("La mini app de Sofi")
st.header("En esta página Sofi está cocinando su primera app")
st.write("La app se está cocinando")
image = Image.open('conejito.jpg')
st.image(Image, caption = "Conejito feliz")
