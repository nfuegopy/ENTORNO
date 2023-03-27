import random

# Creamos una lista con los números del 1 al 49
numeros = [x for x in range(1, 50)]

# Creamos una lista vacía para almacenar los números adivinados
adivinados = []

# Iteramos seis veces para elegir seis números
for i in range(6):
    # Elegimos un número aleatorio de la lista de números disponibles
    numero_elegido = random.choice(numeros)
    
    # Agregamos el número adivinado a la lista de números adivinados
    adivinados.append(numero_elegido)
    
    # Eliminamos el número adivinado de la lista de números disponibles
    numeros.remove(numero_elegido)

# Ordenamos la lista de números adivinados y la imprimimos en pantalla
adivinados.sort()
print("Los números adivinados son:", adivinados)
