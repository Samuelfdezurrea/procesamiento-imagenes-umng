from colorsys import rgb_to_hls

def obtener_color_predominante_segmentado(imagen_original, imagen_segmentada):
    """
    Calcula color predominante basado únicamente en píxeles donde la máscara está blanca.
    Reglas:
      - Si saturación baja -> Blanco/Negro/Gris según luminancia
      - Si saturación alta -> usar rango de tono (en grados) para mapear a Rojo/Verde/Azul
    """
    img_color = imagen_original.convert("RGB")
    mask = imagen_segmentada.convert("L")
    ancho, alto = img_color.size
    pix_color = img_color.load()
    pix_mask = mask.load()

    conteo = {"Rojo": 0, "Verde": 0, "Azul": 0, "Negro/Gris": 0, "Blanco": 0}

    total_segmentados = 0
    for x in range(ancho):
        for y in range(alto):
            if pix_mask[x, y] >= 250:  # consideramos blanco de máscara como prenda
                r, g, b = pix_color[x, y]
                # normalizar
                rn, gn, bn = r / 255.0, g / 255.0, b / 255.0
                h, l, s = rgb_to_hls(rn, gn, bn)  # h en [0,1]
                total_segmentados += 1

                # umbrales robustos para gris/blanco/negro
                if s < 0.18:
                    if l > 0.85:
                        conteo["Blanco"] += 1
                    elif l < 0.25:
                        conteo["Negro/Gris"] += 1
                    else:
                        conteo["Negro/Gris"] += 1
                else:
                    h_deg = h * 360.0
                    # Rango extendido para rojo (maneja rojos/anaranjados)
                    if h_deg <= 30 or h_deg >= 330:
                        conteo["Rojo"] += 1
                    elif 30 < h_deg <= 100:
                        conteo["Verde"] += 1
                    elif 100 < h_deg <= 260:
                        conteo["Azul"] += 1
                    else:
                        # tonos intermedios se consideran Gris/Negro
                        conteo["Negro/Gris"] += 1

    if total_segmentados == 0:
        return "Desconocido"

    # Seleccionar color con mayor conteo
    color_pred = max(conteo, key=conteo.get)
    return color_pred