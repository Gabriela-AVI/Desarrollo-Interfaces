# Clases Usuario y GestorUsuarios (lógica y datos)
import csv


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
        # Guardar todos los usuarios
        try:
            with open(ruta, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)

                # Cabecera
                writer.writerow(["nombre", "edad", "genero", "avatar"])

                # Filas (nombre, edad, genero, avatar-file)
                for u in self._usuarios:
                    writer.writerow([u.nombre, u.edad, u.genero, u.avatar])

            return True  #éxito

        except Exception as e:
            print("Error al guardar CSV:", e)
            return False  #fallo

    def cargar_csv(self, ruta: str = "usuarios.csv"):
        # Cargar usuarios desde CSV
        try:
            with open(ruta, "r", encoding="utf-8", newline="") as f:
                reader = csv.reader(f)

                next(reader, None) # Leer cabecera y descartarla

                self._usuarios.clear()  # Vaciar lista actual

                for fila in reader:
                    # Fila válida --> EXACTAMENTE 4 columnas
                    if len(fila) != 4:
                        print("Fila inválida saltada:", fila)
                        continue

                    nombre, edad, genero, avatar = fila

                    # Edad debe ser número
                    try:
                        edad = int(edad)
                    except ValueError:
                        print("Edad inválida en fila:", fila)
                        continue

                    # Crear usuario y añadirlo
                    user = Usuario(nombre, edad, genero, avatar)
                    self._usuarios.append(user)

            return True  # éxito

        except FileNotFoundError:
            print("Archivo no encontrado")
            return False

        except Exception as e:
            print("Error al cargar CSV:", e)
            return False

