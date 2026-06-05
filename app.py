import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Para Mi Novia", page_icon="🌹", layout="centered")

# --- CONFIGURACIÓN DE TU RELACIÓN ---
# ⚠️ CAMBIA ESTO por el año, mes y día exactos en que empezaron
FECHA_INICIO = datetime.date(2025, 1, 14)  

# --- CÁLCULOS DEL TIEMPO ---
hoy = datetime.date.today()

# Calculamos la diferencia exacta en meses y días
diferencia = relativedelta(hoy, FECHA_INICIO)
meses_totales = (diferencia.years * 12) + diferencia.months

# Determinar el tamaño de la flor (Crece un 15% por cada mes cumplido)
tamano_flor = 100 + (meses_totales * 15) 

# Determinar si hoy es día 14
es_aniversario = (hoy.day == 6)

# --- DISEÑO DE LA PÁGINA ---
st.title("💖 Para la mujer de mi vida 💖")

# Sección del contador
st.subheader("Nuestro contador de amor:")
st.metric(label="Meses Juntos", value=f"{meses_totales} meses")
st.write(f"Desde el {FECHA_INICIO.strftime('%d/%m/%Y')}, cada día 14 nuestra flor crece más.")

st.write("---")

# Efectos especiales si hoy es el día especial
if es_aniversario:
    st.balloons()  # Lluvia de globos en la pantalla
    st.success("🎉 ¡Feliz día 14 mi amor! Hoy nuestra flor ha florecido más 🎉")

# Mostrar la flor con el tamaño dinámico corregido
st.markdown(
    f"""
    <div style="text-align: center; margin: 20px 0;">
        <span style="font-size: {tamano_flor}px; transition: all 1s ease-in-out; display: inline-block;">🌹</span>
    </div>
    """, 
    unsafe_allow_html=True  # 👈 Corrección aplicada aquí
)

st.write("---")
st.write("Te amo cada día más. Gracias por estar a mi lado. 💕")
