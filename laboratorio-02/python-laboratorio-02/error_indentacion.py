# Versión corregida: el print va indentado dentro del if
precio = 80000

if precio >= 50000:
    print("La compra supera el valor indicado.")

print("Programa terminado.")

# Variante: el último print DENTRO del bloque if.
# Con precio = 30000 este mensaje ya no se mostraría, porque
# solo se ejecuta cuando la condición es verdadera.
precio = 30000

if precio >= 50000:
    print("La compra supera el valor indicado.")
    print("Programa terminado (dentro del if).")
