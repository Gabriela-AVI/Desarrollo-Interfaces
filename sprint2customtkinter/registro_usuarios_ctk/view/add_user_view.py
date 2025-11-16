import customtkinter as ctk
from PIL import Image
from pathlib import Path


class AddUserView(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Añadir usuario")
        self.geometry("350x560")
        self.resizable(False, False)

        # BASE_DIR
        BASE_DIR = Path(__file__).resolve().parent.parent

        # VARIABLES
        self.var_nombre = ctk.StringVar()
        self.var_edad = ctk.IntVar(value=18)
        self.var_genero = ctk.StringVar(value="Masculino")
        self.var_avatar = ctk.StringVar(value="avatar1.png")

        # NOMBRE
        ctk.CTkLabel(self, text="Nombre:").pack(anchor="w", padx=20)
        self.entry_nombre = ctk.CTkEntry(self, textvariable=self.var_nombre)
        self.entry_nombre.pack(fill="x", padx=20, pady=5)

        # EDAD
        ctk.CTkLabel(self, text="Edad (0-100):").pack(anchor="w", padx=20)
        self.scale_edad = ctk.CTkSlider(self, from_=0, to=100, number_of_steps=100,
                                        variable=self.var_edad)
        self.scale_edad.pack(fill="x", padx=20, pady=5)

        self.label_valor_edad = ctk.CTkLabel(self, text="Edad: 18")
        self.label_valor_edad.pack(pady=5)

        # Actualizar label al mover la escala
        self.scale_edad.configure(command=self._actualizar_label_edad)

        # GENERO
        ctk.CTkLabel(self, text="Género:").pack(anchor="w", padx=20)
        frame_genero = ctk.CTkFrame(self)
        frame_genero.pack(fill="x", padx=20, pady=5)

        generos = ["Masculino", "Femenino", "Otro"]
        for g in generos:
            ctk.CTkRadioButton(frame_genero, text=g,
                               variable=self.var_genero,
                               value=g).pack(anchor="w")

        # AVATAR
        ctk.CTkLabel(self, text="Avatar:").pack(anchor="w", padx=20, pady=(10, 0))
        frame_avatar = ctk.CTkFrame(self)
        frame_avatar.pack(padx=20, pady=5)

        # Rutas ABSOLUTAS usando Path
        self.avatars = {
            "avatar1.png": BASE_DIR / "assets" / "avatar1.png",
            "avatar2.png": BASE_DIR / "assets" / "avatar2.png",
            "avatar3.png": BASE_DIR / "assets" / "avatar3.png",
        }

        # Mantener referencia de imagen
        self.preview_img = None

        # RadioButtons avatar
        for archivo in self.avatars.keys():
            ctk.CTkRadioButton(frame_avatar, text=archivo,
                               variable=self.var_avatar,
                               value=archivo,
                               command=self._previsualizar_avatar).pack(anchor="w")

        # PREVISUALIZACIÓN
        self.label_preview = ctk.CTkLabel(self, text="(previsualización)")
        self.label_preview.pack(pady=10)

        self._previsualizar_avatar()

        # BOTÓN GUARDAR
        self.btn_guardar = ctk.CTkButton(self, text="Guardar")
        self.btn_guardar.pack(pady=15)


    def _previsualizar_avatar(self):
        ruta = self.avatars[self.var_avatar.get()]   # Ahora es un objeto Path
        img = Image.open(ruta)
        img = img.resize((150, 150))

        self.preview_img = ctk.CTkImage(
            light_image=img,
            dark_image=img
        )
        self.label_preview.configure(image=self.preview_img)


    def _actualizar_label_edad(self, value):
        self.label_valor_edad.configure(text=f"Edad: {int(float(value))}")
