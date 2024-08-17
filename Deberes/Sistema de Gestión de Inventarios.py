class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                return "Error: ID ya existe."
        self.productos.append(producto)
        return "Producto agregado correctamente."

    def eliminar_producto(self, id):
        for i, producto in enumerate(self.productos):
            if producto.get_id() == id:
                del self.productos[i]
                return "Producto eliminado correctamente."
        return "Producto no encontrado."

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                return "Producto actualizado correctamente."
        return "Producto no encontrado."

    def buscar_producto(self, nombre):
        resultados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        return self.productos

def main():
    inventario = Inventario()
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar producto por ID")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            print(inventario.agregar_producto(producto))

        elif opcion == "2":
            id = input("Ingrese el ID del producto a eliminar: ")
            print(inventario.eliminar_producto(id))

        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            print(inventario.actualizar_producto(id, cantidad, precio))

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                print("\nProductos encontrados:")
                for producto in resultados:
                    print(
                        f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: ${producto.get_precio()}")
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            productos = inventario.mostrar_productos()
            if productos:
                print("\nListado de todos los productos:")
                for producto in productos:
                    print(
                        f"ID: {producto.get_id()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: ${producto.get_precio()}")
            else:
                print("El inventario está vacío.")

        elif opcion == "6":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

main()