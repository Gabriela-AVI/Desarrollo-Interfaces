# Orquesta modelo y vista (callbacks, validaciones)

from model.usuario_model import Usuario, GestorUsuarios
from view.main_view import MainView
from view.add_user_view import AddUserView

import customtkinter as ctk
from PIL import Image
from pathlib import Path

class AppController:
    def __init__(self, root):
        self.model = GestorUsuarios()
        self.view = MainView(root)

        self.BASE_DIR = Path(__file__).resolve().parent.parent

        # Referencia de imagen derecha
        self.avatar_preview = None

        # Enganchar eventos
        self.view.btn_añadir.configure(command=self.abrir_modal_añadir)
        self.view.btn_eliminar.configure(command=self.eliminar_usuario)

        # Mostrar detalles al hacer clic
        self.view.lista.bind("<ButtonRelease-1>", self.mostrar_detalle)

        # Filtrar por nombre
        self.view.var_buscar.trace_add("write", lambda *args: self.actualizar_lista())

        # Filtrar por género
        self.view.genero_menu.configure(command=lambda _: self.actualizar_lista())

        # Conectar menú Archivo
        archivo_menu = self.view.menu_archivo
        archivo_menu.entryconfig(0, command=self.guardar_csv_controller)  # Guardar CSV
        archivo_menu.entryconfig(1, command=self.cargar_csv_controller)  # Cargar CSV


    # Añadir usuario

    def abrir_modal_añadir(self):
        modal = AddUserView(self.view.root)
        modal.btn_guardar.configure(command=lambda: self.guardar_usuario(modal))


    def guardar_usuario(self, modal):
        nombre = modal.var_nombre.get().strip()
        edad = modal.var_edad.get()
        genero = modal.var_genero.get()
        avatar_file = modal.var_avatar.get()  # "avatar1.png"

        # Validaciones básicas
        if not nombre:
            modal.entry_nombre.configure(border_color="red")
            return

        if not (0 <= edad <= 100):
            return

        # Guardamos nombre del archivo
        nuevo = Usuario(nombre, edad, genero, avatar_file)
        self.model.añadir(nuevo)

        # Actualizamos lista
        self.actualizar_lista()

        modal.destroy()

    def actualizar_lista(self):
        self.view.lista.delete("1.0", "end")
        usuarios_filtrados = self.filtrar_usuarios()
        for i, u in enumerate(usuarios_filtrados):
            self.view.lista.insert("end", f"{i}. {u.nombre}\n")

    def mostrar_detalle(self, event=None):
        linea = self.view.lista.get("insert linestart", "insert lineend")
        index_str = linea.split(".")[0]

        if not index_str.isdigit():
            return

        i = int(index_str)
        usuarios = self.model.listar()

        if i < 0 or i >= len(usuarios):
            return

        u = usuarios[i]

        # Actualizar texto
        self.view.label_nombre.configure(text=f"Nombre: {u.nombre}")
        self.view.label_edad.configure(text=f"Edad: {u.edad}")
        self.view.label_genero.configure(text=f"Género: {u.genero}")

        # Ruta imagen
        ruta = self.BASE_DIR / "assets" / u.avatar

        # Cargar avatar
        if ruta.exists():
            img = Image.open(ruta).resize((160, 160))
            self.avatar_preview = ctk.CTkImage(light_image=img, dark_image=img)
            self.view.label_avatar.configure(image=self.avatar_preview, text="")
        else:
            self.view.label_avatar.configure(text="(avatar no encontrado)", image=None)

    # Filtros
    def filtrar_usuarios(self):
        texto = self.view.var_buscar.get().lower().strip()
        genero_filtro = self.view.genero_menu.get()

        usuarios = self.model.listar()

        # Filtrar por nombre
        if texto:
            usuarios = [u for u in usuarios if texto in u.nombre.lower()]

        # Filtrar por género
        if genero_filtro != "todos":
            usuarios = [u for u in usuarios if u.genero == genero_filtro]

        return usuarios

    # CSV

    def guardar_csv_controller(self):
        if self.model.guardar_csv():
            print("CSV guardado correctamente.")
        else:
            print("Error al guardar CSV.")

    def cargar_csv_controller(self):
        if self.model.cargar_csv():
            print("CSV cargado")
            self.actualizar_lista()
        else:
            print("Error al cargar CSV")

    # Eliminar

    def eliminar_usuario(self):
        pass

