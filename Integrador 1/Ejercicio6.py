"""Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad"""

class Persona:
    # Constructor de la clase
    def __init__(self, nombre="", edad=0, dni=""):
        # Inicializamos los atributos
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    # Setter para el atributo 'nombre'
    def set_nombre(self, nombre):
        # Validamos que el nombre no esté vacío
        if nombre.strip() != "":
            self.nombre = nombre
        else:
            print("Error: El nombre no puede estar vacío.")

    # Getter para el atributo 'nombre'
    def get_nombre(self):
        return self.nombre

    # Setter para el atributo 'edad'
    def set_edad(self, edad):
        # Validamos que la edad sea un número positivo
        if edad >= 0:
            self.edad = edad
        else:
            print("Error: La edad debe ser un número positivo.")

    # Getter para el atributo 'edad'
    def get_edad(self):
        return self.edad

    # Setter para el atributo 'dni'
    def set_dni(self, dni):
        # Validamos que el DNI tenga una longitud válida
        if len(dni) == 9:
            self.dni = dni
        else:
            print("Error: El DNI debe tener 9 dígitos.")

    # Getter para el atributo 'dni'
    def get_dni(self):
        return self.dni

    # Método para mostrar los datos de la persona
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    # Método para verificar si la persona es mayor de edad
    def es_mayor_de_edad(self):
        return self.edad >= 18

# Ejemplo de uso:
persona1 = Persona()
persona1.set_nombre("Juan")
persona1.set_edad(25)
persona1.set_dni("123456789")

persona1.mostrar()

if persona1.es_mayor_de_edad():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")
