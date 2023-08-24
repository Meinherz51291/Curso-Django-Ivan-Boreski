"""Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos."""

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
    def __init__(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

# Ejemplo de uso:
titular = Persona("Juan")
cuenta1 = Cuenta(titular, 1000.0)

cuenta1.mostrar()
cuenta1.ingresar(500.0)
cuenta1.retirar(200.0)

print("\nDespués de operaciones:")
cuenta1.mostrar()
