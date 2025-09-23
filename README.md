# procesamiento-imagenes-umng
Proyecto de Procesamiento de Imágenes, Programa que identifica prendas de vestir
# Procesamiento de Imágenes - UMNG

## Descripción
Proyecto académico para la materia *Procesamiento de Imágenes*.  
Implementaciones en **Python puro** (sin OpenCV, NumPy ni PIL) de filtros espaciales y ecualización, basadas en las fórmulas vistas en clase.

## Estructura
- `main.py` → interfaz por consola para aplicar filtros.
- `modulos/` → implementación de algoritmos:
  - `utilidades.py` → lectura/escritura PGM.
  - `filtros.py` → filtros promedio, mediana, Sobel.
  - `ecualizacion.py` → ecualización de histograma.
- `imagenes/` → imágenes PGM de entrada/salida.
- `tests/` → pruebas unitarias con `unittest`.
- `docs/` → documentación del proyecto / entregas.

## Formulas aplicadas (resumen)
- **Filtro promedio k×k:** salida = promedio aritmético de la ventana (Σ vecinos / k²).
- **Filtro mediana 3×3:** salida = mediana de los 9 valores en la ventana.
- **Sobel:** Gx y Gy con kernels clásicos; magnitud = sqrt(Gx² + Gy²).
- **Ecualización:** salida = round((cdf[v] - cdf_min) / (N - cdf_min) * max_valor).

> Todas las fórmulas se implementaron siguiendo el material de apoyo del profesor tal como se solicita en el enunciado del proyecto.

## Requisitos
- Python 3.8+ (no se requieren librerías externas para el procesamiento implementado).
- Para ejecutar pruebas: `python -m unittest`

## Uso rápido
1. Coloca una imagen PGM (formato ASCII P2) en `imagenes/` (ej: `imagenes/ejemplo1.pgm`).
2. Ejecuta:
```bash
python main.py
