from vehiculo import Vehiculo
from motor import Motor

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas, motor: Motor):
        super().__init__(marca, modelo, anio)
        self.puertas = puertas
        self.motor = motor

    # Métodos de comportamiento
    def abrir_maletero(self):
        return f"El maletero del automóvil {self.marca} está abierto."

    def tocar_claxon(self):
        return "¡Beep beep!"

    def __str__(self):
        return f"{super().__str__()} - Automóvil {self.puertas} puertas, {self.motor}"