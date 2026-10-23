# Error original: se usaba "or", así que bastaba una condición.
# Corrección: deben cumplirse AMBAS, por eso se usa "and".
membresia = False
valor_compra = 200000

if membresia and valor_compra >= 150000:
    print("Aplica descuento.")
else:
    print("No aplica descuento.")
