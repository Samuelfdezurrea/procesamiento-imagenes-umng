"""
modulos/segmentacion.py
Segmentación de silueta:
- Umbralización de Otsu
- Operaciones morfológicas básicas (erosión, dilatación, apertura, cierre)
"""

from typing import List

def umbral_otsu(matriz: List[List[int]], ancho: int, alto: int, max_valor: int) -> List[List[int]]:
    """Umbral automático de Otsu."""
    hist = [0] * (max_valor + 1)
    for fila in matriz:
        for v in fila:
            hist[v] += 1
    total = ancho * alto
    sum_total = sum(i * hist[i] for i in range(max_valor+1))

    sum_b = 0
    w_b = 0
    max_var = 0
    umbral = 0
    for t in range(max_valor+1):
        w_b += hist[t]
        if w_b == 0: continue
        w_f = total - w_b
        if w_f == 0: break
        sum_b += t * hist[t]
        m_b = sum_b / w_b
        m_f = (sum_total - sum_b) / w_f
        var = w_b * w_f * (m_b - m_f) ** 2
        if var > max_var:
            max_var = var
            umbral = t

    resultado = []
    for i in range(alto):
        fila = []
        for j in range(ancho):
            fila.append(255 if matriz[i][j] >= umbral else 0)
        resultado.append(fila)
    return resultado

def morfologia(matriz: List[List[int]], ancho: int, alto: int, operacion: str = "erosion") -> List[List[int]]:
    """
    Morfología binaria: erosión, dilatación, apertura, cierre.
    Usamos un elemento estructurante 3x3.
    """
    def erosion(m):
        out = [[0]*ancho for _ in range(alto)]
        for i in range(1, alto-1):
            for j in range(1, ancho-1):
                vecinos = [m[i+di][j+dj] for di in (-1,0,1) for dj in (-1,0,1)]
                out[i][j] = 255 if all(v==255 for v in vecinos) else 0
        return out

    def dilatacion(m):
        out = [[0]*ancho for _ in range(alto)]
        for i in range(1, alto-1):
            for j in range(1, ancho-1):
                vecinos = [m[i+di][j+dj] for di in (-1,0,1) for dj in (-1,0,1)]
                out[i][j] = 255 if any(v==255 for v in vecinos) else 0
        return out

    if operacion == "erosion":
        return erosion(matriz)
    elif operacion == "dilatacion":
        return dilatacion(matriz)
    elif operacion == "apertura":
        return dilatacion(erosion(matriz))
    elif operacion == "cierre":
        return erosion(dilatacion(matriz))
    else:
        raise ValueError("Operación no válida: elija erosion, dilatacion, apertura o cierre")