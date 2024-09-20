import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Clase principal de la aplicación
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Contenedores
        self.create_frames()

        # Componentes
        self.create_widgets()

        # Lista de eventos
        self.events = []

    def create_frames(self):
        # Frame para la lista de eventos
        self.events_frame = ttk.Frame(self.root)
        self.events_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Frame para la entrada de datos
        self.entry_frame = ttk.Frame(self.root)
        self.entry_frame.pack(fill="x", padx=10, pady=5)

        # Frame para los botones
        self.buttons_frame = ttk.Frame(self.root)
        self.buttons_frame.pack(fill="x", padx=10, pady=10)

    def create_widgets(self):
        # Lista de eventos (Treeview)
        self.events_tree = ttk.Treeview(self.events_frame, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.events_tree.heading("Fecha", text="Fecha")
        self.events_tree.heading("Hora", text="Hora")
        self.events_tree.heading("Descripción", text="Descripción")
        self.events_tree.pack(fill="both", expand=True)

        # Scrollbar para la lista de eventos
        self.scrollbar = ttk.Scrollbar(self.events_frame, orient="vertical", command=self.events_tree.yview)
        self.events_tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")

        # Campos de entrada
        ttk.Label(self.entry_frame, text="Fecha (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = ttk.Entry(self.entry_frame)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.entry_frame, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5)
        self.time_entry = ttk.Entry(self.entry_frame)
        self.time_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(self.entry_frame, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.desc_entry = ttk.Entry(self.entry_frame, width=50)
        self.desc_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # Botones
        self.add_button = ttk.Button(self.buttons_frame, text="Agregar Evento", command=self.add_event)
        self.add_button.pack(side="left", padx=5, pady=5)

        self.delete_button = ttk.Button(self.buttons_frame, text="Eliminar Evento Seleccionado", command=self.delete_event)
        self.delete_button.pack(side="left", padx=5, pady=5)

        self.quit_button = ttk.Button(self.buttons_frame, text="Salir", command=self.root.quit)
        self.quit_button.pack(side="right", padx=5, pady=5)

    def add_event(self):
        # Obtener datos de entrada
        date = self.date_entry.get()
        time = self.time_entry.get()
        description = self.desc_entry.get()

        # Validación simple
        if not self.validate_date(date):
            messagebox.showwarning("Fecha Inválida", "Por favor, ingresa una fecha válida en el formato YYYY-MM-DD.")
            return

        if not self.validate_time(time):
            messagebox.showwarning("Hora Inválida", "Por favor, ingresa una hora válida en el formato HH:MM.")
            return

        if not description:
            messagebox.showwarning("Descripción Incompleta", "Por favor, ingresa una descripción para el evento.")
            return

        # Agregar evento al Treeview
        self.events_tree.insert("", "end", values=(date, time, description))

        # Limpiar entradas
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def delete_event(self):
        selected_item = self.events_tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmar Eliminación", "¿Estás seguro de que deseas eliminar este evento?")
            if confirm:
                # Eliminar el evento seleccionado del Treeview
                self.events_tree.delete(selected_item)
        else:
            messagebox.showwarning("Sin Selección", "Por favor, selecciona un evento para eliminar.")

    def validate_date(self, date_text):
        """Valida que la fecha esté en formato YYYY-MM-DD y sea válida."""
        try:
            datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def validate_time(self, time_text):
        """Valida que la hora esté en formato HH:MM y sea válida."""
        try:
            datetime.strptime(time_text, '%H:%M')
            return True
        except ValueError:
            return False

# Inicializar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
