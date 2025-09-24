def convertir_a_grises(imagen_rgb):
    ancho, alto = imagen_rgb.size
    pixeles = imagen_rgb.load()
    for x in range(ancho):
        for y in range(alto):
            r, g, b = pixeles[x, y]
            gris = int(0.299*r + 0.587*g + 0.114*b)  # Fórmula del profesor
            pixeles[x, y] = (gris, gris, gris)
    return imagen_rgb