class Cuenta:
    # Constructor de la clase
    def __init__(self, titular, cantidad=0.0):
        # Inicializamos los atributos
        self.titular = titular
        self.cantidad = cantidad

    # Setter para el atributo 'cantidad' (solo permite ingresar o retirar dinero)
    def ingresar(self, cantidad):
        # Validamos que la cantidad ingresada sea positiva
        if cantidad > 0:
            self.cantidad += cantidad
        else:
            print("Error: La cantidad debe ser positiva para ingresar dinero.")

    def retirar(self, cantidad):
        # Permitimos retirar incluso si la cantidad es negativa (quedando en números rojos)
        self.cantidad -= cantidad

    # Getter para el atributo 'titular'
    def get_titular(self):
        return self.titular.get_nombre()  # Utilizamos el getter de la clase Persona

    # Getter para el atributo 'cantidad'
    def get_cantidad(self):
        return self.cantidad

    # Método para mostrar los datos de la cuenta
    def mostrar(self):
        print(f"Titular: {self.get_titular()}")
        print(f"Cantidad en la cuenta: {self.cantidad}")

# Definición de la clase Persona (previamente definida)
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

# Clase CuentaJoven
class CuentaJoven(Cuenta):
    # Constructor de la clase CuentaJoven
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        # Llamamos al constructor de la clase padre (Cuenta)
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    # Setter y getter para el atributo 'bonificacion'
    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    # Método para validar si el titular es mayor de edad pero menor de 25 años
    def es_titular_valido(self):
        edad_titular = self.titular.get_edad()
        return 18 <= edad_titular < 25

    # Override del método retirar para verificar si el titular es válido
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("Error: El titular no es válido para retirar dinero.")

    # Override del método mostrar para incluir la información específica de CuentaJoven
    def mostrar(self):
        print("Cuenta Joven")
        print(f"Bonificación: {self.bonificacion}%")
        super().mostrar()

# Ejemplo de uso:
titular_joven = Persona("Ana", 22)
cuenta_joven = CuentaJoven(titular_joven, 500.0, 5.0)

cuenta_joven.mostrar()

cuenta_joven.ingresar(200.0)
cuenta_joven.retirar(50.0)

print("\nDespués de operaciones:")
cuenta_joven.mostrar()

