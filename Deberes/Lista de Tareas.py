import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        # Lista de tareas
        self.task_list = []

        # Frame para entrada de nueva tarea
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.entry_frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=5)
        self.task_entry.bind('<Return>', self.add_task_event)

        self.add_button = tk.Button(self.entry_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        # Listbox para mostrar las tareas
        self.task_listbox = tk.Listbox(self.root, width=50, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)
        self.task_listbox.bind('<Double-Button-1>', self.mark_task_completed)

        # Frame para botones de control
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.complete_button = tk.Button(self.button_frame, text="Marcar como Completada", command=self.mark_task_completed)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

    def add_task_event(self, event):
        self.add_task()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía")

    def mark_task_completed(self, event=None):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_list[selected_index]
            completed_task = f"{task} ✔️"
            self.task_list[selected_index] = completed_task
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(selected_index, completed_task)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para marcarla como completada")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_list.pop(selected_index)
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para eliminar")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()