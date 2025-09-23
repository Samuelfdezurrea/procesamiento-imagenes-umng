"""
modulos/colores.py
Detección de color dominante en imágenes PPM.
"""

from typing import List, Tuple

def color_dominante(matriz: List[List[Tuple[int,int,int]]], ancho: int, alto: int) -> str:
    """Determina el color dominante promedio."""
    total_r = total_g = total_b = 0
    for fila in matriz:
        for (r,g,b) in fila:
            total_r += r
            total_g += g
            total_b += b
    n = ancho * alto
    r, g, b = total_r//n, total_g//n, total_b//n

    # Clasificación simple de colores
    if r>200 and g>200 and b>200: return "blanco"
    if r<50 and g<50 and b<50: return "negro"
    if r>g and r>b: return "rojo"
    if g>r and g>b: return "verde"
    if b>r and b>g: return "azul"
    return "otro"