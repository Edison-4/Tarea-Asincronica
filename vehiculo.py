class Vehiculo:
    def __init__(self, marca: str, modelo: str, anio: int):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._marca = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._modelo = value

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, value):
        self._anio = value

    # Métodos de comportamiento
    def encender(self):
        return f"El vehículo {self.marca} {self.modelo} está encendido."

    def apagar(self):
        return f"El vehículo {self.marca} {self.modelo} está apagado."

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"