# Ejercicio 3: Entry

"""Crea una interfaz con un campo de entrada (Entry) donde el usuario escriba su nombre.
Al hacer clic en un botón, debe mostrarse un saludo personalizado en una etiqueta.
Prueba a usar entrada.get() para obtener el texto del usuario."""

import tkinter as tk

def saludar():
   etiqueta.config(text=f"Hola, {nombre.get()}  :)")

root = tk.Tk()
root.title("03_Entry_Gabriela.A.V.I")
root.geometry("300x150")

etiqueta = (tk.Label(root, text="Introduzca su nombre:"))
etiqueta.pack()

nombre = tk.Entry(root)
nombre.pack()

boton = tk.Button(root, text="Saludar", command=saludar)
boton.pack()

root.mainloop()



