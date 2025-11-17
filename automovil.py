class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, anio: int, motor: Motor, numero_puertas: int):
        super().__init__(marca, modelo, anio, motor)
        self._numero_puertas = numero_puertas

    @property
    def numero_puertas(self) -> int:
        return self._numero_puertas

    @numero_puertas.setter
    def numero_puertas(self, valor: int):
        if valor in (2, 4, 5):
            self._numero_puertas = valor
        else:
            print("Error: Número de puertas no común.")

    def abrir_maletero(self):
        print(f"El maletero del {self.marca} está abierto.")

    def tocar_claxon(self):
        print(f"¡Beep! ¡Beep! Soy un {self.modelo}.")

    def __str__(self) -> str:
        info_padre = super().__str__()
        return f"Automovil[{info_padre}, Puertas: {self._numero_puertas}]"
