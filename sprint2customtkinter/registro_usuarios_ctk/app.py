# Punto de entrada (bootstrap)

import customtkinter as ctk
from controller.app_controller import AppController

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Registro de Usuarios (CTk + MVC)")
    app.geometry("900x600")

    controller = AppController(app)  # crear modelo y vista

    # Deterner autoguardado
    app.protocol(
        "WM_DELETE_WINDOW",
        lambda: (controller.detener_autosave(), app.destroy())
    )

    app.mainloop()
