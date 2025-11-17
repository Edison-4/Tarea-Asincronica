class Motor:
    def __init__(self, tipo: str, potencia: int):
        self._tipo = tipo
        self._potencia = potencia

    @property
    def tipo(self) -> str:
        return self._tipo

    @tipo.setter
    def tipo(self, valor: str):
        print(f"Cambiando tipo de motor a: {valor}")
        self._tipo = valor

    @property
    def potencia(self) -> int:
        return self._potencia

    @potencia.setter
    def potencia(self, valor: int):
        if valor > 0:
            self._potencia = valor
        else:
            print("Error: La potencia debe ser un valor positivo.")

    def encender_motor(self):
        print(f"Motor {self._tipo} de {self._potencia} HP encendido. ¡Vroom!")

    def detener_motor(self):
        print(f"Motor {self._tipo} apagado.")

    def __str__(self) -> str:
        return f"Motor(Tipo: {self._tipo}, Potencia: {self._potencia} HP)"
