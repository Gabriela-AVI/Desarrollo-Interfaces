
# EJERCICIOS 8: Frame

""" Diseña una interfaz dividida en dos Frame:
• El Frame superior debe contener dos etiquetas y un campo de entrada.
• El Frame inferior debe tener dos botones:
    - Uno para mostrar el contenido del Entry en una etiqueta.
    - Otro para borrar su contenido.
Puedes organizar los widgets con grid() dentro de cada Frame."""

import tkinter as tk

def mostrar():
    mensaje.config(text=f"{entry1.get()}")
def borrar():
    mensaje.config(text=f"")

root = tk.Tk()
root.title("08_Frames_Gabriela.A.V.I")
root.geometry("400x400")

#Crear Frame
frame1 = tk.Frame(root, relief="sunken", borderwidth=1)
frame1.pack(padx=10, pady=10)

frame2 = tk.Frame(root, relief="sunken", borderwidth=1)
frame2.pack(padx=10, pady=10)

#Crear widgets dentro de Frame1
etiqueta1 = tk.Label(frame1, text="Primera etiqueta")
etiqueta1.grid(row=0, column=0, padx=5, pady=5)
etiqueta2 = tk.Label(frame1, text="Segunda etiqueta")
etiqueta2.grid(row=1, column=0, padx=5, pady=5)

entry1 = tk.Entry(frame1)
entry1.grid(row=2, column=0, padx=5, pady=5)

#Crear widgets dentro de Frame2
mensaje = tk.Label(frame2, text="")
mensaje.grid(row=0, column=0, columnspan=2, pady=10)

boton1 = tk.Button(frame2, text="Mostrar", command=mostrar)
boton1.grid(row=1, column=0, padx=10, pady=10)
boton2 = tk.Button(frame2, text="Borrar", command=borrar)
boton2.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()

