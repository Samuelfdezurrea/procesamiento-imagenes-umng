"""
modulos/preprocesamiento.py
Operaciones de preprocesamiento fotométrico:
- Normalización lineal
- Corrección gamma
- Ecualización de histograma
"""

from typing import List
import math

def normalizar(matriz: List[List[int]], ancho: int, alto: int, max_valor: int) -> List[List[int]]:
    """Normaliza intensidades a rango [0, max_valor]."""
    minimo = min(min(fila) for fila in matriz)
    maximo = max(max(fila) for fila in matriz)
    resultado = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            val = (matriz[i][j] - minimo) * max_valor // (maximo - minimo + 1)
            fila.append(val)
        resultado.append(fila)
    return resultado

def gamma(matriz: List[List[int]], ancho: int, alto: int, max_valor: int, gamma: float = 1.0) -> List[List[int]]:
    """Corrección gamma: s = c * r^gamma"""
    c = max_valor / (max_valor ** gamma)
    resultado = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            r = matriz[i][j]
            s = int(c * (r ** gamma))
            fila.append(min(max(s, 0), max_valor))
        resultado.append(fila)
    return resultado

def ecualizar_histograma(matriz: List[List[int]], ancho: int, alto: int, max_valor: int) -> List[List[int]]:
    """Ecualización de histograma (PDF del profe)."""
    N = ancho * alto
    hist = [0] * (max_valor + 1)
    for fila in matriz:
        for v in fila:
            hist[v] += 1
    cdf = [0] * (max_valor + 1)
    cdf[0] = hist[0]
    for i in range(1, max_valor + 1):
        cdf[i] = cdf[i-1] + hist[i]
    # Transformación
    resultado = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            val = matriz[i][j]
            s = int((cdf[val] - cdf[0]) / (N - 1) * max_valor)
            fila.append(s)
        resultado.append(fila)
    return resultado