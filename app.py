import streamlit as st
import requests
from PIL import Image
import base64

# Configuración general
st.set_page_config(
    page_title="IntiBot - Aprende Quechua",
    page_icon="🦙",
    layout="centered",
)

# Encabezado con imagen y título
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Llama_lying_down.jpg/320px-Llama_lying_down.jpg", width=70)
with col2:
    st.title("IntiBot: Tu compañero de quechua 🦙")

st.markdown("""
IntiBot es un asistente conversacional entrenado para ayudarte a aprender quechua boliviano.
Puedes hacerle preguntas, pedir traducciones o simplemente conversar.

*Ejemplo: "Hola, ¿puedes traducir 'Buenos días, mi nombre es Carla'?*"
""")

# Entrada del usuario
st.subheader("📝 Escribe tu mensaje")
user_input = st.text_input("", placeholder="Escribe aquí tu pregunta o saludo...")

# Enviar a n8n webhook
n8n_webhook_url = "http://localhost:5678/webhook-test/fedb82e6-11f2-4749-9e3b-99e8051e7ae6"

if st.button("Enviar a IntiBot") and user_input:
    with st.spinner("IntiBot está pensando en quechua..."):
        try:
            response = requests.post(n8n_webhook_url, json={"mensaje": user_input})
            if response.ok:
                result = response.json()
                reply = result.get("message") or "(Respuesta recibida pero vacía)"
                st.success("🌟 IntiBot responde:")
                st.markdown(f"> {reply}")
            else:
                st.error("❌ Error: IntiBot no pudo responder. Intenta de nuevo más tarde.")
        except Exception as e:
            st.error(f"Error de conexión: {str(e)}")

# Footer con link
st.markdown("""
---
Desarrollado con 🚀 por [Carli Code](https://carlicode.com)
""")
