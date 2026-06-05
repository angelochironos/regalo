import streamlit as st
import datetime
import time

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Para Mi Novia", page_icon="🌸", layout="centered")

# Ocultar menús nativos de Streamlit para una experiencia limpia en celular
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    body { background-color: #0a0a0f !important; color: white; }
    .stApp { background-color: #0a0a0f !important; }
    </style>
    """, 
    unsafe_allow_html=True
)

# --- CONFIGURACIÓN DE TU RELACIÓN ---
# ⚠️ CAMBIA ESTO por el año, mes, día, hora, minuto exactos en que empezaron
FECHA_INICIO = datetime.datetime(2025, 1, 14, 0, 0, 0)  

# --- LÓGICA DEL TIEMPO ---
ahora = datetime.datetime.now()
diferencia = ahora - FECHA_INICIO

# Desglose estricto del tiempo transcurrido para tu contador
dias = diferencia.days
horas, residuo = divmod(diferencia.seconds, 3600)
minutos, segundos = divmod(residuo, 60)

# Calcular crecimiento dinámico según los días transcurridos
tamano_base_pc = 180
tamano_base_movil = 110
crecimiento = (dias // 30) * 15  # Crece 15px por cada mes cumplido

tamano_final_pc = tamano_base_pc + crecimiento
tamano_final_movil = tamano_base_movil + crecimiento

# --- DISEÑO DE LA INTERFAZ (HTML + CSS ENMASCARADO EN PYTHON) ---
st.markdown(
    f"""
    <div style="text-align: center; padding: 20px; font-family: 'Courier New', Courier, monospace; min-height: 80vh; display: flex; flex-direction: column; justify-content: center; align-items: center;">
        
        <!-- CONTADOR ESTILO FUENTE MONOSPACE GIGANTE -->
        <div style="font-size: 3.5rem; font-weight: bold; color: #ffffff; letter-spacing: 2px; margin-bottom: 40px; text-shadow: 0px 0px 15px rgba(255,255,255,0.3);">
            {dias:02d}:{horas:02d}:{minutos:02d}:{segundos:02d}
        </div>

        <!-- ESPACIO DE LA FLOR RESPONSIVA -->
        <div style="margin: 30px 0; position: relative;">
            <style>
                @keyframes pulse {{
                    0% {{ transform: scale(1); filter: drop-shadow(0 0 10px rgba(255, 105, 180, 0.6)); }}
                    50% {{ transform: scale(1.05); filter: drop-shadow(0 0 25px rgba(255, 105, 180, 0.9)); }}
                    100% {{ transform: scale(1); filter: drop-shadow(0 0 10px rgba(255, 105, 180, 0.6)); }}
                }}
                
                .cerezo-digital {{
                    font-size: {tamano_final_pc}px;
                    display: inline-block;
                    animation: pulse 2s infinite ease-in-out;
                }}

                @media (max-width: 768px) {{
                    .cerezo-digital {{
                        font-size: {tamano_final_movil}px;
                    }}
                }}
            </style>
            <span class="cerezo-digital">🌸</span>
        </div>

        <!-- MENSAJE DE AMOR -->
        <div style="color: #ffb7c5; font-size: 1.1rem; max-width: 80%; margin-top: 30px; line-height: 1.6;">
            Cada segundo que pasa, nuestra historia se vuelve más grande. <br>
            Nuestra flor seguirá creciendo el día 14 de cada mes.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Activar globos automáticos si hoy es día 14
if ahora.day == 14:
    st.balloons()

# Recarga la página automáticamente cada 5 segundos para actualizar los números
time.sleep(5)
st.rerun()
