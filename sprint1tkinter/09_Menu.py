# Ejercicio 9: Menu

"""
Crea una barra de menú en la ventana con los siguientes elementos:
    • Menú “Archivo” → opciones “Abrir” y “Salir”.
    • Menú “Ayuda” → opción “Acerca de”.
La opción “Salir” debe cerrar la aplicación, y “Acerca de” debe mostrar un mensaje en una
ventana emergente.
* Usa messagebox.showinfo("Acerca de", "texto") para mostrar el cuadro de diálogo.
"""

import tkinter as tk
from tkinter import messagebox

def abrir_ventana():
    messagebox.showinfo("Archivo", "MENSAJE (Abrir)")

def mostrar_ayuda():
    messagebox.showinfo("Ayuda", " MENSAJE (Acerca de) ")

root = tk.Tk()
root.title("09_Menu_Gabriela.A.V.I")
root.geometry("300x300")

#Crear barra menú
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

#Crear un submenú "Archivo"
menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo",menu=menu_archivo)

menu_archivo.add_command(label="Abrir", command=abrir_ventana)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)

#Crear un submenú "Ayuda"
menu_ayuda = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Ayuda",menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=mostrar_ayuda)

root.mainloop()
