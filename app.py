import streamlit as st
import datetime
import time

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Nuestro Contador", page_icon="🌸", layout="centered")

# Ocultar menús nativos de Streamlit para que parezca una app móvil limpia
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    body { background-color: #0a0a0f; color: white; }
    stApp { background-color: #0a0a0f; }
    </style>
    """, 
    unsafe_allow_html=True
)

# --- CONFIGURACIÓN DE TU RELACIÓN ---
# Coloca aquí la fecha exacta en la que iniciaron
FECHA_INICIO = datetime.datetime(2025, 1, 14, 0, 0, 0)  

# --- LÓGICA DEL TIEMPO ---
ahora = datetime.datetime.now()
diferencia = ahora - FECHA_INICIO

# Desglose estricto del tiempo transcurrido
dias = diferencia.days
horas, residuo = divmod(diferencia.seconds, 3600)
minutos, segundos = divmod(residuo, 60)

# Calcular meses totales para el crecimiento de la flor
meses_totales = dias // 30  
tamano_flor = 120 + (meses_totales * 20)  # Crece dinámicamente cada mes

# --- DISEÑO DE LA INTERFAZ ESTILO PYGAME ---
st.markdown(
    f"""
    <div style="background-color: #0a0a0f; text-align: center; padding: 20px; font-family: 'Courier New', Courier, monospace; min-height: 90vh; display: flex; flex-direction: column; justify-content: center; align-items: center;">
        
        <!-- CONTADOR ESTILO FUENTE MONOSPACE GIGANTE -->
        <div style="font-size: 3.5rem; font-weight: bold; color: #ffffff; letter-spacing: 2px; margin-bottom: 40px; text-shadow: 0px 0px 15px rgba(255,255,255,0.3);">
            {dias:02d}:{horas:02d}:{minutos:02d}:{segundos:02d}
        </div>

        <!-- ESPACIO DE LA FLOR / ÁRBOL INTERACTIVO -->
        <div style="margin: 40px 0; position: relative;">
            <style>
                @keyframes pulse {{
                    0% {{ transform: scale(1); filter: drop-shadow(0 0 10px rgba(255, 105, 180, 0.6)); }}
                    50% {{ transform: scale(1.08); filter: drop-shadow(0 0 25px rgba(255, 105, 180, 0.9)); }}
                    100% {{ transform: scale(1); filter: drop-shadow(0 0 10px rgba(255, 105, 180, 0.6)); }}
                }}
                .cerezo-digital {{
                    font-size: {tamano_flor}px;
                    display: inline-block;
                    animation: pulse 2s infinite ease-in-out;
                    cursor: pointer;
                }}
            </style>
            <!-- Usamos el emoji tradicional de Cerezo en Flor que renderiza hermoso en iOS y Android -->
            <span class="cerezo-digital">🌸</span>
        </div>

        <!-- MENSAJE DE AMOR CON LOS COLORES DE TU PALETA -->
        <div style="color: #ffb7c5; font-size: 1.1rem; max-width: 80%; margin-top: 30px; line-height: 1.6;">
            Cada segundo que pasa, nuestra historia se vuelve más grande. 
            Nuestra flor seguirá creciendo en el día 14 de cada mes.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Activar globos interactivos si hoy es día 14
if ahora.day == 14:
    st.balloons()

# Forzar una recarga en la web cada 10 segundos para actualizar el contador automáticamente
time.sleep(10)
st.rerun()

<!-- ESPACIO DE LA FLOR / ÁRBOL INTERACTIVO RESPONSIVO -->
<div style="margin: 20px 0; position: relative;">
    <style>
        @keyframes pulse {
            0% { transform: scale(1); filter: drop-shadow(0 0 10px rgba(255, 105, 180, 0.6)); }
            50% { transform: scale(1.05); filter: drop-shadow(0 0 25px rgba(255, 105, 180, 0.9)); }
            100% { transform: scale(1); filter: drop-shadow(0 0 10px rgba(255, 105, 180, 0.6)); }
        }
        
        /* Tamaño para pantallas grandes de computadora */
        .cerezo-digital {
            font-size: 180px; 
            display: inline-block;
            animation: pulse 2s infinite ease-in-out;
            cursor: pointer;
        }

        /* 📱 Tamaño adaptado automáticamente para celulares */
        @media (max-width: 768px) {
            .cerezo-digital {
                font-size: 110px; /* Evita que se salga de la pantalla del móvil */
            }
        }
    </style>
    <span class="cerezo-digital">🌸</span>
</div>
