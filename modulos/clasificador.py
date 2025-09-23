"""
modulos/clasificador.py
Clasificación simple de prendas:
- Usa descriptores de forma y una regla de distancia
"""

from typing import List
from . import descriptores

# Prototipos inventados (ejemplo, se deben entrenar con imágenes reales)
PROTOTIPOS = {
    "camiseta": [1e6, 5e8, 1e12],
    "pantalon": [2e6, 4e8, 8e12],
    "zapato":   [5e6, 1e9, 2e13]
}

def distancia(v1: List[float], v2: List[float]) -> float:
    return sum((a-b)**2 for a,b in zip(v1,v2))

def clasificar(matriz: List[List[int]], ancho: int, alto: int) -> str:
    """Clasifica la prenda según los momentos de Hu."""
    hu = descriptores.momentos_hu(matriz, ancho, alto)
    mejor = None
    menor_d = float("inf")
    for clase, prot in PROTOTIPOS.items():
        d = distancia(hu, prot)
        if d < menor_d:
            menor_d = d
            mejor = clase
    return mejor