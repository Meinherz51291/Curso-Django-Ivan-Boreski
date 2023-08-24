"""Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia)."""

# Pedimos al usuario que ingrese una cadena de caracteres
cadena = input("Ingresa una cadena de caracteres: ")

# Dividimos la cadena en palabras utilizando el espacio como separador y guardamos las palabras en una lista
palabras = cadena.split()

# Creamos un diccionario para almacenar las palabras y sus frecuencias
diccionario_frecuencias = {}

# Recorremos la lista de palabras
for palabra in palabras:
    # Si la palabra ya está en el diccionario, incrementamos su frecuencia
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra] += 1
    # Si la palabra no está en el diccionario, la agregamos con frecuencia 1
    else:
        diccionario_frecuencias[palabra] = 1

# Mostramos el diccionario de frecuencias resultante
print("Frecuencia de palabras:")
for palabra, frecuencia in diccionario_frecuencias.items():
    print(f"{palabra}: {frecuencia}")
