
# Ejercicio 12: Aplicación de Registro de Usuarios

"""
Desarrolla una aplicación de registro de usuarios que contenga:
    1. Campo Entry para el nombre.
    2. Scale para la edad (0–100 años).
    3. Tres Radiobutton para el género (masculino, femenino, otro).
    4. Botón “Añadir” para guardar un usuario en una lista.
    5. Listbox con todos los usuarios registrados (nombre, edad y género).
    6. Scrollbar vertical para la lista.
    7. Botón “Eliminar” para borrar el usuario seleccionado.
    8. Botón “Salir” para cerrar la aplicación.
    9. Menú con opciones “Guardar Lista” y “Cargar Lista” que muestren un messagebox.
Puedes empezar construyendo la interfaz paso a paso, probando que cada parte funcione antes de continuar.
"""

import tkinter as tk
from tkinter import messagebox

#1
def añadir_usuario():
    nombre = entry_nombre.get()
    edad = scale_edad.get()
    genero = var_genero.get()

    lista.insert(tk.END, f"{nombre} - {edad} - {genero}")
    entry_nombre.delete(0, tk.END)
#2
def eliminar_usuario():
    seleccionado = lista.curselection()
    lista.delete(seleccionado)
#9
def guardar_lista():
    messagebox.showinfo("Guardar", "MENSAJE (Guardar lista)")
def cargar_lista():
    messagebox.showinfo("Cargar", "MENSAJE (Cargar lista)")

root = tk.Tk()
root.title("12_AplicaciónRegistroUsuarios_Gabriela.A.V.I")

# 1. Nombre
etq_nombre = tk.Label(root, text="NOMBRE:")
etq_nombre.grid(row=0, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)

# 2. Edad
etq_edad = tk.Label(root, text="EDAD:")
etq_edad.grid(row=1, column=0)
scale_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
scale_edad.grid(row=1, column=1)

# 3. Género
etq_genero = tk.Label(root, text="GÉNERO: ")
etq_genero.grid(row=2, column=0)
var_genero = tk.StringVar(value="otro")
opcion_masc = tk.Radiobutton(root, text="Masculino", variable=var_genero, value="masculino")
opcion_masc.grid(column=1, row=3, padx=20)
opcion_femn = tk.Radiobutton(root, text="Femenino", variable=var_genero, value="femenino")
opcion_femn.grid(column=1, row=4, padx=20)
opcion_otro = tk.Radiobutton(root, text="Otro", variable=var_genero, value="otro")
opcion_otro.grid(column=1, row=5, padx=20)

# 4.Botón Añadir
boton_añadir = tk.Button(root, text="Añadir", command=añadir_usuario)
boton_añadir.grid(row=6, columnspan=2, pady=10)

# 5. Listbox
lista = tk.Listbox(root, width=40)
scroll = tk.Scrollbar(root, command=lista.yview)

# 6. Scrollbar
lista.config(yscrollcommand=scroll.set)
lista.grid(row=7, column=0, columnspan=2)
scroll.grid(row=7, column=2, sticky="ns")

# 7. Botón Eliminar
boton_eliminar = tk.Button(root, text="Eliminar", command=eliminar_usuario)
boton_eliminar.grid(row=8, column=0)

# 8. Botón Salir
boton_salir = tk.Button(root, text="Salir", command=root.quit)
boton_salir.grid(row=8, column=1, pady=20)

# 9. Menú
#   Crear barra
menu_ventana = tk.Menu(root)
root.config(menu=menu_ventana)
#   Menú
menu= tk.Menu(menu_ventana, tearoff=0)
menu_ventana.add_cascade(label="Menú",menu=menu)
#  Opciones Menú
menu.add_command(label="Guardar Lista", command=guardar_lista)
menu.add_command(label="Cargar Lista", command=cargar_lista)

root.mainloop()
