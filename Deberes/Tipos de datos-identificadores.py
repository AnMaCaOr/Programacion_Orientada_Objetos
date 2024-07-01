# Este programa calcula el área de diferentes figuras geométricas: cuadrado, rectángulo y círculo.
# El usuario puede seleccionar la figura y proporcionar los datos necesarios para el cálculo.

def calcular_area_cuadrado(lado: float) -> float:
    """Calcula el área de un cuadrado dado el lado."""
    return lado * lado


def calcular_area_rectangulo(ancho: float, alto: float) -> float:
    """Calcula el área de un rectángulo dados el ancho y el alto."""
    return ancho * alto


def calcular_area_circulo(radio: float) -> float:
    """Calcula el área de un círculo dado el radio."""
    pi = 3.14159
    return pi * radio * radio


def main():
    print("Calculadora de áreas de figuras geométricas")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Círculo")

    # Solicita al usuario seleccionar una figura
    seleccion = int(input("Seleccione la figura (1/2/3): "))

    if seleccion == 1:
        # Calcula el área de un cuadrado
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = calcular_area_cuadrado(lado)
        figura = "cuadrado"

    elif seleccion == 2:
        # Calcula el área de un rectángulo
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        alto = float(input("Ingrese el alto del rectángulo: "))
        area = calcular_area_rectangulo(ancho, alto)
        figura = "rectángulo"

    elif seleccion == 3:
        # Calcula el área de un círculo
        radio = float(input("Ingrese el radio del círculo: "))
        area = calcular_area_circulo(radio)
        figura = "círculo"

    else:
        # Opción no válida
        print("Selección no válida")
        return

    # Muestra el resultado
    print(f"El área del {figura} es: {area}")


# Ejecuta el programa principal
if __name__ == "__main__":
    main()