"""
main.py
Proyecto de Procesamiento de Imágenes - UMNG
Menú principal para pruebas de cada módulo.
"""

import sys
from modulos import utils, preprocesamiento, segmentacion, bordes, descriptores, clasificador, colores

def mostrar_menu():
    print("\n=== Proyecto Clasificador de Prendas - UMNG ===")
    print("1) Cargar imagen en escala de grises (PGM)")
    print("2) Cargar imagen a color (PPM)")
    print("3) Preprocesar imagen (normalización, gamma, ecualización)")
    print("4) Segmentar silueta (umbral + morfología)")
    print("5) Detectar bordes con Sobel")
    print("6) Extraer descriptores (Hu)")
    print("7) Clasificar prenda")
    print("8) Detectar color dominante")
    print("9) Salir")

def main():
    matriz = None
    ancho = alto = max_valor = None
    color = False   # bandera para saber si la imagen es RGB o grises

    while True:
        mostrar_menu()
        opcion = input("Elija opción: ").strip()

        if opcion == "9":
            print("👋 Saliendo del programa...")
            sys.exit(0)

        elif opcion == "1":
            ruta = utils.seleccionar_imagen([("PGM", "*.pgm"), ("Todos", "*.*")])
            if not ruta:
                print("⚠️ No se seleccionó archivo.")
                continue
            try:
                matriz, ancho, alto, max_valor = utils.leer_pgm(ruta)
                color = False
                print(f"✅ Imagen PGM cargada - {ruta}")
                print(f"Dimensiones: {ancho}x{alto}")
            except Exception as e:
                print("⚠️ Error al cargar imagen:", e)

        elif opcion == "2":
            ruta = utils.seleccionar_imagen([("PPM", "*.ppm"), ("Todos", "*.*")])
            if not ruta:
                print("⚠️ No se seleccionó archivo.")
                continue
            try:
                matriz, ancho, alto, max_valor = utils.leer_ppm(ruta)
                color = True
                print(f"✅ Imagen PPM cargada - {ruta}")
                print(f"Dimensiones: {ancho}x{alto}")
            except Exception as e:
                print("⚠️ Error al cargar imagen:", e)

        elif opcion == "3":
            if matriz is None or color:
                print("⚠️ Debe cargar primero una imagen en escala de grises (PGM).")
            else:
                print("Aplicando preprocesamiento...")
                matriz = preprocesamiento.normalizar(matriz, ancho, alto, max_valor)
                matriz = preprocesamiento.gamma(matriz, ancho, alto, max_valor, gamma=0.8)
                matriz = preprocesamiento.ecualizar_histograma(matriz, ancho, alto, max_valor)
                print("✅ Preprocesamiento completado.")

        elif opcion == "4":
            if matriz is None:
                print("⚠️ Cargue una imagen primero.")
            else:
                print("Segmentando silueta...")
                matriz = segmentacion.umbral_otsu(matriz, ancho, alto, max_valor)
                matriz = segmentacion.morfologia(matriz, ancho, alto, operacion="apertura")
                print("✅ Segmentación completada.")

        elif opcion == "5":
            if matriz is None:
                print("⚠️ Cargue una imagen primero.")
            else:
                print("Detectando bordes con Sobel...")
                matriz = bordes.sobel(matriz, ancho, alto)
                print("✅ Bordes detectados.")

        elif opcion == "6":
            if matriz is None:
                print("⚠️ Cargue una imagen primero.")
            else:
                print("Extrayendo descriptores...")
                hu = descriptores.momentos_hu(matriz, ancho, alto)
                print("Momentos de Hu:", hu)
                print("✅ Descriptores extraídos.")

        elif opcion == "7":
            if matriz is None:
                print("⚠️ Cargue una imagen primero.")
            else:
                print("Clasificando prenda...")
                tipo = clasificador.clasificar(matriz, ancho, alto)
                print("👕 Prenda detectada:", tipo)

        elif opcion == "8":
            if matriz is None or not color:
                print("⚠️ Cargue primero una imagen a color (PPM).")
            else:
                print("Analizando color dominante...")
                dominante = colores.color_dominante(matriz, ancho, alto)
                print("🎨 Color dominante:", dominante)

        else:
            print("❌ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()