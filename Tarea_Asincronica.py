class Motor:
    def __init__(self, tipo, potencia):
        self._tipo = tipo
        self._potencia = potencia

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        print(f"Cambiando tipo de motor a: {valor}")
        self._tipo = valor

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, valor):
        if valor > 0:
            self._potencia = valor
        else:
            print("Error: La potencia debe ser positiva.")

    def encender_motor(self):
        print(f"Motor {self._tipo} encendido (Potencia: {self._potencia} HP).")

    def detener_motor(self):
        print(f"Motor {self._tipo} apagado.")

    def __str__(self):
        return f"Motor(Tipo: {self._tipo}, Potencia: {self._potencia} HP)"

class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, valor):
        self._marca = valor

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, valor):
        self._modelo = valor

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, valor):
        if valor > 1900:
            self._anio = valor
        else:
            print("Error: Año no válido.")

    def encender(self):
        print(f"El {self._marca} {self._modelo} se ha encendido.")

    def apagar(self):
        print(f"El {self._marca} {self._modelo} se ha apagado.")

    def __str__(self):
        return f"Vehiculo(Marca: {self._marca}, Modelo: {self._modelo}, Año: {self._anio})"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, numero_de_puertas, motor):
        super().__init__(marca, modelo, anio)
        self._numero_de_puertas = numero_de_puertas
        self._motor = motor

    @property
    def numero_de_puertas(self):
        return self._numero_de_puertas

    @numero_de_puertas.setter
    def numero_de_puertas(self, valor):
        self._numero_de_puertas = valor

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    def abrir_maletero(self):
        print(f"Abriendo maletero del {self.marca} {self.modelo}.")

    def tocar_claxon(self):
        print(f"¡Beep! ¡Beep! ({self.marca})")

    def __str__(self):
        info_base = super().__str__()
        return (f"Automovil -> {info_base}\n"
                f"  Puertas: {self._numero_de_puertas}\n"
                f"  {self._motor}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, cilindraje, motor):
        super().__init__(marca, modelo, anio)
        self._cilindraje = cilindraje
        self._motor = motor

    @property
    def cilindraje(self):
        return self._cilindraje

    @cilindraje.setter
    def cilindraje(self, valor):
        self._cilindraje = valor

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    def hacer_caballito(self):
        print(f"¡La {self.marca} {self.modelo} está haciendo un caballito! 🏍️")

    def usar_patada_arranque(self):
        print(f"Usando la patada de arranque... *KICK*")

    def __str__(self):
        info_base = super().__str__()
        return (f"Motocicleta -> {info_base}\n"
                f"  Cilindraje: {self._cilindraje}cc\n"
                f"  {self._motor}")

if __name__ == "__main__":
    
    print("========= SISTEMA DE GESTIÓN DE VEHÍCULOS =========")

    print("\n--- Creando Motores ---")
    motor_v8_mustang = Motor(tipo="V8", potencia=450)
    motor_electrico_tesla = Motor(tipo="Eléctrico", potencia=300)
    motor_boxer_bmw = Motor(tipo="Boxer", potencia=136)
    motor_mono_honda = Motor(tipo="Monocilíndrico", potencia=40)
    
    print(motor_v8_mustang)
    motor_v8_mustang.encender_motor()
    
    print("-------------------------------------------------")

    print("\n--- Creando Automóviles ---")
    auto1 = Automovil("Ford", "Mustang", 2023, 2, motor_v8_mustang)
    auto2 = Automovil("Tesla", "Model S", 2024, 4, motor_electrico_tesla)

    print("\n[Probando Auto 1: Ford Mustang]")
    auto1.encender()
    auto1.tocar_claxon()
    auto1.abrir_maletero()
    
    print("\n[Info Auto 2: Tesla (usa __str__)]")
    print(auto2)
    auto2.motor.encender_motor() 
    
    print("-------------------------------------------------")

    print("\n--- Creando Motocicletas ---")
    moto1 = Motocicleta("BMW", "R1250GS", 2022, 1250, motor_boxer_bmw)
    moto2 = Motocicleta("Honda", "CRF450L", 2021, 450, motor_mono_honda)

    print("\n[Probando Moto 1: BMW]")
    moto1.encender()
    moto1.hacer_caballito()
    
    print("\n[Info Moto 2: Honda (usa __str__)]")
    print(moto2)
    moto2.usar_patada_arranque()
    moto2.motor.encender_motor()
    
    print("-------------------------------------------------")

    print("\n--- Demostración de @setter ---")
    print(f"Año original de auto1: {auto1.anio}")
    auto1.anio = 2024
    print(f"Nuevo año de auto1: {auto1.anio}")
    
    print(f"\nPotencia original motor moto1: {moto1.motor.potencia} HP")
    moto1.motor.potencia = 140 
    print(f"Nueva potencia motor moto1: {moto1.motor.potencia} HP")
    
    print("\n[Info Moto 1 actualizada]")
    print(moto1)
