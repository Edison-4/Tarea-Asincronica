from vehiculo import Vehiculo
from motor import Motor

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, cilindraje, motor: Motor):
        super().__init__(marca, modelo, anio)
        self.cilindraje = cilindraje
        self.motor = motor

    # Métodos de comportamiento
    def hacer_caballito(self):
        return f"La motocicleta {self.marca} está haciendo un caballito."

    def usar_patada_arranque(self):
        return f"Arrancando la motocicleta {self.marca} con patada..."

    def __str__(self):
        return f"{super().__str__()} - Motocicleta {self.cilindraje}cc, {self.motor}"