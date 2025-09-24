from PIL import Image

def detectar_bordes(imagen_gris: Image.Image) -> Image.Image:
    
    img_l = imagen_gris.convert("L")
    ancho, alto = img_l.size
    pix = img_l.load()

    # Crear imagen de salida en L
    salida = Image.new("L", (ancho, alto))
    s_pix = salida.load()

    # Kernels Sobel
    Gx = [[-1, 0, 1],
          [-2, 0, 2],
          [-1, 0, 1]]

    Gy = [[-1, -2, -1],
          [0,   0,  0],
          [1,   2,  1]]

    for x in range(1, ancho - 1):
        for y in range(1, alto - 1):
            sx = 0
            sy = 0
            for j in range(3):
                for i in range(3):
                    val = pix[x + i - 1, y + j - 1]
                    sx += Gx[j][i] * val
                    sy += Gy[j][i] * val
            magn = int((sx * sx + sy * sy) ** 0.5)
            if magn > 255:
                magn = 255
            elif magn < 0:
                magn = 0
            s_pix[x, y] = magn

    # convertir a RGB para que sea consistente con el resto del flujo
    return salida.convert("RGB")