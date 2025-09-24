import matplotlib.pyplot as plt
from PIL import Image

def mostrar_histograma_rgb(ruta_imagen):
    imagen = Image.open(ruta_imagen).convert("RGB")
    r_values, g_values, b_values = [], [], []
    pixeles = imagen.load()
    ancho, alto = imagen.size

    for x in range(ancho):
        for y in range(alto):
            r, g, b = pixeles[x, y]
            r_values.append(r)
            g_values.append(g)
            b_values.append(b)

    plt.figure(figsize=(10, 5))
    plt.hist(r_values, bins=256, color='red', alpha=0.5, label='Rojo')
    plt.hist(g_values, bins=256, color='green', alpha=0.5, label='Verde')
    plt.hist(b_values, bins=256, color='blue', alpha=0.5, label='Azul')
    plt.title("Histograma RGB de la imagen")
    plt.xlabel("Intensidad (0-255)")
    plt.ylabel("Cantidad de píxeles")
    plt.legend()
    plt.grid(True)
    plt.show()

# Ejecuta con una imagen de prueba
mostrar_histograma_rgb("data/camiseta_azul.jpg")