
# Ejercicio 14: Aplicación con clases

"""
Reescribe la Aplicación de Registro de Usuarios (Ejercicio 12) empleando una clase RegistroApp.
La clase debe:
    1. Definirse como class RegistroApp:.
    2. Crear todos los widgets dentro del metodo __init__(self, root).
    3. Definir métodos para las acciones:
        • añadir_usuario(self)
        • eliminar_usuario(self)
        • salir(self)
    4. Crear la instancia
"""

import tkinter as tk
from tkinter import messagebox

class RegistroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("14_AplicacionClases_Gabriela.A.V.I")

        # 1. Nombre
        tk.Label(root, text="NOMBRE:").grid(row=0, column=0)
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=0, column=1)

        # 2. Edad
        tk.Label(root, text="EDAD:").grid(row=1, column=0)
        self.scale_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
        self.scale_edad.grid(row=1, column=1)

        # 3. Género
        tk.Label(root, text="GÉNERO:").grid(row=2, column=0)
        self.var_genero = tk.StringVar(value="otro")
        tk.Radiobutton(root, text="Masculino", variable=self.var_genero, value="masculino").grid(column=1, row=3, padx=20)
        tk.Radiobutton(root, text="Femenino", variable=self.var_genero, value="femenino").grid(column=1, row=4, padx=20)
        tk.Radiobutton(root, text="Otro", variable=self.var_genero, value="otro").grid(column=1, row=5, padx=20)

        # 4. Botón Añadir
        tk.Button(root, text="Añadir", command=self.añadir_usuario).grid(row=6, columnspan=2, pady=10)

        # 5. Listbox con Scrollbar
        self.lista = tk.Listbox(root, width=40)
        self.scroll = tk.Scrollbar(root, command=self.lista.yview)
        self.lista.config(yscrollcommand=self.scroll.set)
        self.lista.grid(row=7, column=0, columnspan=2)
        self.scroll.grid(row=7, column=2, sticky="ns")

        # 6. Botón Eliminar
        tk.Button(root, text="Eliminar", command=self.eliminar_usuario).grid(row=8, column=0)

        # 7. Botón Salir
        tk.Button(root, text="Salir", command=self.salir).grid(row=8, column=1, pady=20)

        # 8. Menú
        self.menu_ventana = tk.Menu(root)
        root.config(menu=self.menu_ventana)
        menu = tk.Menu(self.menu_ventana, tearoff=0)
        self.menu_ventana.add_cascade(label="Menú", menu=menu)
        menu.add_command(label="Guardar Lista", command=self.guardar_lista)
        menu.add_command(label="Cargar Lista", command=self.cargar_lista)

    # Métodos
    def añadir_usuario(self):
        nombre = self.entry_nombre.get()
        edad = self.scale_edad.get()
        genero = self.var_genero.get()
        if nombre:
            self.lista.insert(tk.END, f"{nombre} - {edad} - {genero}")
            self.entry_nombre.delete(0, tk.END)

    def eliminar_usuario(self):
        seleccionado = self.lista.curselection()
        if seleccionado:
            self.lista.delete(seleccionado)

    def guardar_lista(self):
        messagebox.showinfo("Guardar", "MENSAJE (Guardar lista)")

    def cargar_lista(self):
        messagebox.showinfo("Cargar", "MENSAJE (Cargar lista)")

    def salir(self):
        self.root.quit()

if __name__ == '__main__':
    # Crear la instancia
    root = tk.Tk()
    app = RegistroApp(root)
    root.mainloop()