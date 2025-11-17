# Orquesta modelo y vista (callbacks, validaciones)

from model.usuario_model import Usuario, GestorUsuarios
from view.main_view import MainView
from view.add_user_view import AddUserView

import customtkinter as ctk
from PIL import Image
from pathlib import Path

import threading
import time

class AppController:
    def __init__(self, root):
        self.model = GestorUsuarios()
        self.view = MainView(root)

        self.BASE_DIR = Path(__file__).resolve().parent.parent

        # Referencia de imagen derecha
        self.avatar_preview = None

        # Auto-guardado
        self.autosave_running = False
        self.autosave_thread = None

        # Enganchar eventos
        self.view.btn_añadir.configure(command=self.abrir_modal_añadir)
        self.view.btn_eliminar.configure(command=self.eliminar_usuario)
        self.view.btn_autosave.configure(command=self.toggle_autosave) #auto-guardado

        # Mostrar detalles al hacer clic
        self.view.lista.bind("<ButtonRelease-1>", self.mostrar_detalle)

        # Editar usuario
        self.view.lista.bind("<Double-Button-1>", self.abrir_modal_editar)

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

        # Recuento barra de estado
        self.set_status(f"{len(usuarios_filtrados)} usuarios visibles.")

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
            img = Image.open(ruta).resize((300, 300))
            self.avatar_preview = ctk.CTkImage( light_image=img, dark_image=img, size=(200, 200))
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

    # Actualizar barra de estado
    def set_status(self, msg: str):
        self.view.status_bar.configure(text=msg)

    # CSV
    def guardar_csv_controller(self):
        if self.model.guardar_csv():
            self.set_status("Guardado correctamente.") #barra estado
        else:
            self.set_status("Error al guardar CSV.") #barra estado

    def cargar_csv_controller(self):
        if self.model.cargar_csv():
            self.set_status("CSV cargado correctamente.") #barra estado
            self.actualizar_lista()
        else:
            self.set_status("Error al cargar CSV.") #barra estado


    # Eliminar
    def eliminar_usuario(self):
        # Obtener la línea seleccionada en la lista
        linea = self.view.lista.get("insert linestart", "insert lineend")
        index_str = linea.split(".")[0]

        if not index_str.isdigit():
            self.set_status("No hay usuario seleccionado.")
            return

        indice_filtrado = int(index_str)

        # Obtener la lista filtrada (no la completa)
        usuarios_filtrados = self.filtrar_usuarios()

        if not (0 <= indice_filtrado < len(usuarios_filtrados)):
            self.set_status("Selección inválida.")
            return

        # Usuario que realmente queremos borrar
        usuario_objetivo = usuarios_filtrados[indice_filtrado]

        # Buscar su índice real en la lista completa
        usuarios_completos = self.model.listar()
        indice_real = usuarios_completos.index(usuario_objetivo)

        # Eliminar en el modelo
        self.model.eliminar(indice_real)

        # Actualizar UI
        self.actualizar_lista()
        self.set_status("Usuario eliminado correctamente.")


    def abrir_modal_editar(self, event=None):
        # Obtener usuario seleccionado
        linea = self.view.lista.get("insert linestart", "insert lineend")
        index_str = linea.split(".")[0]
        if not index_str.isdigit():
            return

        indice = int(index_str)
        usuarios = self.filtrar_usuarios()
        if indice < 0 or indice >= len(usuarios):
            return

        usuario = usuarios[indice]

        # Crear ventana modal
        modal = AddUserView(self.view.root)

        # --- Precargar datos ---
        modal.var_nombre.set(usuario.nombre)
        modal.var_edad.set(usuario.edad)
        modal.var_genero.set(usuario.genero)
        modal.var_avatar.set(usuario.avatar)
        modal._previsualizar_avatar()

        # Cambiar texto botón guardar
        modal.btn_guardar.configure(text="Actualizar")

        # Conectar acción actualizar
        modal.btn_guardar.configure(
            command=lambda: self.actualizar_usuario(indice, modal)
        )

    def actualizar_usuario(self, indice, modal):
        nombre = modal.var_nombre.get().strip()
        edad = modal.var_edad.get()
        genero = modal.var_genero.get()
        avatar_file = modal.var_avatar.get()

        if not nombre or not (0 <= edad <= 100):
            self.set_status("Datos inválidos.")
            return

        # Creamos usuario actualizado
        usuario_actualizado = Usuario(nombre, edad, genero, avatar_file)

        # Actualizar en el modelo
        self.model.actualizar(indice, usuario_actualizado)

        # Actualizar interfaz
        self.actualizar_lista()
        self.set_status("Usuario actualizado correctamente.")

        modal.destroy()

    # Auto-guardado
    def toggle_autosave(self):
        # Apagado a encendido
        if not self.autosave_running:
            self.autosave_running = True
            self.view.btn_autosave.configure(text="Auto-Guardar: ON")
            self.start_autosave_thread()
            self.set_status("Auto-guardado activado.")

        # Encendido a apagado
        else:
            self.autosave_running = False
            self.view.btn_autosave.configure(text="Auto-Guardar: OFF")
            self.set_status("Auto-guardado detenido.")

    # Auto-guardado
    def start_autosave_thread(self):
        def autosave_loop():
            while self.autosave_running:
                time.sleep(10)  # Esperar 10seg

                # Guardar CSV
                self.model.guardar_csv()

                # Actualizar barra de estado (main_view)
                self.view.root.after(
                    0,
                    lambda: self.set_status("Auto-guardado OK.")
                )

        # Crear hilo
        self.autosave_thread = threading.Thread(target=autosave_loop, daemon=True)
        self.autosave_thread.start()

    def detener_autosave(self):
        self.autosave_running = False
