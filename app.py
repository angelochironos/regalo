import streamlit as st
import datetime
from dateutil.relativedelta import relativedelta

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Para Mi Novia", page_icon="🌹", layout="centered")

# --- CONFIGURACIÓN DE TU RELACIÓN ---
FECHA_INICIO = datetime.date(2025, 1, 14)  # 👈 CAMBIA ESTO por el año, mes y día en que empezaron

# --- CÁLCULOS DEL TIEMPO ---
hoy = datetime.date.today()
diferencia = relativedelta(hoy, FECHA_INICIO)
meses_totales = diferencia.years * 12 + diferencia.months

# Determinar el tamaño de la flor (crece el 14 de cada mes)
# Empezamos en un tamaño base y crece un 15% por cada mes cumplido
tamano_flor = 100 + (meses_totales * 15) 

# Mensaje especial si hoy es día 14
es_aniversario = (hoy.day == 14)

# --- DISEÑO DE LA PÁGINA ---
st.title("💖 Para la mujer de mi vida 💖")

# Contador
st.subheader("Nuestro contador de amor:")
st.metric(label="Meses Juntos", value=f"{meses_totales} meses")
st.write(f"Desde el {FECHA_INICIO.strftime('%d/%m/%Y')} cada día 14 nuestra flor crece más.")

# Animación/Gráfico de la Flor (Usamos emojis gigantes y CSS para el tamaño)
st.write("---")
if es_aniversario:
    st.balloons() # Lluvia de globos si es el día 14
    st.success("🎉 ¡Feliz día 14 mi amor! Hoy la flor ha florecido más 🎉")

# Mostrar la flor con el tamaño dinámico calculado
st.markdown(
    f"""
    <div style="text-align: center;">
        <span style="font-size: {tamano_flor}px; transition: all 1s ease-in-out;">🌹</span>
    </div>
    """, 
    unsafe_html=True
)

st.write("---")
st.write("Te amo cada día más. Gracias por estar a mi lado. 💕")