
# EJERCICIO 7: Canvas

"""
Crea un Canvas y dibuja en él un círculo y un rectángulo.
El tamaño y las posiciones deben ser definidas por el usuario mediante campos Entry.
Ejemplo:
Introduce las coordenadas x1, y1, x2, y2 y usa canvas.create_rectangle(x1, y1, x2, y2).
"""

import tkinter as tk

def dibujar():

    rx1 = int(entry_rx1.get())
    ry1 = int(entry_ry1.get())
    rx2 = int(entry_rx2.get())
    ry2 = int(entry_ry2.get())

    cx1_val = int(entry_cx1.get())
    cy1_val = int(entry_cy1.get())
    cx2_val = int(entry_cx2.get())
    cy2_val = int(entry_cy2.get())

    canvas.delete("all")

    canvas.create_rectangle(rx1, ry1, rx2, ry2, outline="blue", width=2)
    canvas.create_oval(cx1_val, cy1_val, cx2_val, cy2_val, outline="red", width=2)

root = tk.Tk()
root.title("07_Canvas_Gabriela.A.V.I")
root.geometry("600x600")

# Organicé la estructura con Frame (ejercicio 8)
frame1 = tk.Frame(root, relief="sunken", borderwidth=1)
frame1.pack(padx=10, pady=10)

frame2 = tk.Frame(root)
frame2.pack(padx=10, pady=10)

#Introducir medidas Canvas (organizada la estructura con Frame)
#RECTÁNGULO
pregunta= tk.Label(frame1, text="RECTÁNGULO")
pregunta.grid(row=0, column=0, padx=5, pady=5)

rx1 = tk.Label(frame1, text="x1:")
rx1.grid(row=1, column=0, padx=5, pady=5)
entry_rx1 = tk.Entry(frame1)
entry_rx1.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

ry1 = tk.Label(frame1, text="y1:")
ry1.grid(row=2, column=0, padx=5, pady=5)
entry_ry1 = tk.Entry(frame1)
entry_ry1.grid(row=2, column=1, padx=5, pady=5, columnspan=2, )

rx2 = tk.Label(frame1, text="x2:")
rx2.grid(row=3, column=0, padx=5, pady=5)
entry_rx2 = tk.Entry(frame1)
entry_rx2.grid(row=3, column=1, padx=5, pady=5)

ry2 = tk.Label(frame1, text="y2:")
ry2.grid(row=4, column=0, padx=5, pady=5)
entry_ry2 = tk.Entry(frame1)
entry_ry2.grid(row=4, column=1, padx=5, pady=5)

#CÍRCULO
pregunta= tk.Label(frame1, text="CÍRCULO")
pregunta.grid(row=0, column=3, padx=5, pady=5)

cx1 = tk.Label(frame1, text="x1:")
cx1.grid(row=1, column=2, padx=10, pady=10, columnspan=2)
entry_cx1 = tk.Entry(frame1)
entry_cx1.grid(row=1, column=4, padx=5, pady=5)

cy1 = tk.Label(frame1, text="y1:")
cy1.grid(row=2, column=2, padx=10, pady=10, columnspan=2)
entry_cy1 = tk.Entry(frame1)
entry_cy1.grid(row=2, column=4, padx=5, pady=5)

cx2 = tk.Label(frame1, text="x2:")
cx2.grid(row=3, column=2, padx=10, pady=10, columnspan=2)
entry_cx2 = tk.Entry(frame1)
entry_cx2.grid(row=3, column=4, padx=5, pady=5)

cy2 = tk.Label(frame1, text="y2:")
cy2.grid(row=4, column=2, padx=10, pady=10, columnspan=2)
entry_cy2 = tk.Entry(frame1)
entry_cy2.grid(row=4, column=4, padx=5, pady=5)

boton = tk.Button(frame2, text="Dibujar", command=dibujar).pack(padx=10, pady=10)
#Crear Canvas base
canvas = tk.Canvas(frame2, width=300, height=300, background="white")
canvas.pack(padx=10, pady=10)

root.mainloop()