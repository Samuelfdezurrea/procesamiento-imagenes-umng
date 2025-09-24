from PIL import Image
from processing.grayscale import convertir_a_grises

def test_grayscale_conversion():
    imagen = Image.new("RGB", (2, 2), color=(100, 150, 200))
    gris = convertir_a_grises(imagen.copy())
    pixeles = gris.load()
    for x in range(2):
        for y in range(2):
            r, g, b = pixeles[x, y]
            assert r == g == b, "La conversión a escala de grises falló"