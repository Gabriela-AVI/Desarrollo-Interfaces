# view/main_view.py
from tkinter import Menu

import customtkinter as ctk

class MainView:
    def __init__(self, root):
        self.root = root

    # Menu
        menubar = Menu(root)
        root.config(menu=menubar)

        # Menú Archivo
        menu_archivo = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)
        # Menú Ayuda
        menu_ayuda = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)

        # Menu Opciones Archivo (Guardar, Cargar, Salir)
        menu_archivo.add_command(label="Guardar")
        menu_archivo.add_command(label="Cargar")
        menu_archivo.add_separator() #Sepador
        menu_archivo.add_command(label="Salir", command=root.destroy)

        self.menu_archivo = menu_archivo

    # Frame inicio
        self.frame = ctk.CTkFrame(root)
        self.frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Parte superior frame (Buscar, Genero, Botones)
        self.top_frame = ctk.CTkFrame(self.frame)
        self.top_frame.pack(fill="x", pady="10")

            # Buscar
        ctk.CTkLabel(self.top_frame, text="Buscar:").pack(side="left", padx=5)

        self.var_buscar = ctk.StringVar()  # Para el trace_add
        self.entry_buscar = ctk.CTkEntry(self.top_frame, width=180, textvariable=self.var_buscar)
        self.entry_buscar.pack(side="left", padx=5)

            # Genero
        ctk.CTkLabel(self.top_frame, text="Género:").pack(side="left", padx=5)
        self.genero_menu = ctk.CTkOptionMenu(
            self.top_frame,
            values=["todos", "Femenino", "Masculino", "Otro"],
            command=self.on_genero_change
        )
        self.genero_menu.pack(side="left")

            # Botones (Añadir, Eliminar)
        self.btn_añadir = ctk.CTkButton(self.top_frame, text="Añadir", width=150)
        self.btn_añadir.pack(side="right", padx=5)
        self.btn_eliminar = ctk.CTkButton(self.top_frame, text="Eliminar", width=150)
        self.btn_eliminar.pack(side="right", padx=10)

    # Parte principal frame
        self.frame_principal = ctk.CTkFrame(self.frame)
        self.frame_principal.pack(fill="both", expand=True, pady=5)

        # Lista de usuarios
        lista_frame = ctk.CTkFrame(self.frame_principal)
        lista_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        self.scrollbar = ctk.CTkScrollbar(lista_frame)
        self.scrollbar.pack(side="right", fill="y")

        self.lista = ctk.CTkTextbox(lista_frame, width=100, yscrollcommand=self.scrollbar.set)
        self.lista.pack(side="left", fill="both", expand=True)

        self.panel = ctk.CTkFrame(self.frame_principal)
        self.panel.pack(side="left", fill="both", expand=True, padx=10, pady=5)

        self.label_avatar = ctk.CTkLabel(self.panel, text="(avatar)")
        self.label_avatar.pack(pady=10)

        self.label_nombre = ctk.CTkLabel(self.panel, text="Nombre: -", anchor="w", justify="left")
        self.label_nombre.pack(pady=5, fill="x", padx=10)

        self.label_edad = ctk.CTkLabel(self.panel, text="Edad: -", anchor="w", justify="left")
        self.label_edad.pack(pady=5, fill="x", padx=10)

        self.label_genero = ctk.CTkLabel(self.panel, text="Género: -", anchor="w", justify="left")
        self.label_genero.pack(pady=5, fill="x", padx=10)

    def on_genero_change(self, value):
        pass
