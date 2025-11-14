# Orquesta modelo y vista (callbacks, validaciones)


from model.usuario_model import Usuario, GestorUsuarios
from view.main_view import MainView

class AppController:
    def __init__(self, root):
        self.model = GestorUsuarios()
        self.view = MainView(root)
