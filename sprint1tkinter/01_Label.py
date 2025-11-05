
# Ejercicio 1: Label

"""Crea una ventana que muestre tres etiquetas (Label):
1. La primera debe mostrar un mensaje de bienvenida.
2. La segunda debe mostrar tu nombre completo.
3. La tercera debe cambiar su texto cuando se presione un botón.
Usa config(text="nuevo texto") dentro de la función asociada al botón."""

import tkinter as tk

def cambiar_texto():
    etiqueta3.config(text="Nuevo texto")

root = tk.Tk()
root.title("01_Label_Gabriela.A.V.I")
root.geometry("300x150")

etiqueta1 = tk.Label(root, text="Bienvenida!")
etiqueta1.pack()

etiqueta2 = (tk.Label(root, text="Gabriela Antía Vázquez Iglesias"))
etiqueta2.pack()

etiqueta3 = (tk.Label(root, text="texto"))
etiqueta3.pack()

boton = tk.Button(root, text="Cambiar texto", command=cambiar_texto)
boton.pack()

root.mainloop()