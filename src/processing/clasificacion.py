from PIL import Image, ImageDraw
import numpy as np
from processing.grayscale import convertir_a_grises
from processing.bordes import detectar_bordes
from processing.segmentacion import segmentar
from utils.histogramas import mostrar_histogramas

# === Plantillas de referencia (silhouettes binarias normalizadas) ===
def _plantillas():
    cam = Image.open("data/ref_camisa.png").convert("L").resize((100, 100))
    pan = Image.open("data/ref_pantalon.png").convert("L").resize((100, 100))
    cami = Image.open("data/ref_camiseta.png").convert("L").resize((100, 100))
    return {
        "Camisa": np.array(cam) > 128,
        "Pantalón": np.array(pan) > 128,
        "Camiseta": np.array(cami) > 128
    }

def _clasificar_por_referencia(mask: Image.Image):
    """
    Compara la máscara segmentada contra plantillas binarias y devuelve la prenda más parecida.
    """
    refs = _plantillas()
    mask_resized = mask.convert("L").resize((100, 100))
    mask_arr = np.array(mask_resized) > 128

    best_tipo = "Desconocido"
    best_score = 1e12
    for tipo, ref in refs.items():
        diff = np.sum(mask_arr != ref)
        if diff < best_score:
            best_score = diff
            best_tipo = tipo
    return best_tipo

def clasificar_prenda(ruta_imagen):
    imagen_original = Image.open(ruta_imagen).convert("RGB")

    # Paso 1: Grises
    imagen_gris = convertir_a_grises(imagen_original.copy())

    # Paso 2: Bordes
    imagen_bordes = detectar_bordes(imagen_gris.copy())

    # Paso 3: Segmentación
    imagen_segmentada = segmentar(imagen_gris.copy())

    # Paso 4: Clasificación por plantilla
    tipo = _clasificar_por_referencia(imagen_segmentada)

    # Paso 5: Color dominante del histograma
    color = mostrar_histogramas(imagen_original, imagen_segmentada)

    # Paso 6: BBox para mostrar
    bbox = imagen_segmentada.getbbox() or (0, 0, imagen_original.size[0], imagen_original.size[1])
    minx, miny, maxx, maxy = bbox
    original_bbox = imagen_original.copy()
    draw = ImageDraw.Draw(original_bbox)
    draw.rectangle([minx, miny, maxx, maxy], outline=(255, 0, 0), width=3)

    resultado_texto = f"Prenda: {tipo}\nColor: {color}"
    return resultado_texto, imagen_gris, imagen_bordes, imagen_segmentada, original_bbox