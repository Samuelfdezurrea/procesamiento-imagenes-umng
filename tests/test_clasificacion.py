from processing.clasificacion import clasificar_prenda

def test_clasificacion_mock():
    # Usa una imagen de prueba que esté en /data/
    resultado = clasificar_prenda("data/ejemplo.jpg")
    assert "Prenda:" in resultado and "Color:" in resultado, "La clasificación no devolvió formato esperado"