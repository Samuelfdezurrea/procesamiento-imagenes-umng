"""
modulos/descriptores.py
Extracción de descriptores:
- Momentos invariantes de Hu
"""

from typing import List
import math

def momentos_hu(matriz: List[List[int]], ancho: int, alto: int) -> List[float]:
    """
    Calcula los 7 momentos invariantes de Hu de la silueta binaria.
    Implementación básica.
    """
    # Momentos espaciales
    m00 = sum(sum(fila) for fila in matriz)
    m10 = sum(i * sum(matriz[i][j] for j in range(ancho)) for i in range(alto))
    m01 = sum(j * sum(matriz[i][j] for i in range(alto)) for j in range(ancho))
    x_bar = m10 / m00
    y_bar = m01 / m00

    # Momentos centrales
    def mu(p, q):
        return sum((i-x_bar)**p * (j-y_bar)**q * matriz[i][j]
                   for i in range(alto) for j in range(ancho))

    mu20, mu02, mu11 = mu(2,0), mu(0,2), mu(1,1)
    mu30, mu03, mu21, mu12 = mu(3,0), mu(0,3), mu(2,1), mu(1,2)

    # Momentos invariantes de Hu (simplificados)
    hu1 = mu20 + mu02
    hu2 = (mu20 - mu02)**2 + 4*mu11**2
    hu3 = (mu30 - 3*mu12)**2 + (3*mu21 - mu03)**2
    return [hu1, hu2, hu3]  # puedes ampliar a los 7