class Cuenta:
    def __init__(self, titular, cantidad=0):
        self._titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        return self._titular

    @property
    def cantidad(self):
        return self._cantidad

    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad

    def retirar(self, cantidad):
        self._cantidad -= cantidad

    def mostrar(self):
        return f"Titular: {self._titular}\nCantidad: {self._cantidad}"

class CuentaJoven(Cuenta):
    def __init__(self, titular, bonificacion, cantidad=0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self._bonificacion

    def es_titular_valido(self):
        return 18 <= self._titular.edad < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)

    def mostrar(self):
        return f"Cuenta Joven\nBonificación: {self._bonificacion}%"

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Solicitar datos al usuario para crear una CuentaJoven
nombre = input("Ingrese el nombre del titular: ")
edad = int(input("Ingrese la edad del titular: "))
bonificacion = float(input("Ingrese la bonificación (%): "))
cantidad_inicial = float(input("Ingrese la cantidad inicial: "))

titular = Persona(nombre, edad)
cuenta_joven = CuentaJoven(titular, bonificacion, cantidad_inicial)

print("Cuenta creada:")
print(cuenta_joven.mostrar())

# Realizar operaciones en la cuenta
cantidad_ingreso = float(input("Ingrese la cantidad a ingresar: "))
cuenta_joven.ingresar(cantidad_ingreso)

cantidad_retiro = float(input("Ingrese la cantidad a retirar: "))
cuenta_joven.retirar(cantidad_retiro)

print("Operaciones realizadas:")
print(cuenta_joven.mostrar())



