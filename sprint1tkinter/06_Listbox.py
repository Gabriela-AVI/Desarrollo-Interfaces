
# EJERCICIO 6

""" Crea una lista (Listbox) con varias frutas: “Manzana”, “Banana”, “Naranja”.
Al seleccionar una fruta y pulsar un botón, muestra el nombre de la fruta seleccionada en
una etiqueta.
Usa curselection() y get() para obtener el elemento activo."""

import tkinter as tk

def mostrar_seleccion():
    seleccion = listbox.curselection()
    elemento = [listbox.get(i) for i in seleccion]
    etiqueta.config(text=f"Seleccionaste: {' '.join(elemento)}")

#   OTRA OPCIÓN:
#    seleccion = listbox.curselection()
#    if seleccion:
#        fruta = listbox.get(seleccion)
#        etiqueta.config(root, text=f"Seleccionaste: {fruta}")
#    else:
#        etiqueta.config(root, text=f"Seleccionaste: Ninguno")

root = tk.Tk()
root.title("06_Listbox_Gabriela.A.V.I")
root.geometry("300x300")

etiqueta = tk.Label(root, text="FRUTAS:")
etiqueta.pack()

#Crear lista opciones
lista_frutas = ["Manzana", "Banana", "Naranja"]

#Crear Listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
for fruta in lista_frutas:
    listbox.insert(tk.END, fruta)
listbox.pack(pady=10)

#Botón mostrat seleción
boton = tk.Button(root, text="Mostrar Selección", command=mostrar_seleccion)
boton.pack()

etiqueta = tk.Label(root, text="Seleccionaste: Ninguno")
etiqueta.pack()

root.mainloop()