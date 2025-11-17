class Vehiculo:
    def __init__(self, marca: str, modelo: str, anio: int, motor: Motor):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio
        self._motor = motor

    @property
    def marca(self) -> str:
        return self._marca

    @marca.setter
    def marca(self, valor: str):
        self._marca = valor

    @property
    def modelo(self) -> str:
        return self._modelo

    @modelo.setter
    def modelo(self, valor: str):
        self._modelo = valor

    @property
    def anio(self) -> int:
        return self._anio

    @anio.setter
    def anio(self, valor: int):
        if valor > 1900:
            self._anio = valor
        else:
            print("Error: Año no válido.")

    @property
    def motor(self) -> Motor:
        return self._motor

    @motor.setter
    def motor(self, valor: Motor):
        if isinstance(valor, Motor):
            self._motor = valor
        else:
            print("Error: Debe asignar un objeto de tipo Motor.")

    def encender(self):
        print(f"Girando la llave del {self._marca} {self._modelo}...")
        self._motor.encender_motor()

    def apagar(self):
        print(f"Apagando el {self._marca} {self._modelo}...")
        self._motor.detener_motor()

    def __str__(self) -> str:
        return f"Vehiculo(Marca: {self._marca}, Modelo: {self._modelo}, Año: {self._anio}, {str(self._motor)})"
