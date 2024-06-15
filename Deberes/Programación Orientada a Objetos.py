class ClimaDiario:
    def __init__(self):
        self._temperaturas = []

    def ingresar_temperaturas(self):
        """Método para ingresar las temperaturas diarias durante una semana."""
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

        for dia in dias:
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del {dia}: "))
                    self._temperaturas.append(temp)
                    break
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")

    def calcular_promedio(self):
        """Método para calcular el promedio semanal de las temperaturas."""
        if len(self._temperaturas) == 0:
            return 0
        return sum(self._temperaturas) / len(self._temperaturas)

    def mostrar_promedio(self):
        """Método para mostrar el promedio semanal de las temperaturas."""
        promedio = self.calcular_promedio()
        print(f"La temperatura promedio semanal es: {promedio:.2f}°C")


def main():
    """Función principal que coordina la ejecución del programa."""
    print("Programa para calcular el promedio semanal del clima")
    clima_semanal = ClimaDiario()
    clima_semanal.ingresar_temperaturas()
    clima_semanal.mostrar_promedio()


# Ejecución del programa
if __name__ == "__main__":
    main()