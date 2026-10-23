productos = ["Teclado", "Mouse", "Monitor", "Cámara", "Parlantes"]

print(productos[0:2])
print(productos[2:])
print(productos[:3])
print(productos[-2:])

print()
productos = ["Monitor", "Cámara", "Teclado"]

ordenados = sorted(productos)
print("Original:", productos)
print("Ordenados:", ordenados)

productos.sort()
print("Después de sort():", productos)
