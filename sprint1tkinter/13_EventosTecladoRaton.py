
# Ejercicio 13: Eventos de teclado y ratón (nuevo)

"""
Crea una ventana con un Canvas que dibuje un círculo en la posición donde el usuario
haga clic con el ratón.
Además, si el usuario presiona la tecla “c”, el Canvas debe borrarse.
    • Usa canvas.bind("<Button-1>", funcion) para detectar clics.
    • Obtén las coordenadas con event.x y event.y.
    • Usa canvas.delete("all") para limpiar.
"""

import tkinter as tk

def dibujar(event):
    canvas.create_oval(event.x-10, event.y-10, event.x+10, event.y+10, fill="purple")

def limpiar(event):
    canvas.delete("all")

root = tk.Tk()
root.title("13_EventosTecladoRaton_Gabriela.A.V.I")

#Crear Canvas
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

#Detectar clics
canvas.bind("<Button-1>", dibujar)

#Limpiar canvas
root.bind("<KeyPress-c>", limpiar)

root.mainloop()