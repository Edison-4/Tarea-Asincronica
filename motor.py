class Motor:
    def __init__(self, tipo: str, potencia: int):
        self._tipo = tipo
        self._potencia = potencia

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, value):
        self._potencia = value

    # Métodos de comportamiento
    def encender_motor(self):
        return f"El motor {self.tipo} ha sido encendido."

    def detener_motor(self):
        return f"El motor {self.tipo} se ha detenido."

    def __str__(self):
        return f"Motor(tipo={self.tipo}, potencia={self.potencia}HP)"