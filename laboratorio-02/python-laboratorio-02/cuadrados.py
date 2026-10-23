numeros = [1, 2, 3, 4, 5]

# Con for
cuadrados = []
for numero in numeros:
    cuadrados.append(numero ** 2)
print(cuadrados)

# Con comprensión
cuadrados = [numero ** 2 for numero in numeros]
print(cuadrados)
