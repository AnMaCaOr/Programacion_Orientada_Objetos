class Aeropuerto:
    def __init__(self, codigo, nombre, ciudad):
        self.codigo = codigo
        self.nombre = nombre
        self.ciudad = ciudad

    def __str__(self):
        return f"{self.nombre} ({self.codigo}) - {self.ciudad}"

class Vuelo:
    def __init__(self, numero, origen, destino, fecha, hora):
        self.numero = numero
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.hora = hora
        self.asientos_disponibles = 100  # número inicial de asientos disponibles

    def __str__(self):
        return f"Vuelo {self.numero} de {self.origen.codigo} a {self.destino.codigo} el {self.fecha} a las {self.hora}"

    def reservar_asiento(self):
        if self.asientos_disponibles > 0:
            self.asientos_disponibles -= 1
            print("¡Reserva exitosa!")
        else:
            print("Lo siento, no hay asientos disponibles en este vuelo.")

class Reserva:
    def __init__(self, vuelo, pasajero):
        self.vuelo = vuelo
        self.pasajero = pasajero

    def __str__(self):
        return f"Reserva para {self.pasajero} en el vuelo {self.vuelo.numero}"

# Ejemplo de uso del sistema de reservas

# Creamos algunos aeropuertos
aeropuerto_cuenca = Aeropuerto("CUE", "Aeropuerto Mariscal La Mar", "Cuenca")
aeropuerto_quito = Aeropuerto("UIO", "Aeropuerto Mariscal Sucre", "Quito")
aeropuerto_guayaquil = Aeropuerto("GYE", "Aeropuerto José Joaquín de Olmedo", "Guayaquil")

# Creamos algunos vuelos
vuelo1 = Vuelo("IB1234", aeropuerto_cuenca, aeropuerto_quito, "2024-07-01", "10:00")
vuelo2 = Vuelo("AF5678", aeropuerto_guayaquil, aeropuerto_cuenca, "2024-07-02", "12:00")

# Mostramos información de los vuelos
print(vuelo1)
print(vuelo2)

# Intentamos reservar asientos
vuelo1.reservar_asiento()  # Reserva exitosa
vuelo1.reservar_asiento()  # Reserva exitosa
vuelo1.reservar_asiento()  # Reserva exitosa
vuelo1.reservar_asiento()  # Reserva exitosa
vuelo1.reservar_asiento()  # No hay asientos disponibles

# Creamos una reserva
reserva1 = Reserva(vuelo1, "Angel Cabrera")

# Mostramos la reserva
print(reserva1)