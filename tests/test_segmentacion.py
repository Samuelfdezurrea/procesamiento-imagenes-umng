from PIL import Image
from processing.segmentacion import segmentar

def test_segmentacion_binaria():
    imagen = Image.new("RGB", (2, 2), color=(200, 200, 200))  # gris claro
    resultado = segmentar(imagen.copy())
    pixeles = resultado.load()
    for x in range(2):
        for y in range(2):
            assert pixeles[x, y] == (255, 255, 255), "La segmentación binaria falló"