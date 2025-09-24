def detectar_bordes(imagen_gris):
    ancho, alto = imagen_gris.size
    pixeles = imagen_gris.load()
    nueva = imagen_gris.copy()
    salida = nueva.load()

    for x in range(1, ancho-1):
        for y in range(1, alto-1):
            # Extraer solo el valor de gris (r, g, b son iguales)
            def G(px): return px[0]

            gx = (-1*G(pixeles[x-1,y-1]) + 1*G(pixeles[x+1,y-1]) +
                  -2*G(pixeles[x-1,y])   + 2*G(pixeles[x+1,y]) +
                  -1*G(pixeles[x-1,y+1]) + 1*G(pixeles[x+1,y+1]))

            gy = (-1*G(pixeles[x-1,y-1]) + -2*G(pixeles[x,y-1]) + -1*G(pixeles[x+1,y-1]) +
                   1*G(pixeles[x-1,y+1]) +  2*G(pixeles[x,y+1]) +  1*G(pixeles[x+1,y+1]))

            magnitud = min(255, int((gx**2 + gy**2)**0.5))
            salida[x, y] = (magnitud, magnitud, magnitud)
    return nueva