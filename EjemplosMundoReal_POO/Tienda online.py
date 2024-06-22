class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"{self.nombre} ({self.email})"

class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad):
        self.items.append((producto, cantidad))
        print(f"Se agregaron {cantidad} unidades de {producto.nombre} al carrito.")

    def eliminar_producto(self, producto):
        for item in self.items:
            if item[0] == producto:
                self.items.remove(item)
                print(f"{producto.nombre} fue eliminado del carrito.")

    def calcular_total(self):
        total = 0
        for item in self.items:
            producto, cantidad = item
            total += producto.precio * cantidad
        return total

    def mostrar_carrito(self):
        print("Carrito de compras:")
        for item in self.items:
            producto, cantidad = item
            print(f"{producto.nombre} - Precio unitario: ${producto.precio} - Cantidad: {cantidad}")
        print(f"Total a pagar: ${self.calcular_total()}")

# Ejemplo de uso del sistema de la tienda online

# Creamos algunos productos
producto1 = Producto("P001", "Laptop HP", 1500, 10)
producto2 = Producto("P002", "Mouse Logitech", 10, 20)
producto3 = Producto("P003", "Teclado mecánico", 15, 15)

# Creamos un cliente
cliente1 = Cliente("Angel Cabrera", "angel777ec@gmail.com")

# Creamos un carrito de compras
carrito1 = Carrito()

# El cliente agrega productos al carrito
carrito1.agregar_producto(producto1, 1)
carrito1.agregar_producto(producto2, 2)

# Mostramos el contenido actual del carrito
carrito1.mostrar_carrito()

# El cliente elimina un producto del carrito
carrito1.eliminar_producto(producto2)

# Mostramos el contenido actualizado del carrito
carrito1.mostrar_carrito()

# El cliente realiza el pago
total_pagar = carrito1.calcular_total()
print(f"{cliente1.nombre} pagará un total de ${total_pagar}. Gracias por su compra!")