📝 Explicación del Programa

Este programa implementa un sistema orientado a objetos que modela diferentes tipos de vehículos y su motor, aplicando herencia, composición y principios básicos de POO en Python.

El objetivo es simular el comportamiento de un vehículo genérico, así como de sus dos subclases principales: Automóvil y Motocicleta. Además, se incluye la clase Motor, que se incorpora a cada vehículo mediante composición, representando la parte fundamental del funcionamiento.

🚗 Clases del Programa
1. Clase Vehiculo (Clase Padre)

Representa las características generales de un vehículo.
Incluye atributos comunes como:

marca

modelo

año

Y métodos básicos:

encender()

apagar()

__str__() para mostrar información del vehículo.

Esta clase sirve como base para los otros tipos de vehículos.

2. Clase Automovil (Hereda de Vehiculo)

Amplía la funcionalidad del vehículo añadiendo:

número de puertas

métodos propios como:

abrir_maletero()

tocar_claxon()

Tiene una relación de composición con la clase Motor, ya que todo automóvil posee un motor y sin él no funciona.

3. Clase Motocicleta (Hereda de Vehiculo)

Incluye atributos específicos de una moto:

cilindraje

Y métodos únicos como:

hacer_caballito()

usar_patada_arranque()

También incluye un objeto Motor mediante composición.

4. Clase Motor (Composición)

Define características y comportamientos del motor:

tipo de motor

potencia

Con métodos:

encender_motor()

detener_motor()

La relación de composición indica que el motor forma parte esencial del vehículo:
si el vehículo deja de existir, su motor también.

🔗 Relaciones del Sistema
✔ Herencia

Automovil y Motocicleta heredan de Vehiculo.

✔ Composición

Tanto Automovil como Motocicleta contienen un objeto Motor.

▶️ Funcionamiento del Programa

El programa permite:

Crear diferentes vehículos.

Encenderlos, apagarlos o activar acciones específicas.

Mostrar la información completa de cada uno.

Comprobar el uso del motor mediante composición.

Ejemplo común de ejecución:

moto = Motocicleta("Yamaha", "FZ", 2022, 150, Motor("Gasolina", 14))
automovil = Automovil("Chevrolet", "Spark", 2020, 4, Motor("Gasolina", 80))

print(moto)
print(automovil)
