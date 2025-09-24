import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from processing.clasificacion import clasificar_prenda

def _pil_to_tk(img_pil, maxsize=(250, 250)):
    im = img_pil.copy()
    im.thumbnail(maxsize)
    return ImageTk.PhotoImage(im)

def iniciar_app():
    root = tk.Tk()
    root.title("Clasificación Automática de Prendas")
    root.geometry("1300x750")
    root.configure(bg="#f7f7f7")

    # Frame superior con botón
    frame_top = tk.Frame(root, bg="#f7f7f7")
    frame_top.pack(fill="x", pady=5)
    boton_cargar = tk.Button(frame_top, text="Cargar Imagen", font=("Arial", 12),
                             command=lambda: cargar_imagen(),
                             bg="#1976d2", fg="white", padx=16, pady=8)
    boton_cargar.pack()

    # Frame principal (imagenes izquierda, resultado derecha)
    frame_main = tk.Frame(root, bg="#f7f7f7")
    frame_main.pack(fill="both", expand=True, padx=10, pady=10)

    frame_imgs = tk.Frame(frame_main, bg="#ffffff", bd=1, relief="solid")
    frame_imgs.pack(side="left", padx=10, pady=10)

    # Original
    original_label = tk.Label(frame_imgs, text="Imagen original (con bbox)", bg="#ffffff")
    original_label.pack()
    original_canvas = tk.Label(frame_imgs, bg="#ddd")
    original_canvas.pack(padx=8, pady=8)

    # Previews
    previews = {}
    for titulo in ["Escala de grises", "Bordes (Sobel)", "Segmentación (máscara)"]:
        lbl = tk.Label(frame_imgs, text=titulo, bg="#ffffff")
        lbl.pack()
        panel = tk.Label(frame_imgs, bg="#eee")
        panel.pack(padx=8, pady=6)
        previews[titulo] = panel

    # Resultado a la derecha
    frame_result = tk.Frame(frame_main, bg="#f7f7f7")
    frame_result.pack(side="right", padx=20, pady=20, fill="y")

    resultado_label = tk.Label(frame_result, text="Resultado:", font=("Arial", 16),
                               bg="#f7f7f7", justify="left")
    resultado_label.pack(anchor="n")

    def cargar_imagen():
        ruta = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=[("Imágenes", ("*.jpg", "*.jpeg", "*.png", "*.bmp", "*.gif"))]
        )
        if not ruta:
            return
        try:
            resultado_texto, img_gris, img_bordes, img_seg, original_bbox = clasificar_prenda(ruta)

            tk_orig = _pil_to_tk(original_bbox, maxsize=(350, 350))
            original_canvas.config(image=tk_orig)
            original_canvas.image = tk_orig

            tk_g = _pil_to_tk(img_gris)
            previews["Escala de grises"].config(image=tk_g)
            previews["Escala de grises"].image = tk_g

            tk_b = _pil_to_tk(img_bordes)
            previews["Bordes (Sobel)"].config(image=tk_b)
            previews["Bordes (Sobel)"].image = tk_b

            tk_s = _pil_to_tk(img_seg)
            previews["Segmentación (máscara)"].config(image=tk_s)
            previews["Segmentación (máscara)"].image = tk_s

            resultado_label.config(text=f"Resultado:\n{resultado_texto}")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo procesar la imagen: {e}")

    root.mainloop()