import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry  # Necesario para el DatePicker (selección de fecha)

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Frame para la visualización de eventos
        self.frame_eventos = ttk.Frame(self.root)
        self.frame_eventos.pack(pady=20)

        # Creación del TreeView para mostrar eventos
        self.tree = ttk.Treeview(self.frame_eventos, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para entradas (fecha, hora, descripción)
        self.frame_inputs = ttk.Frame(self.root)
        self.frame_inputs.pack(pady=10)

        # Etiqueta y entrada de Fecha
        ttk.Label(self.frame_inputs, text="Fecha:").grid(row=0, column=0, padx=5)
        self.entry_fecha = DateEntry(self.frame_inputs)  # DateEntry para seleccionar la fecha
        self.entry_fecha.grid(row=0, column=1, padx=5)

        # Etiqueta y entrada de Hora
        ttk.Label(self.frame_inputs, text="Hora:").grid(row=1, column=0, padx=5)
        self.entry_hora = ttk.Entry(self.frame_inputs)
        self.entry_hora.grid(row=1, column=1, padx=5)

        # Etiqueta y entrada de Descripción
        ttk.Label(self.frame_inputs, text="Descripción:").grid(row=2, column=0, padx=5)
        self.entry_desc = ttk.Entry(self.frame_inputs)
        self.entry_desc.grid(row=2, column=1, padx=5)

        # Frame para los botones
        self.frame_botones = ttk.Frame(self.root)
        self.frame_botones.pack(pady=10)

        # Botón para agregar evento
        self.btn_agregar = ttk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.grid(row=0, column=0, padx=10)

        # Botón para eliminar evento seleccionado
        self.btn_eliminar = ttk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.btn_eliminar.grid(row=0, column=1, padx=10)

        # Botón para salir de la aplicación
        self.btn_salir = ttk.Button(self.frame_botones, text="Salir", command=self.root.quit)
        self.btn_salir.grid(row=0, column=2, padx=10)

    # Método para agregar evento
    def agregar_evento(self):
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        desc = self.entry_desc.get()

        # Verificación de campos vacíos
        if fecha and hora and desc:
            self.tree.insert("", "end", values=(fecha, hora, desc))
            self.limpiar_campos()
        else:
            messagebox.showwarning("Entrada inválida", "Por favor, completa todos los campos.")

    # Método para eliminar evento seleccionado
    def eliminar_evento(self):
        selected_item = self.tree.selection()  # Obtener el evento seleccionado
        if selected_item:
            self.tree.delete(selected_item)  # Eliminar el evento
        else:
            messagebox.showwarning("Sin selección", "Selecciona un evento para eliminar.")

    # Método para limpiar los campos de entrada después de agregar evento
    def limpiar_campos(self):
        self.entry_fecha.set_date("")  # Limpiar fecha
        self.entry_hora.delete(0, tk.END)  # Limpiar hora
        self.entry_desc.delete(0, tk.END)  # Limpiar descripción

# Ejecución de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
