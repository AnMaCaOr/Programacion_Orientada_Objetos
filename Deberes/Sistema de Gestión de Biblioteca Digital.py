class Libro:
    def __init__(self, autor, titulo, categoria, isbn):
        self.info = (autor, titulo)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        autor, titulo = self.info
        return f"{titulo} por {autor}, Categoria: {self.categoria}, ISBN: {self.isbn}"

class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista para gestionar los libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.user_id}, Libros Prestados: {[str(libro) for libro in self.libros_prestados]}"

class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario {isbn: objeto Libro}
        self.usuarios = {}  # Diccionario {user_id: objeto Usuario}
        self.user_ids = set()  # Conjunto para asegurar IDs únicos

    def anadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro añadido: {libro}")
        else:
            print("Libro ya existe en el sistema.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.user_ids:
            self.usuarios[usuario.user_id] = usuario
            self.user_ids.add(usuario.user_id)
            print(f"Usuario registrado: {usuario}")
        else:
            print("ID de usuario ya existe.")

    def dar_baja_usuario(self, user_id):
        if user_id in self.user_ids:
            del self.usuarios[user_id]
            self.user_ids.remove(user_id)
            print(f"Usuario con ID {user_id} dado de baja.")
        else:
            print("Usuario no encontrado.")

    def prestar_libro(self, isbn, user_id):
        if isbn in self.libros and user_id in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[user_id]
            usuario.libros_prestados.append(libro)
            print(f"Libro '{libro}' prestado a {usuario.nombre}.")
        else:
            print("Libro o usuario no encontrado.")

    def devolver_libro(self, isbn, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            libro = next((l for l in usuario.libros_prestados if l.isbn == isbn), None)
            if libro:
                usuario.libros_prestados.remove(libro)
                print(f"Libro '{libro}' devuelto.")
            else:
                print("Libro no encontrado en los prestados del usuario.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        encontrados = []
        for libro in self.libros.values():
            if getattr(libro, criterio, '') == valor:
                encontrados.append(libro)
        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontraron libros con ese criterio.")

# Ejemplo de Uso
biblioteca = Biblioteca()

# Creando y añadiendo libros
libro1 = Libro("Gabriel García Márquez", "Cien Años de Soledad", "Novela", "978-3-16-148410-0")
libro2 = Libro("J.K. Rowling", "Harry Potter y la piedra filosofal", "Fantasía", "978-3-16-148411-7")
biblioteca.anadir_libro(libro1)
biblioteca.anadir_libro(libro2)

# Registrando usuarios
usuario1 = Usuario("Angel Cabrera", 1)
usuario2 = Usuario("Aylín Cabrera", 2)
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar y devolver libros
biblioteca.prestar_libro("978-3-16-148410-0", 1)
biblioteca.devolver_libro("978-3-16-148410-0", 1)

# Buscar libros
biblioteca.buscar_libro('categoria', 'Novela')