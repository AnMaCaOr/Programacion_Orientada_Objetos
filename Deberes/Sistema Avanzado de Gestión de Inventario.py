class Producto:
    """
    Clase Producto que representa cada artículo en el inventario.
    Atributos:
        id (str): Identificador único del producto.
        nombre (str): Nombre del producto.
        cantidad (int): Cantidad disponible del producto.
        precio (float): Precio unitario del producto.
    """
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Inventario:
    """
    Clase Inventario para manejar las operaciones del inventario.
    Atributos:
        productos (dict): Diccionario que almacena los objetos Producto, usando el ID como clave.
    """
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)

    def buscar_producto(self, nombre_producto):
        for producto in self.productos.values():
            if producto.get_nombre().lower() == nombre_producto.lower():
                return producto
        return None

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, filename):
        with open(filename, 'w') as file:
            for producto in self.productos.values():
                file.write(f"{producto.get_id()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio()}\n")

    def cargar_inventario(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    id, nombre, cantidad, precio = line.strip().split(',')
                    self.agregar_producto(Producto(id, nombre, int(cantidad), float(precio)))
        except FileNotFoundError:
            print("Archivo no encontrado, iniciando con inventario vacío.")


def menu():
    """
    Función que implementa el menú interactivo para manejar el inventario desde la consola.
    """
    inventario = Inventario()
    inventario.cargar_inventario("inventario.txt")

    while True:
        print("\n1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Guardar y Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            inventario.agregar_producto(Producto(id, nombre, cantidad, precio))
        elif opcion == '2':
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == '3':
            id = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            producto = inventario.buscar_producto(nombre)
            if producto:
                print(producto)
            else:
                print("Producto no encontrado.")
        elif opcion == '5':
            inventario.mostrar_productos()
        elif opcion == '6':
            inventario.guardar_inventario("inventario.txt")
            print("Inventario guardado. Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

menu()