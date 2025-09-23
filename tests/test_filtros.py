import unittest
from modulos.utilidades import guardar_pgm, leer_pgm
from modulos.filtros import filtro_promedio, filtro_mediana_3x3, sobel
from modulos.ecualizacion import ecualizar

class TestFiltros(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Creamos una imagen de prueba pequeña 5x5 en imagenes/ para las pruebas
        cls.ruta = "imagenes/prueba_5x5.pgm"
        ancho, alto, maxv = 5, 5, 255
        # matriz con un pico central
        matriz = [
            [10,10,10,10,10],
            [10,10,10,10,10],
            [10,10,255,10,10],
            [10,10,10,10,10],
            [10,10,10,10,10],
        ]
        guardar_pgm(cls.ruta, matriz, ancho, alto, maxv)

    def test_promedio(self):
        m, a, h, mv = leer_pgm("imagenes/prueba_5x5.pgm")
        r = filtro_promedio(m, a, h, k=3)
        self.assertEqual(len(r), h)
        self.assertEqual(len(r[0]), a)

    def test_mediana(self):
        m, a, h, mv = leer_pgm("imagenes/prueba_5x5.pgm")
        r = filtro_mediana_3x3(m, a, h)
        self.assertEqual(len(r), h)

    def test_sobel(self):
        m, a, h, mv = leer_pgm("imagenes/prueba_5x5.pgm")
        r = sobel(m, a, h)
        # La matriz resultante debe tener mismas dimensiones
        self.assertEqual(len(r), h)
        self.assertEqual(len(r[0]), a)

    def test_ecualizacion(self):
        m, a, h, mv = leer_pgm("imagenes/prueba_5x5.pgm")
        r = ecualizar(m, a, h, mv)
        self.assertEqual(len(r), h)

if __name__ == "__main__":
    unittest.main()