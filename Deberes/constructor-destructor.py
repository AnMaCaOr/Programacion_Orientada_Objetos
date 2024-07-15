class Persona:
    def __init__(self, nombre, edad):
        """
        Constructor: Inicializa un objeto Persona.
        Asigna el nombre y la edad proporcionados a los atributos del objeto.
        """
        self.nombre = nombre
        self.edad = edad
        print(f"Persona creada: {self.nombre}, {self.edad} años")

    def saludar(self):
        """
        Método que imprime un saludo.
        """
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def __del__(self):
        """
        Destructor: Se llama cuando el objeto Persona es destruido.
        """
        print(f"Adiós, {self.nombre}.")

# Demostración del uso de los constructores y destructores
def main():
    # Crear un objeto Persona
    persona1 = Persona('Angel', 42)
    persona1.saludar()

    # Crear otro objeto Persona
    persona2 = Persona('Irene', 40)
    persona2.saludar()

    # Los objetos serán automáticamente destruidos al salir del alcance
    # y los destructores serán llamados.

if __name__ == "__main__":
    main()