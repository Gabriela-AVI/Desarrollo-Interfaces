
# Ejercicio 2: Button

"""Diseña una ventana con dos botones:
  - Uno debe mostrar un mensaje en una etiqueta al presionarlo.
  - El otro debe cerrar la ventana.
Puedes usar root.quit() para salir de la aplicación."""

import tkinter as tk

def mensaje_etiqueta():
   etiqueta.config(text="Has pulsado el botón")

root = tk.Tk()
root.title("02_Button_Gabriela.A.V.I")
root.geometry("300x150")

boton1 = tk.Button(root, text="Botón etiqueta", command=mensaje_etiqueta)
boton1.pack()
etiqueta = (tk.Label(root, text=""))
etiqueta.pack()

boton2 = tk.Button(root, text="Botón salir", command=root.quit)
boton2.pack()

root.mainloop()
