import pygame
import random
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de pantalla (Pantalla completa o ventana gigante)
INFO = pygame.display.Info()
ANCHO, ALTO = INFO.current_w, INFO.current_h
pantalla = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)
pygame.display.set_caption("Contador Cerezo Gigante")

# Paleta de Colores
NEGRO = (10, 10, 15)
BLANCO = (255, 255, 255)
MARRON_TRONCO = (54, 38, 27)
ROSA_HOJA = (255, 183, 197)
ROSA_FOSFORO = (255, 105, 180)

# Configuración de Reloj e Historial de Tiempo
reloj = pygame.time.Clock()
tiempo_inicial = pygame.time.get_ticks()
ultimo_segundo_registrado = 0

# Variables del Árbol y las Hojas
hojas = []
ramas_posiciones = []

def generar_estructura_arbol(x, y, angulo, longitud, grosor):
    """Genera recursivamente los puntos finales de las ramas para brotar hojas."""
    if longitud < 15:
        ramas_posiciones.append((x, y))
        return
    
    # Calcular destino de la rama
    import math
    x_destino = x + int(math.cos(math.radians(angulo)) * longitud)
    y_destino = y - int(math.sin(math.radians(angulo)) * longitud)
    
    # Guardar puntos para dibujar el tronco estático después
    ramas_posiciones.append(((x, y), (x_destino, y_destino), grosor))
    
    # Ramificaciones intermitentes
    nuevo_grosor = max(1, int(grosor * 0.7))
    generar_estructura_arbol(x_destino, y_destino, angulo - random.randint(15, 30), longitud * 0.75, nuevo_grosor)
    generar_estructura_arbol(x_destino, y_destino, angulo + random.randint(15, 30), longitud * 0.75, nuevo_grosor)

# Construir el esqueleto inicial del cerezo gigante
# Base en el centro inferior, longitud inicial de rama de 220 píxeles
generar_estructura_arbol(ANCHO // 2, ALTO - 100, 90, 220, 22)

# Filtrar solo extremos para brotes de hojas iniciales
puntos_brote = [pos for pos in ramas_posiciones if isinstance(pos, tuple) and not isinstance(pos[0], tuple)]
lineas_tronco = [linea for linea in ramas_posiciones if isinstance(linea, tuple) and isinstance(linea[0], tuple)]

def agregar_hojas():
    """Añade un lote de hojas nuevas esparcidas cerca de las copas de las ramas."""
    for _ in range(35):  # Cantidad de hojas nuevas por cada segundo cumplido
        origen = random.choice(puntos_brote)
        offset_x = random.randint(-80, 80)
        offset_y = random.randint(-80, 80)
        color = random.choice([ROSA_HOJA, ROSA_FOSFORO])
        tamano_maximo = random.randint(6, 12)
        hojas.append({
            "pos": (origen[0] + offset_x, origen[1] + offset_y),
            "size": 1,
            "max_size": tamano_maximo,
            "color": color
        })

# Bucle principal del software gráfico
ejecutando = True
while ejecutando:
    pantalla.fill(NEGRO)
    
    # Captura de eventos del sistema (Salir con ESC)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
            ejecutando = False

    # 1. Cálculo estricto del tiempo transcurrido
    milisegundos_totales = pygame.time.get_ticks() - tiempo_inicial
    segundos_totales = milisegundos_totales // 1000
    
    dias = segundos_totales // 86400
    horas = (segundos_totales % 86400) // 3600
    minutos = (segundos_totales % 3600) // 60
    segundos = segundos_totales % 60

    # 2. Trigger lógico: Si cambió el segundo actual, nacen hojas
    if segundos_totales > ultimo_segundo_registrado:
        agregar_hojas()
        ultimo_segundo_registrado = segundos_totales

    # 3. Renderizar el tronco estático del Cerezo Gigante
    for inicio, fin, grosor in lineas_tronco:
        pygame.draw.line(pantalla, MARRON_TRONCO, inicio, fin, grosor)

    # 4. Renderizar y actualizar el crecimiento orgánico de las hojas
    for hoja in hojas:
        if hoja["size"] < hoja["max_size"]:
            hoja["size"] += 0.2  # Crecimiento progresivo fluido animado
        pygame.draw.circle(pantalla, hoja["color"], (int(hoja["pos"][0]), int(hoja["pos"][1])), int(hoja["size"]))

    # 5. Renderizar el contador puro (Sin etiquetas de texto, solo números flotantes)
    fuente = pygame.font.SysFont("monospace", 65, bold=True)
    string_contador = f"{dias:02d}:{horas:02d}:{minutos:02d}:{segundos:02d}"
    superficie_texto = fuente.render(string_contador, True, BLANCO)
    
    # Posicionar contador centrado en la zona superior de la pantalla
    pantalla.blit(superficie_texto, (ANCHO // 2 - superficie_texto.get_width() // 2, 50))

    pygame.display.flip()
    reloj.tick(60)  # Forzar a 60 fotogramas por segundo estables

pygame.quit()
sys.exit()