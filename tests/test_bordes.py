from PIL import Image
from processing.bordes import detectar_bordes

def test_bordes_output_size():
    imagen = Image.new("RGB", (10, 10), color=(128, 128, 128))
    resultado = detectar_bordes(imagen.copy())
    assert resultado.size == (10, 10), "La imagen de bordes tiene tamaño incorrecto"