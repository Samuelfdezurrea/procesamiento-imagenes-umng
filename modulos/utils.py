"""
modulos/utils.py
Funciones para cargar y guardar imágenes en formatos PGM (grises) y PPM (color).
Incluye además un selector de archivos con Tkinter.
No se usan librerías externas de procesamiento.
"""

from typing import List, Tuple
import tkinter as tk
from tkinter import filedialog

# ----------- PGM (grises) -----------

def leer_pgm(ruta: str) -> Tuple[List[List[int]], int, int, int]:
    """
    Lee una imagen en formato PGM (P2 - ASCII).
    Retorna (matriz, ancho, alto, max_valor).
    """
    with open(ruta, "r") as f:
        tipo = f.readline().strip()
        if tipo != "P2":
            raise ValueError("El archivo no es PGM ASCII (P2).")

        # Saltar comentarios
        linea = f.readline().strip()
        while linea.startswith("#"):
            linea = f.readline().strip()

        ancho, alto = map(int, linea.split())
        max_valor = int(f.readline().strip())

        valores = []
        for linea in f:
            valores.extend(linea.split())

        matriz = []
        k = 0
        for i in range(alto):
            fila = []
            for j in range(ancho):
                fila.append(int(valores[k]))
                k += 1
            matriz.append(fila)

    return matriz, ancho, alto, max_valor


def guardar_pgm(ruta: str, matriz: List[List[int]], ancho: int, alto: int, max_valor: int = 255):
    """Guarda una matriz en formato PGM (P2)."""
    with open(ruta, "w") as f:
        f.write("P2\n")
        f.write(f"{ancho} {alto}\n")
        f.write(f"{max_valor}\n")
        for fila in matriz:
            f.write(" ".join(str(min(max(0, v), max_valor)) for v in fila) + "\n")


# ----------- PPM (color) -----------

def leer_ppm(ruta: str) -> Tuple[List[List[Tuple[int,int,int]]], int, int, int]:
    """
    Lee una imagen en formato PPM (P3 - ASCII).
    Retorna (matriz, ancho, alto, max_valor).
    Cada píxel es una tupla (R,G,B).
    """
    with open(ruta, "r") as f:
        tipo = f.readline().strip()
        if tipo != "P3":
            raise ValueError("El archivo no es PPM ASCII (P3).")

        # Saltar comentarios
        linea = f.readline().strip()
        while linea.startswith("#"):
            linea = f.readline().strip()

        ancho, alto = map(int, linea.split())
        max_valor = int(f.readline().strip())

        valores = []
        for linea in f:
            valores.extend(linea.split())

        matriz = []
        k = 0
        for i in range(alto):
            fila = []
            for j in range(ancho):
                r = int(valores[k]); g = int(valores[k+1]); b = int(valores[k+2])
                fila.append((r, g, b))
                k += 3
            matriz.append(fila)

    return matriz, ancho, alto, max_valor


def guardar_ppm(ruta: str, matriz: List[List[Tuple[int,int,int]]], ancho: int, alto: int, max_valor: int = 255):
    """Guarda una matriz en formato PPM (P3)."""
    with open(ruta, "w") as f:
        f.write("P3\n")
        f.write(f"{ancho} {alto}\n")
        f.write(f"{max_valor}\n")
        for fila in matriz:
            linea = " ".join(f"{r} {g} {b}" for (r,g,b) in fila)
            f.write(linea + "\n")


# ----------- Selector de archivos -----------

def seleccionar_imagen(extensiones=[("PGM/PPM", "*.pgm *.ppm"), ("Todos", "*.*")]) -> str:
    """
    Abre un cuadro de diálogo para seleccionar un archivo de imagen.
    Retorna la ruta seleccionada o "" si se cancela.
    """
    root = tk.Tk()
    root.withdraw()  # ocultar ventana principal
    ruta = filedialog.askopenfilename(title="Seleccione una imagen", filetypes=extensiones)
    root.destroy()
    return ruta