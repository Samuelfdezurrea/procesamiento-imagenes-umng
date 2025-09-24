import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from processing.clasificacion import clasificar_prenda

def cargar_imagen():
    ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.jpg *.png *.bmp")])
    if ruta:
        imagen = Image.open(ruta)
        imagen.thumbnail((300, 300))
        img_tk = ImageTk.PhotoImage(imagen)
        panel.config(image=img_tk)
        panel.image = img_tk
        resultado = clasificar_prenda(ruta)
        resultado_label.config(text=resultado)

def iniciar_app():
    global panel, resultado_label
    ventana = tk.Tk()
    ventana.title("Clasificador de Prendas")
    ventana.geometry("400x500")

    btn_cargar = tk.Button(ventana, text="Cargar imagen", command=cargar_imagen)
    btn_cargar.pack(pady=10)

    panel = tk.Label(ventana)
    panel.pack()

    resultado_label = tk.Label(ventana, text="", font=("Arial", 14))
    resultado_label.pack(pady=20)

    ventana.mainloop()