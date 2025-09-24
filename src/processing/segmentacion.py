def segmentar(imagen_gris):
    ancho, alto = imagen_gris.size
    pixeles = imagen_gris.load()
    nueva = imagen_gris.copy()
    salida = nueva.load()

    umbral = 128  # valor fijo o calculado por histograma
    for x in range(ancho):
        for y in range(alto):
            gris = pixeles[x, y][0]
            salida[x, y] = (255, 255, 255) if gris > umbral else (0, 0, 0)
    return nueva