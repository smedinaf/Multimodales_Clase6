import streamlit as st
from PIL import Image

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="La mini app de Sofi 🐰", page_icon="🎀")

# --- ESTILO CSS CUSTOM ---
st.markdown("""
    <style>
    /* Fondo y fuentes */
    .stApp {
        background-color: #FFF9FB; /* Rosa blanquecino */
    }
    h1 {
        color: #FF85A1 !important;
        font-family: 'Georgia', serif;
        text-align: center;
        text-shadow: 2px 2px #FFD1DC;
    }
    h2, h3 {
        color: #D4A5A5 !important;
    }
    /* Estilo para los botones y checkboxes */
    .stButton>button {
        background-color: #FFB6C1;
        color: white;
        border-radius: 20px;
        border: none;
        width: 100%;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #FF85A1;
        color: white;
    }
    /* Estilo para los inputs */
    .stTextInput>div>div>input {
        border-radius: 15px;
        border: 2px solid #FFD1DC !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎀 La mini app de Sofi ✨")

st.markdown("<h4 style='text-align: center; color: #BDB76B;'>☁️ En esta página Sofi está cocinando su primera app ☁️</h4>", unsafe_allow_html=True)

# Contenedor para la imagen principal
st.write("---")
col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
with col_img2:
    try:
        image = Image.open('conejito.jpg')
        st.image(image, caption="🐰 Conejito feliz disfrutando el día", use_container_width=True)
    except:
        st.image("https://cdn-icons-png.flaticon.com/512/2663/2663067.png", caption="✨ (Aquí va tu conejito)")

st.write("---")

# Input de animal favorito
texto = st.text_input('✨ Escribe el nombre de tu animal favorito:', 'Mi animal fav')
st.markdown(f"<p style='color: #FF85A1;'>💖 El animal favorito del usuario es: <b>{texto}</b></p>", unsafe_allow_html=True)

st.subheader("🌷 Probemos con 2 columnas")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🥕 ¿Cuánto sabes sobre los conejos?")
    st.write("¿Los conejos comen zanahoria?")
    resp = st.checkbox('✨ ¡Sí, les encantan!')
    if resp:
        st.success('¡Correcto! Eres una experta 🎀')

with col2:
    st.markdown("### 🏠 Sobre preferencia")
    modo = st.radio(
        "¿Cuál es la mejor forma de tener un conejo?",
        ("En casa", "En una finca", "Al aire libre")
    )

    if modo:
        st.info(f"📍 {modo} es la mejor forma de que viva un conejo.")

st.write("---")

# Sección del botón
st.subheader("🐰 ¿Tienes conejos?")
if st.button('Selecciona el botón si amas a los peluditos'):
    st.balloons()
    st.write('✨ ¡Gracias por presionar, eres genial! ✨')
else:
    st.caption('Todavía no has presionado el botón... 🌸')

st.write("---")

# Selector de nombre
st.subheader("🏷️ Elige el nombre de tu peludito")
in_mod = st.selectbox(
    "Selecciona el color de tu conejo",
    ("Cafe", "Blanco", "Gris"),
)

set_mod = ""
if in_mod == "Cafe":
    set_mod = "Canela 🍂"
elif in_mod == "Blanco":
    set_mod = "Algodón ☁️"
elif in_mod == "Gris":
    set_mod = "Motita 🌪️"

st.markdown(f"""
    <div style='background-color: white; padding: 20px; border-radius: 20px; border: 2px dashed #FFB6C1; text-align: center;'>
        <p style='font-size: 20px; color: #FF85A1;'>👑 Tu conejo se llamará: <b>{set_mod}</b></p>
    </div>
""", unsafe_allow_html=True)

# Sidebar Coquette
with st.sidebar:
    st.markdown("<h2 style='color: #FF85A1;'>🎀 Menú de Sofi</h2>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/3069/3069172.png", width=100)
    st.subheader("Elige tu modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad que deseas usar",
        ("Visual 🎨", "Auditiva 🎧", "Háptica ⚡")
    )
    st.write("---")
    st.caption("Hecho con mucho ✨ por Sofi")

st.markdown("<br><center><p style='color: #D4A5A5; font-size: 12px;'>🐰 App en construcción... ¡quedando divina!</p></center>", unsafe_allow_html=True)
