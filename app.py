import streamlit as st
from PIL import Image

st.title("La mini app de Sofi")
st.header("En esta página Sofi está cocinando su primera app")
st.write("La app se está cocinando")
image = Image.open('conejito.jpg')
st.image(image, caption = "Conejito feliz")


texto = st.text_input('Escribe el nombre de tu animal favorito', 'Mi animal fav')
st.write('El animal favorito del usuario es', texto)

st.subheader("Probemos con 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("¿Cuánto sabes sobre los conejos?")
  st.write("Los conejos comen zanahoria")
  resp = st.checkbox('De acuerdo')
  if resp:
    st.write('Correcto!')

with col2:
  st.subheader("Sobre preferencia")
  modo = st.radio("¿Cuál es la mejor forma de tener un conejo?",("En casa", "En una finca", "Al aire libre"))

  if modo == "En casa":
        st.write("En casa es la mejor forma de que viva un conejo")

  elif modo == "En una finca":
        st.write("En una finca es la mejor forma de que viva un conejo")

  elif modo == "Al aire libre":
        st.write("Al aire libre es la mejor forma de que viva un conejo")


st.subheader("¿Tienes conejos?")
if st.button('Selecciona el botón'):
    st.write('Gracias por presionar')
else:
    st.write('No has presionado aún')

st.subheader("Selectbox")
in_mod = st.selectbox(
    "Selecciona el color de tu conejo",
    ("Cafe", "Blanco", "Gris"),
)
if in_mod == "Cafe":
    set_mod = "Tu conejo se llamará Canela"
elif in_mod == "Blanco":
    set_mod = "Tu conejo se llamará Algodón"
elif in_mod == "Gris":
    set_mod = "Tu conejo se llamará Motita"
st.write(" La acción es:" , set_mod)


with st.sidebar:
    st.subheader("Configura la modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva","Háptica")
    )
