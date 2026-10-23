# Error original: "numero" nunca cambiaba, la condición siempre era verdadera.
# Corrección: se incrementa la variable que controla el ciclo.
numero = 1

while numero <= 5:
    print(numero)
    numero += 1
#while repite un bloque de codigo de manera automatica 