
# Ejercicio 11: Scale

"""
Crea una barra deslizante (Scale) que permita al usuario seleccionar un número entre 0 y 100.
El valor seleccionado debe mostrarse en tiempo real en una etiqueta.
Usa command=funcion en la Scale para actualizar la etiqueta cada vez que se mueva el control.*
"""

import tkinter as tk

def actualizar(valor):
    etiqueta.config(text=f"Valor: {valor}")

root = tk.Tk()
root.title("11_Scale_Gabriela.A.V.I")
root.geometry("300x300")

#Crear a Scale
scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=actualizar)
scale.pack(pady=20)

#Mostrar seleccionado
etiqueta = tk.Label(root, text="Valor: 0")
etiqueta.pack()

root.mainloop()