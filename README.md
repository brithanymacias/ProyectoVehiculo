# 🚗 Sistema de Vehículos en Python (POO con Herencia, Composición y Encapsulamiento)

Este proyecto implementa un sistema orientado a objetos en Python aplicando los principios fundamentales de la Programación Orientada a Objetos:

- **Herencia**
- **Encapsulamiento con @property**
- **Composición**
- **Métodos de comportamiento**
- **Sobrescritura de métodos (`__str__`)**

El sistema modela vehículos, incluyendo automóviles y motocicletas, cada uno con sus propias características, pero compartiendo atributos comunes gracias a la herencia.

---

## 📘 Estructura del Proyecto

El programa está compuesto por las siguientes clases:

---

### 🔹 **1. Clase Vehiculo (Superclase)**  
Contiene:

- Atributos privados: `marca`, `modelo`, `anio`
- Encapsulamiento mediante `@property` y `@setter`
- Métodos de comportamiento: `encender()`, `apagar()`
- Implementación del método especial `__str__()`

---

### 🔹 **2. Clase Motor (Composición)**  
Cada vehículo tiene un motor.

- Atributos privados: `tipo`, `potencia`
- Métodos: `encender_motor()`, `detener_motor()`
- Sobrescritura de `__str__()`

---

### 🔹 **3. Clase Automovil (Hija de Vehiculo)**  
Incluye:

- Atributo adicional: `puertas`
- Composición: incluye un objeto `Motor`
- Métodos: `abrir_maletero()`, `tocar_claxon()`
- Sobrescritura de `__str__()` usando `super()`

---

### 🔹 **4. Clase Motocicleta (Hija de Vehiculo)**  
Incluye:

- Atributo adicional: `cilindraje`
- Contiene un `Motor` (composición)
- Métodos: `hacer_caballito()`, `usar_patada_arranque()`
- Sobrescritura de `__str__()` usando `super()`

