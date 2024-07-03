# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre  # Atributo público


# Clase derivada que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.__raza = raza  # Atributo privado (encapsulación)

    def hacer_sonido(self):
        return "Guau!"

    # Método para acceder al atributo privado
    def obtener_raza(self):
        return self.__raza

# Otra clase derivada que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.__color = color  # Atributo privado (encapsulación)

    def hacer_sonido(self):
        return "Miau!"

    # Método para acceder al atributo privado
    def obtener_color(self):
        return self.__color

# Ejemplo de polimorfismo
def imprimir_sonido(animal):
    print(f"{animal.nombre} dice: {animal.hacer_sonido()}")

# Crear instancias de las clases
perro = Perro("Rex", "Labrador")
gato = Gato("Michi", "Blanco")

# Acceder a los métodos y atributos
print(perro.nombre)  # Salida: Rex
print(perro.obtener_raza())  # Salida: Labrador
print(gato.nombre)  # Salida: Michi
print(gato.obtener_color())  # Salida: Blanco

# Demostración de polimorfismo
imprimir_sonido(perro)  # Salida: Rex dice: Guau!
imprimir_sonido(gato)   # Salida: Michi dice: Miau!