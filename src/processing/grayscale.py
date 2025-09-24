from PIL import Image

def convertir_a_grises(imagen_rgb: Image.Image) -> Image.Image:
    ancho, alto = imagen_rgb.size
    img = imagen_rgb.convert("RGB")
    pix = img.load()
    for x in range(ancho):
        for y in range(alto):
            r, g, b = pix[x, y]
            gris = int(0.299 * r + 0.587 * g + 0.114 * b)
            pix[x, y] = (gris, gris, gris)
    return img