total = 0
numero = int(input("Número (0 para terminar): "))

while numero != 0:
    total += numero
    print("Acumulado:", total)
    numero = int(input("Número (0 para terminar): "))

print("Total final:", total)
# Con 10, 25, -5, 0 el total esperado es 30
