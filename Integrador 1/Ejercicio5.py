"""Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva."""

# Función para obtener un valor entero del usuario de manera iterativa
def get_int_iterativo():
    while True:
        try:
            # Pedimos al usuario que ingrese un valor
            valor = int(input("Ingresa un valor entero: "))
            # Si no se lanzó ValueError, retornamos el valor
            return valor
        except ValueError:
            print("Oops! No es un valor entero válido. Inténtalo nuevamente.")

# Función para obtener un valor entero del usuario de manera recursiva
def get_int_recursivo():
    try:
        # Pedimos al usuario que ingrese un valor
        valor = int(input("Ingresa un valor entero: "))
        # Si no se lanzó ValueError, retornamos el valor
        return valor
    except ValueError:
        print("Oops! No es un valor entero válido. Inténtalo nuevamente.")
        # Llamamos a la función recursivamente para volver a intentarlo
        return get_int_recursivo()

# Uso de las funciones
print("Obtener un valor entero de manera iterativa:")
valor_iterativo = get_int_iterativo()
print(f"Valor entero obtenido de manera iterativa: {valor_iterativo}")

print("\nObtener un valor entero de manera recursiva:")
valor_recursivo = get_int_recursivo()
print(f"Valor entero obtenido de manera recursiva: {valor_recursivo}")
