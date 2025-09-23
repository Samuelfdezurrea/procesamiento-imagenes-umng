"""
modulos/bordes.py
Detección de bordes con Sobel.
"""

from typing import List
from math import sqrt

def sobel(matriz: List[List[int]], ancho: int, alto: int) -> List[List[int]]:
    """Aplica el operador Sobel y devuelve magnitud de gradiente en rango [0,255]."""
    resultado = [[0]*ancho for _ in range(alto)]
    for i in range(1, alto-1):
        for j in range(1, ancho-1):
            gx = (-1*matriz[i-1][j-1] + 0*matriz[i-1][j] + 1*matriz[i-1][j+1]
                  -2*matriz[i][j-1]   + 0*matriz[i][j]   + 2*matriz[i][j+1]
                  -1*matriz[i+1][j-1] + 0*matriz[i+1][j] + 1*matriz[i+1][j+1])
            gy = (1*matriz[i-1][j-1] + 2*matriz[i-1][j] + 1*matriz[i-1][j+1]
                  +0*matriz[i][j-1]   + 0*matriz[i][j]   + 0*matriz[i][j+1]
                  -1*matriz[i+1][j-1] -2*matriz[i+1][j] -1*matriz[i+1][j+1])
            mag = int(sqrt(gx*gx + gy*gy))
            resultado[i][j] = min(255, max(0, mag))
    return resultado