precios = [10000, 20000, 50000, 80000]

# Con for y append
con_impuesto_for = []
for precio in precios:
    con_impuesto_for.append(precio * 1.19)

# Con comprensión
con_impuesto_comp = [precio * 1.19 for precio in precios]

print(con_impuesto_for)
print(con_impuesto_comp)
print("¿Equivalentes?", con_impuesto_for == con_impuesto_comp)
