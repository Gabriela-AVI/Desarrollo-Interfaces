# PIEDRA - PAPEL - TIJERA (TAREA OPCIONAL)

"""
El usuario juegue a Piedra-Papel-Tijera contra la máquina.  La partida es al mejor de 5 (gana quien alcance 3 puntos).
Los empates no suman ronda. Diseña la disposición de elementos a tu gusto.

Requisitos funcionales
    - Tres elecciones posibles del jugador: Piedra, Papel, Tijera (botones con imágenes).
    - La máquina elige aleatoriamente su jugada.
    - Mostrar la elección de ambos y el resultado de la ronda.
        ( Ej: Jugador 1 elige piedra, jugador 2 elige papel. Piedra gana a papel.)
    - Marcador en pantalla: puntos del jugador y de la máquina.
    - Final de partida cuando alguien llega a 3; mostrar mensaje de victoria/derrota y bloquear las jugadas (opcional).
    - Botones de Iniciar partida / Nuevo juego (Opcionales: reinicia marcador y estado) y Salir.
    - Empates: no suman puntos ni cuentan como ronda válida.

Pistas técnicas
    - Widgets: Frame, Label, Button, (opcional LabelFrame), messagebox.
    - Variables: StringVar, IntVar.
    - Colocación: pack() o grid().
    - Lógica CPU: random.choice(["piedra","papel","tijera"]).

Entregar enlace al repositorio y vídeo de muestra del programa.
Si la tarea está bien, se sumarán 0,2 puntos a la nota final.
"""
import tkinter as tk
import random
from tkinter import messagebox

root = tk.Tk()
root.title("Piedra-Papel-Tijeras_Gabriela.A.V.I")

# Variables del marcador
jugador_puntos = tk.IntVar(value=0)
maquina_puntos = tk.IntVar(value=0)
resultado_texto = tk.StringVar(value="Elige tu jugada")
eleccion_jugador = tk.StringVar(value="")
eleccion_maquina = tk.StringVar(value="")

# Cargar imágenes
img_piedra = tk.PhotoImage(file="piedra.png").subsample(3, 3)
img_papel = tk.PhotoImage(file="papel.png").subsample(3, 3)
img_tijera = tk.PhotoImage(file="tijera.png").subsample(5, 5)

# Funciones
def reiniciar():
    jugador_puntos.set(0)
    maquina_puntos.set(0)
    resultado_texto.set("Elige tu jugada")
    eleccion_jugador.set("")
    eleccion_maquina.set("")

def salir():
    root.destroy()

def jugar(eleccion_jugador_str):
    eleccion_maquina_str = random.choice(["piedra", "papel", "tijera"])

    eleccion_jugador.set(f"Jugador eligió: {eleccion_jugador_str}")
    eleccion_maquina.set(f"Máquina eligió: {eleccion_maquina_str}")

    if eleccion_jugador_str == eleccion_maquina_str:
        resultado_texto.set(f"Empate de {eleccion_jugador_str}.")
        return

    if (
        (eleccion_jugador_str == "piedra" and eleccion_maquina_str == "tijera") or
        (eleccion_jugador_str == "tijera" and eleccion_maquina_str == "papel") or
        (eleccion_jugador_str == "papel" and eleccion_maquina_str == "piedra")
    ):
        jugador_puntos.set(jugador_puntos.get() + 1)
        resultado_texto.set(f"Ganaste la ronda: ({eleccion_jugador_str} vence a {eleccion_maquina_str})")
    else:
        maquina_puntos.set(maquina_puntos.get() + 1)
        resultado_texto.set(f"Perdiste la ronda: ({eleccion_maquina_str} vence a {eleccion_jugador_str})")

    # Mensaje de ganar/perder
    if jugador_puntos.get() == 3 or maquina_puntos.get() == 3:
        if jugador_puntos.get() == 3:
            messagebox.showinfo("Partida terminada", "🏆 - VICTORIA - 🏆")
        else:
            messagebox.showinfo("Partida terminada", "💀 - GAME OVER - 💀")
        reiniciar()

# Vista marcador
frame_marcador = tk.Frame(root)
frame_marcador.pack(pady=10)

tk.Label(frame_marcador, text="Jugador:").grid(row=0, column=0)
tk.Label(frame_marcador, textvariable=jugador_puntos).grid(row=0, column=1, padx=10)
tk.Label(frame_marcador, text="Máquina:").grid(row=0, column=2)
tk.Label(frame_marcador, textvariable=maquina_puntos).grid(row=0, column=3, padx=10)

# Resultado por ronda
tk.Label(root, textvariable=resultado_texto, font=("Arial", 12)).pack(pady=10)

# Elecciones escogidas
frame_elecciones = tk.Frame(root)
frame_elecciones.pack(pady=5)
tk.Label(frame_elecciones, textvariable=eleccion_jugador).pack()
tk.Label(frame_elecciones, textvariable=eleccion_maquina).pack()

# Botones con imágenes
frame_botones = tk.Frame(root)
frame_botones.pack(pady=20)

tk.Button(frame_botones, image=img_piedra, command=lambda: jugar("piedra"), borderwidth=0).grid(row=0, column=0, padx=10)
tk.Button(frame_botones, image=img_papel, command=lambda: jugar("papel"), borderwidth=0).grid(row=0, column=1, padx=10)
tk.Button(frame_botones, image=img_tijera, command=lambda: jugar("tijera"), borderwidth=0).grid(row=0, column=2, padx=10)

# Botones final
frame_control = tk.Frame(root)
frame_control.pack(pady=15)

tk.Button(frame_control, text="Nuevo juego", command=reiniciar).grid(row=0, column=0, padx=10)
tk.Button(frame_control, text="Salir", command=salir).grid(row=0, column=1, padx=10)

root.mainloop()