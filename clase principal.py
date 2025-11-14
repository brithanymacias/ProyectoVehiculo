from motor import Motor
from automovil import Automovil
from motocicleta import Motocicleta

# Crear Motores
motor1 = Motor("Gasolina", 120)
motor2 = Motor("Diesel", 140)
motor3 = Motor("Gasolina", 60)
motor4 = Motor("Eléctrico", 80)

# Crear Automóviles
auto1 = Automovil("Toyota", "Corolla", 2020, 4, motor1)
auto2 = Automovil("Hyundai", "Elantra", 2018, 4, motor2)

# Crear Motocicletas
moto1 = Motocicleta("Yamaha", "FZ", 2022, 150, motor3)
moto2 = Motocicleta("Honda", "CBR", 2021, 250, motor4)

# Ejecutar métodos de comportamiento
print(auto1.encender())
print(auto1.abrir_maletero())
print(auto1.motor.encender_motor())

print()

print(moto1.encender())
print(moto1.hacer_caballito())
print(moto1.motor.encender_motor())

print()

# Mostrar resultados
print(auto1)
print(auto2)
print(moto1)
print(moto2)