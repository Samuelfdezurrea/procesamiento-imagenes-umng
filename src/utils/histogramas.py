import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def mostrar_histogramas(imagen_color: Image.Image, imagen_segmentada: Image.Image):
    """
    Genera histogramas de color SOLO de los píxeles segmentados.
    Intensidad en eje Y, frecuencia en eje X.
    Retorna el color dominante (Rojo, Verde, Azul).
    """
    mask = imagen_segmentada.convert("L")
    arr_mask = np.array(mask)
    arr_color = np.array(imagen_color.convert("RGB"))

    indices = arr_mask >= 250
    if indices.sum() == 0:
        r = arr_color[:, :, 0].flatten()
        g = arr_color[:, :, 1].flatten()
        b = arr_color[:, :, 2].flatten()
    else:
        r = arr_color[:, :, 0][indices]
        g = arr_color[:, :, 1][indices]
        b = arr_color[:, :, 2][indices]

    # Hist counts
    hist_r, _ = np.histogram(r, bins=256, range=(0, 255))
    hist_g, _ = np.histogram(g, bins=256, range=(0, 255))
    hist_b, _ = np.histogram(b, bins=256, range=(0, 255))

    intensidades = np.arange(256)
    plt.figure(figsize=(7, 7))
    plt.barh(intensidades, hist_r, color="red", alpha=0.6, label="Rojo")
    plt.barh(intensidades, hist_g, color="green", alpha=0.6, label="Verde")
    plt.barh(intensidades, hist_b, color="blue", alpha=0.6, label="Azul")
    plt.title("Histograma de Color (solo objeto segmentado)")
    plt.ylabel("Intensidad")
    plt.xlabel("Frecuencia")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Dominante
    total_r, total_g, total_b = hist_r.sum(), hist_g.sum(), hist_b.sum()
    maximo = max(total_r, total_g, total_b)
    if maximo == total_r:
        return "Rojo"
    elif maximo == total_g:
        return "Verde"
    else:
        return "Azul"