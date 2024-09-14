import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada_dato.get()
    if dato:  # Verificar que el campo no esté vacío
        lista_datos.insert(tk.END, dato)
        entrada_dato.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "El campo no puede estar vacío.")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Etiqueta para el campo de texto
etiqueta = tk.Label(ventana, text="Ingrese el dato:")
etiqueta.pack(pady=10)

# Campo de texto para ingresar datos
entrada_dato = tk.Entry(ventana, width=40)
entrada_dato.pack(pady=5)

# Botón para agregar el dato a la lista
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar los datos agregados
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=10)

# Botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
