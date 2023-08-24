def calcular_mcm(num1, num2):
    # Inicializar el máximo de los dos números para asegurarnos de que el bucle no sea infinito
    maximo = max(num1, num2)
    
    # Empezamos a buscar el MCM desde el máximo de los dos números
    while True:
        # Verificar si el máximo es un múltiplo de ambos números
        if maximo % num1 == 0 and maximo % num2 == 0:
            # Si es así, hemos encontrado el MCM
            mcm = maximo
            break  # Salir del bucle
        maximo += 1  # Intentar con el siguiente número
    
    return mcm

# Solicitar números al usuario
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Calcular el MCM
mcm_resultado = calcular_mcm(numero1, numero2)

# Mostrar el resultado
print(f"El Mínimo Común Múltiplo (MCM) de {numero1} y {numero2} es: {mcm_resultado}")
