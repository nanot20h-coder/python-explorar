grupos = [[1, 2], [3, 4], [5, 6]]

numeros = [numero for grupo in grupos for numero in grupo]
print(numeros)  # [1, 2, 3, 4, 5, 6]

# Esto es una expresión generadora, no una tupla
cuadrados = (numero ** 2 for numero in range(1, 5))
print(type(cuadrados))
print(list(cuadrados))

tupla_cuadrados = tuple(numero ** 2 for numero in range(1, 5))
print(tupla_cuadrados)
