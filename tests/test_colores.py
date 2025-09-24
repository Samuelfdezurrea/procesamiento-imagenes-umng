from PIL import Image
from utils.colores import obtener_color_predominante

def test_color_predominante_rojo():
    imagen = Image.new("RGB", (5, 5), color=(255, 0, 0))
    color = obtener_color_predominante(imagen)
    assert color == "Rojo", f"Color detectado incorrecto: {color}"