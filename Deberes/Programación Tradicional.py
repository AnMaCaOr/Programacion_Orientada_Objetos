def ingresar_temperaturas():
    """Función para ingresar las temperaturas diarias durante una semana."""
    temperaturas = []
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

    for dia in dias:
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico.")

    return temperaturas


def calcular_promedio(temperaturas):
    """Función para calcular el promedio de una lista de temperaturas."""
    if len(temperaturas) == 0:
        return 0
    return sum(temperaturas) / len(temperaturas)


def main():
    """Función principal que coordina la ejecución del programa."""
    print("Programa para calcular el promedio semanal del clima")
    temperaturas_semanales = ingresar_temperaturas()
    promedio_semanal = calcular_promedio(temperaturas_semanales)
    print(f"La temperatura promedio semanal es: {promedio_semanal:.2f}°C")


# Ejecución del programa
if __name__ == "__main__":
    main()


