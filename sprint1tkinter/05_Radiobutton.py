
# Ejercicio 5: Radiobutton

"""Crea un grupo de tres botones de opción (Radiobutton) para que el usuario elija su color
favorito (rojo, verde o azul).
Al seleccionar una opción, cambia el color de fondo de la ventana
al color elegido.
Recuerda: los Radiobutton comparten una misma variable (StringVar).
Usa root.config(bg=var.get()) para cambiar el color."""

import tkinter as tk

def cambiar_color():
   root.config(bg=color.get())

root = tk.Tk()
root.title("05_Radiobutton_Gabriela.A.V.I")
root.geometry("300x150")

color = tk.StringVar()
opcion_rojo = tk.Radiobutton(root, text="Rojo", variable=color, value="red", command=cambiar_color)
opcion_rojo.pack()
opcion_verde = tk.Radiobutton(root, text="Verde", variable=color, value="green", command=cambiar_color)
opcion_verde.pack()
opcion_azul = tk.Radiobutton(root, text="Azul", variable=color, value="blue", command=cambiar_color)
opcion_azul.pack()

root.mainloop()