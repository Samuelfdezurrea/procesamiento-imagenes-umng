from collections import Counter
from PIL import Image, ImageFilter

def calcular_umbral_otsu(im_l: Image.Image) -> int:
    """Implementación tipo Otsu para un image en modo 'L'."""
    ancho, alto = im_l.size
    pix = im_l.load()
    hist = Counter(pix[x, y] for x in range(ancho) for y in range(alto))
    total = ancho * alto
    # Acumulados
    sum_total = sum(i * hist.get(i, 0) for i in range(256))
    sum_b = 0
    w_b = 0
    var_max = 0
    umbral = 0
    for t in range(256):
        w_b += hist.get(t, 0)
        if w_b == 0:
            continue
        w_f = total - w_b
        if w_f == 0:
            break
        sum_b += t * hist.get(t, 0)
        m_b = sum_b / w_b
        m_f = (sum_total - sum_b) / w_f
        var_between = w_b * w_f * (m_b - m_f) ** 2
        if var_between > var_max:
            var_max = var_between
            umbral = t
    return umbral

def segmentar(imagen_gris):
    """
    Segmentación binaria:
    - Usa Otsu para calcular umbral en imagen en modo 'L'
    - Devuelve máscara RGB con (255,255,255) para objeto y (0,0,0) para fondo
    - Aplica cierre morfológico con filtros Max/Min para limpiar ruido (PIL)
    """
    im_l = imagen_gris.convert("L")
    ancho, alto = im_l.size
    umbral = calcular_umbral_otsu(im_l)

    mask = Image.new("L", (ancho, alto))
    mpx = mask.load()
    src = im_l.load()
    for x in range(ancho):
        for y in range(alto):
            mpx[x, y] = 255 if src[x, y] > umbral else 0

    # Cerrar pequeños huecos: aplicar MaxFilter (dilatación) y luego MinFilter (erosión)
    # Repetir una o dos veces según sea necesario para limpiar ruido
    mask = mask.filter(ImageFilter.MaxFilter(3))
    mask = mask.filter(ImageFilter.MinFilter(3))
    mask = mask.filter(ImageFilter.MaxFilter(3))
    mask = mask.filter(ImageFilter.MinFilter(3))

    # Devolver en RGB para compatibilidad con el resto del flujo
    return mask.convert("RGB")