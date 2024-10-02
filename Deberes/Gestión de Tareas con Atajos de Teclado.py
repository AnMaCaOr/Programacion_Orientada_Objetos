import tkinter as tk
from tkinter import messagebox, END


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")

        # Lista de tareas
        self.tasks = []

        # Configuración de la interfaz
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Manejo de atajos de teclado
        self.root.bind("<Return>", self.add_task_event)
        self.root.bind("<c>", self.complete_task_event)
        self.root.bind("<Delete>", self.delete_task_event)
        self.root.bind("<Escape>", self.close_app)

    def add_task(self):
        task_text = self.entry.get()
        if task_text:
            self.tasks.append(task_text)
            self.update_task_list()
            self.entry.delete(0, END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, escribe una tarea.")

    def add_task_event(self, event):
        self.add_task()

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            completed_task = self.tasks[selected_index] + " (Completada)"
            self.tasks[selected_index] = completed_task
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcarla como completada.")

    def complete_task_event(self, event):
        self.complete_task()

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminarla.")

    def delete_task_event(self, event):
        self.delete_task()

    def close_app(self, event):
        self.root.quit()

    def update_task_list(self):
        self.task_listbox.delete(0, END)
        for task in self.tasks:
            self.task_listbox.insert(END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
