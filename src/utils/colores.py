from colorsys import rgb_to_hls

def obtener_color_predominante_segmentado(imagen_original, imagen_segmentada):
    pixeles_color = imagen_original.load()
    pixeles_segmento = imagen_segmentada.load()
    ancho, alto = imagen_original.size

    colores = {
        "Rojo": 0,
        "Verde": 0,
        "Azul": 0,
        "Negro/Gris": 0,
        "Blanco": 0
    }

    for x in range(ancho):
        for y in range(alto):
            if pixeles_segmento[x, y] == (255, 255, 255):  # Solo píxeles de la prenda
                r, g, b = pixeles_color[x, y]
                r /= 255
                g /= 255
                b /= 255
                h, l, s = rgb_to_hls(r, g, b)

                if l > 0.9:
                    colores["Blanco"] += 1
                elif l < 0.2:
                    colores["Negro/Gris"] += 1
                elif h < 0.05 or h > 0.95:
                    colores["Rojo"] += 1
                elif 0.05 <= h < 0.4:
                    colores["Verde"] += 1
                elif 0.4 <= h < 0.7:
                    colores["Azul"] += 1
                else:
                    colores["Negro/Gris"] += 1

    return max(colores, key=colores.get)