# Clases Usuario y GestorUsuarios (lógica y datos)

class Usuario:
    def __init__(self, nombre: str, edad: int, genero: str, avatar: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar  # Ruta relativa en assets/

class GestorUsuarios:
    def __init__(self):
        self._usuarios = []  # Lista guardar Usuario

    def listar(self):
        return list(self._usuarios)

    def añadir(self, usuario: Usuario):
        self._usuarios.append(usuario)

    def eliminar(self, indice: int):
        ...

    def actualizar(self, indice: int, usuario_actualizado: Usuario):
        ...

    def guardar_csv(self, ruta: str = "usuarios.csv"):
        ...

    def cargar_csv(self, ruta: str = "usuarios.csv"):
        ...
