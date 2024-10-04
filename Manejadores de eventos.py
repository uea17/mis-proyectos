import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, END, StringVar

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")

        # Variable para almacenar la nueva tarea
        self.task_var = StringVar()

        # Frame para la entrada de tareas y botones
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(frame, textvariable=self.task_var, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        # Botón para añadir tarea
        add_task_btn = tk.Button(frame, text="Añadir Tarea", command=self.add_task)
        add_task_btn.pack(side=tk.LEFT)

        # Listbox para mostrar las tareas
        self.task_listbox = Listbox(self.root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Scrollbar para el Listbox
        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # Botones para completar y eliminar tareas
        complete_task_btn = tk.Button(self.root, text="Marcar como Completada", command=self.complete_task)
        complete_task_btn.pack(pady=5)

        delete_task_btn = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        delete_task_btn.pack(pady=5)

        # Atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())  # Enter para añadir tarea
        self.root.bind('<c>', lambda event: self.complete_task())  # C para completar tarea
        self.root.bind('<Delete>', lambda event: self.delete_task())  # Delete para eliminar tarea
        self.root.bind('<Escape>', lambda event: self.root.quit())  # Escape para cerrar la aplicación

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.task_listbox.insert(END, task)
            self.task_var.set("")  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese una tarea.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(selected_index, f"{task} - Completada")
            self.task_listbox.itemconfig(selected_index, {'fg': 'gray'})  # Cambiar color a gris
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea para completar.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor seleccione una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
