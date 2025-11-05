
# Ejercicio 4: Checkbutton

"""Crea una ventana con tres casillas (Checkbutton) que representen aficiones: “Leer”, “Deporte” y “Música”.
Cuando el usuario seleccione o desmarque una casilla, el estado actual de las aficiones seleccionadas debe
mostrarse en una etiqueta. Usa variables de control (IntVar o StringVar) y actualiza la etiqueta en una función
actualizar()."""

import tkinter as tk

def actualizar():
   seleccion1 = var_check1.get()
   seleccion2 = var_check2.get()
   seleccion3 = var_check3.get()
   estado1 = "Seleccionado" if seleccion1 else "No Seleccionado"
   estado2 = "Seleccionado" if seleccion2 else "No Seleccionado"
   estado3 = "Seleccionado" if seleccion3 else "No Seleccionado"
   check1_estado.config(text= f"{estado1}")
   check2_estado.config(text=f"{estado2}")
   check3_estado.config(text=f"{estado3}")

root = tk.Tk()
root.title("04_Checkbutton_Gabriela.A.V.I")
root.geometry("350x250")

etiqueta = tk.Label(root, text="AFICIONES:")
etiqueta.pack()

var_check1 = tk.IntVar()
check1 = tk.Checkbutton(root,text="Leer", variable=var_check1, command=actualizar).pack()
check1_estado = tk.Label(root, text="No Seleccionado")
check1_estado.pack()

var_check2 = tk.IntVar()
check2 = tk.Checkbutton(root,text="Deporte", variable=var_check2, command=actualizar).pack()
check2_estado = tk.Label(root, text="No Seleccionado")
check2_estado.pack()

var_check3 = tk.IntVar()
check3 = tk.Checkbutton(root,text="Música", variable=var_check3, command=actualizar).pack()
check3_estado = tk.Label(root, text="No Seleccionado")
check3_estado.pack()

root.mainloop()