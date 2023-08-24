# Definimos una función llamada 'calcular_mcd' que recibe dos números 'numero1' y 'numero2'
def calcular_mcd(numero1, numero2):
    # Empezamos un ciclo mientras el segundo número no sea cero
    while numero2 != 0:
        # Guardamos el valor original del primer número en 'temporal'
        temporal = numero1
        # Actualizamos el valor del primer número con el valor del segundo número
        numero1 = numero2
        # Calculamos el residuo de la división del valor original del primer número entre el segundo número
        # Y ese residuo se convierte en el nuevo valor del segundo número
        numero2 = temporal % numero2

    # Cuando el segundo número se vuelve cero, el primer número es el máximo común divisor
    return numero1

# Pedimos al usuario que ingrese dos números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Llamamos a la función 'calcular_mcd' con los números ingresados y guardamos el resultado en 'resultado'
resultado = calcular_mcd(num1, num2)

# Mostramos el resultado al usuario
print(f"El máximo común divisor de {num1} y {num2} es: {resultado}")


