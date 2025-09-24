from PIL import Image
from processing.grayscale import convertir_a_grises
from processing.bordes import detectar_bordes
from processing.segmentacion import segmentar
from utils.colores import obtener_color_predominante_segmentado

def clasificar_prenda(ruta_imagen):
    imagen_original = Image.open(ruta_imagen).convert("RGB")

    # Paso 1: Escala de grises
    imagen_gris = convertir_a_grises(imagen_original.copy())

    # Paso 2: Detección de bordes
    imagen_bordes = detectar_bordes(imagen_gris.copy())

    # Paso 3: Segmentación binaria
    imagen_segmentada = segmentar(imagen_gris.copy())

    # Paso 4: Clasificación geométrica
    ancho, alto = imagen_segmentada.size
    proporcion = alto / ancho

    if proporcion > 1.5:
        tipo = "Pantalón"
    elif proporcion < 1.0:
        tipo = "Camiseta"
    else:
        tipo = "Camisa"

    # Paso 5: Color usando solo píxeles segmentados
    color = obtener_color_predominante_segmentado(imagen_original, imagen_segmentada)

    return f"Prenda: {tipo}\nColor: {color}"