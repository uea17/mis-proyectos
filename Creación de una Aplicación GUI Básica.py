import tkinter as tk
from tkinter import messagebox, Listbox

# Clase principal de la aplicación
class AplicacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Información")

        # Estilo y configuración
        self.root.configure(bg="#1E90FF")  # Fondo de color azul (#1E90FF)

        # Título de la ventana
        self.label_titulo = tk.Label(root, text="Gestión de Información", font=("Arial", 16, "bold"), bg="#1E90FF", fg="white")
        self.label_titulo.pack(pady=20)

        # Etiqueta
        self.label_instruccion = tk.Label(root, text="Introduce información:", font=("Arial", 12), bg="#1E90FF", fg="white")
        self.label_instruccion.pack(pady=10)

        # Campo de texto
        self.entry_info = tk.Entry(root, font=("Arial", 12), width=30)
        self.entry_info.pack(pady=10)

        # Lista para mostrar datos
        self.lista_info = Listbox(root, font=("Arial", 12), width=40, height=10)
        self.lista_info.pack(pady=10)

        # Botón para agregar información
        self.btn_agregar = tk.Button(root, text="Agregar", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=self.agregar_info)
        self.btn_agregar.pack(pady=10)

        # Botón para limpiar la lista
        self.btn_limpiar = tk.Button(root, text="Limpiar", font=("Arial", 12, "bold"), bg="#f44336", fg="white", command=self.limpiar_lista)
        self.btn_limpiar.pack(pady=10)

    # Función para agregar información
    def agregar_info(self):
        info = self.entry_info.get()
        if info:
            self.lista_info.insert(tk.END, info)  # Inserta la información en la lista
            self.entry_info.delete(0, tk.END)     # Limpia el campo de texto
        else:
            messagebox.showwarning("Advertencia", "El campo está vacío")

    # Función para limpiar la lista
    def limpiar_lista(self):
        self.lista_info.delete(0, tk.END)

# Configuración de la ventana
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()
