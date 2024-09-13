import tkinter as tk
from tkinter import messagebox

# Funciones para manejar eventos
def agregar_dato():
    dato = entry_dato.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entry_dato.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa un dato.")

def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Interacción con Datos")

# Etiqueta
label_instruccion = tk.Label(ventana, text="Ingresa un dato:")
label_instruccion.pack(pady=5)

# Campo de texto
entry_dato = tk.Entry(ventana, width=40)
entry_dato.pack(pady=5)

# Botón para agregar datos
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar datos
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=10)

# Botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Inicia el bucle principal de la aplicación
ventana.mainloop()
