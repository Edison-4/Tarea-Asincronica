from motor import Motor
from automovil import Automovil
from motocicleta import Motocicleta

motor1 = Motor("Eléctrico", 350)
motor2 = Motor("Gasolina V8", 400)
motor3 = Motor("Gasolina", 50)
motor4 = Motor("Gasolina V-Twin", 90)

auto1 = Automovil("Tesla", "Model S", 2023, 5, motor1)
auto2 = Automovil("Ford", "F-150", 2021, 4, motor2)

moto1 = Motocicleta("Vespa", "Primavera", 2023, 125, motor3)
moto2 = Motocicleta("Harley-Davidson", "Street Bob", 2022, 1868, motor4)

print(auto1.encender())
print(auto1.abrir_maletero())
print(auto1.motor.encender_motor())

print()

print(moto1.encender())
print(moto1.hacer_caballito())
print(moto1.motor.encender_motor())

print()

print(auto1)
print(auto2)
print(moto1)
print(moto2)