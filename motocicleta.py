class Motocicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, anio: int, motor: Motor, cilindraje: int):
        super().__init__(marca, modelo, anio, motor)
        self._cilindraje = cilindraje

    @property
    def cilindraje(self) -> int:
        return self._cilindraje

    @cilindraje.setter
    def cilindraje(self, valor: int):
        if valor >= 50:
            self._cilindraje = valor
        else:
            print("Error: Cilindraje muy bajo.")

    def hacer_caballito(self):
        print(f"¡La {self.marca} {self.modelo} está haciendo un caballito! 🏍️")

    def usar_patada_arranque(self):
        print(f"Dando una patada de arranque a la {self._cilindraje}cc...")

    def __str__(self) -> str:
        info_padre = super().__str__()
        return f"Motocicleta[{info_padre}, Cilindraje: {self._cilindraje}cc]"
