import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from collections import deque

def _extract_largest_cc(binary_mask):
    """Extrae la mayor componente conexa de un mask binario."""
    h, w = binary_mask.shape
    visited = np.zeros((h, w), dtype=bool)
    best_mask = np.zeros((h, w), dtype=bool)
    best_size = 0

    for y in range(h):
        for x in range(w):
            if binary_mask[y, x] and not visited[y, x]:
                q = deque([(y, x)])
                visited[y, x] = True
                comp_coords = []
                while q:
                    yy, xx = q.popleft()
                    comp_coords.append((yy, xx))
                    for ny, nx in ((yy-1, xx), (yy+1, xx), (yy, xx-1), (yy, xx+1)):
                        if 0 <= ny < h and 0 <= nx < w and (not visited[ny, nx]) and binary_mask[ny, nx]:
                            visited[ny, nx] = True
                            q.append((ny, nx))
                size = len(comp_coords)
                if size > best_size:
                    best_size = size
                    best_mask[:, :] = False
                    for yy, xx in comp_coords:
                        best_mask[yy, xx] = True
    return best_mask

def _nombre_color(r, g, b):
    """Clasifica color predominante a partir de promedios RGB."""
      # Brillo total
    brillo = (r + g + b) / 3

    if brillo < 40:
        return "Negro"
    if brillo > 220:
        return "Blanco"

    # Comparar canales
    if r > g and r > b:
        if g > 100 and b < 80:
            return "Naranja / Marrón"
        return "Rojo"
    elif g > r and g > b:
        return "Verde"
    elif b > r and b > g:
        return "Azul"

    # Mezclas
    if abs(r - g) < 30 and b < 100:
        return "Amarillo"
    if abs(r - b) < 30 and g < 100:
        return "Magenta"
    if abs(g - b) < 30 and r < 100:
        return "Cian"
    
    return "Color indefinido"

def mostrar_histogramas(imagen_color: Image.Image, imagen_segmentada: Image.Image):
    """
    Dibuja un gráfico de barras con intensidades promedio R/G/B
    usando SOLO píxeles de la prenda segmentada.
    Detecta automáticamente si la prenda está en blanco o en negro
    comparando el brillo medio de las componentes.
    """
    arr_color = np.array(imagen_color.convert("RGB"))
    arr_mask = np.array(imagen_segmentada.convert("L"))

    cand_white = arr_mask > 128
    cand_black = arr_mask <= 128

    cc_white = _extract_largest_cc(cand_white)
    cc_black = _extract_largest_cc(cand_black)

    # Calcular brillo promedio de cada componente
    def mean_brightness(mask):
        if mask.sum() == 0:
            return 9999
        vals = arr_color[mask]
        return vals.mean()

    mean_white = mean_brightness(cc_white)
    mean_black = mean_brightness(cc_black)

    # Elegir la componente más oscura como prenda
    if mean_black < mean_white:
        mask_object = cc_black
    else:
        mask_object = cc_white

    if mask_object.sum() == 0:
        print("⚠️ No se detectó prenda en la segmentación.")
        return

    r_mean = arr_color[:, :, 0][mask_object].mean()
    g_mean = arr_color[:, :, 1][mask_object].mean()
    b_mean = arr_color[:, :, 2][mask_object].mean()

    nombre = _nombre_color(r_mean, g_mean, b_mean)

    colores = ["Rojo", "Verde", "Azul"]
    valores = [r_mean, g_mean, b_mean]
    colores_plot = ["red", "green", "blue"]

    plt.figure(figsize=(6, 5))
    plt.bar(colores, valores, color=colores_plot, alpha=0.8)
    plt.ylim(0, 255)
    plt.ylabel("Intensidad (0-255)")
    for i, v in enumerate(valores):
        plt.text(i, v + 3, f"{v:.1f}", ha="center")
    plt.tight_layout()
    plt.show()

    return {"R": r_mean, "G": g_mean, "B": b_mean, "Nombre": nombre}
