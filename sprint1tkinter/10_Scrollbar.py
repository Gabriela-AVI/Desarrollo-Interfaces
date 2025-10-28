
#Ejercicio 10: Scrollbar

"""
Crea un Text con un texto largo (varios párrafos) y añade una barra de desplazamiento vertical (Scrollbar).
* Recuerda conectar ambos widgets con scrollcommand y command:
    scroll.config(command=texto.yview) y texto.config(yscrollcommand=scroll.set).
"""

import tkinter as tk

def insertar_texto():
    for i in range(1,101):
        cuadro_texto.insert(tk.END, f"Línea {i}\n")

    cuadro_texto.insert(tk.END, f"")
    cuadro_texto.insert(tk.END, f"")

root = tk.Tk()
root.title("10_Scrollbar_Gabriela.A.V.I")
root.geometry("400x500")

#Crear Frame para contener Text y la Scrollbar
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Líneas permiten que los widgets se expandan correctamente
frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)

#Crear el Text
cuadro_texto = tk.Text(frame, wrap="none")
cuadro_texto.grid(row=0, column=0, sticky="nsew")

#Crear Scrollbar vertical
scroll_vertical = tk.Scrollbar(frame, orient="vertical",command=cuadro_texto.yview)
scroll_vertical.grid(row=0, column=1, sticky="ns")
cuadro_texto.config(yscrollcommand=scroll_vertical.set)

#Insertar texto
insertar_texto()

root.mainloop()
