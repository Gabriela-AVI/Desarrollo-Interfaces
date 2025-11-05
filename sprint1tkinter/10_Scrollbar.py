
# Ejercicio 10: Scrollbar

"""
Crea un Text con un texto largo(2 párrafos) y añade una barra de desplazamiento vertical (Scrollbar).
* Recuerda conectar ambos widgets con scrollcommand y command:
    scroll.config(command=texto.yview) y texto.config(yscrollcommand=scroll.set).
"""

import tkinter as tk

def insertar_texto():
    parrafo1 = """Este ejemplo muestra la estructura básica de una aplicación en Tkinter: cómo crear la ventana principal, añadir widgets y responder a acciones del usuario. Un programa en Tkinter suele tener siempre las siguientes partes:"""

    parrafo2 = """1. Importación de la librería: import tkinter as tk
2. Definición de funciones o clases que controlan el comportamiento de la interfaz.
3. Creación de la ventana principal: root = tk.Tk()
4. Creación y colocación de widgets.
5. Ejecución del bucle principal: root.mainloop()

Es recomendable definir las funciones antes de crear los widgets que las usan, y mantener el código organizado agrupando la creación de la interfaz dentro de funciones o clases."""

    texto.insert(tk.END, parrafo1 + "\n\n" + parrafo2)


root = tk.Tk()
root.title("10_Scrollbar_Gabriela.A.V.I")
root.geometry("300x300")

# Crear Frame para contener el Text y la Scrollbar
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Widgets internos crezcan al redimensionar la ventana
frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)

# Crear el widget Text
texto = tk.Text(frame, wrap="word")
texto.pack(expand=True)

# Crear Scrollbar vertical
scroll = tk.Scrollbar(frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# Conectar ambos widgets
texto.config(yscrollcommand=scroll.set)
scroll.config(command=texto.yview)

#Insertar texto
insertar_texto()

root.mainloop()
