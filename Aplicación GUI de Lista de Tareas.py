import tkinter as tk
from tkinter import messagebox

# Función para añadir tarea
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)  # Añadir tarea al Listbox
        task_entry.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Entrada Vacía", "Por favor, escribe una tarea.")

# Función para marcar tarea como completada
def complete_task():
    try:
        selected_index = task_listbox.curselection()[0]  # Obtener índice de la tarea seleccionada
        task = task_listbox.get(selected_index)
        if not task.startswith("[✓]"):
            task_listbox.delete(selected_index)  # Eliminar la tarea
            task_listbox.insert(selected_index, f"[✓] {task}")  # Reinsertar la tarea con marca de completada
    except IndexError:
        messagebox.showwarning("Seleccionar tarea", "Por favor, selecciona una tarea para marcarla como completada.")

# Función para eliminar tarea
def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]  # Obtener índice de la tarea seleccionada
        task_listbox.delete(selected_index)  # Eliminar la tarea seleccionada
    except IndexError:
        messagebox.showwarning("Seleccionar tarea", "Por favor, selecciona una tarea para eliminar.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Campo de entrada de tarea
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)

# Listbox para mostrar las tareas
task_listbox = tk.Listbox(root, height=10, width=50, selectmode=tk.SINGLE)
task_listbox.grid(row=1, column=0, padx=10, pady=10)

# Botón para añadir tarea
add_button = tk.Button(root, text="Añadir Tarea", width=20, command=add_task)
add_button.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

# Botón para marcar tarea como completada
complete_button = tk.Button(root, text="Marcar como Completada", width=20, command=complete_task)
complete_button.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)

# Botón para eliminar tarea
delete_button = tk.Button(root, text="Eliminar Tarea", width=20, command=delete_task)
delete_button.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

# Permitir añadir tarea al presionar Enter
task_entry.bind("<Return>", lambda event: add_task())

# Ejecutar la aplicación
root.mainloop()
