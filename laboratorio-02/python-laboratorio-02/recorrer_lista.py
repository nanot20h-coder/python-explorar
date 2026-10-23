productos = ["Teclado", "Mouse", "Monitor"]

for producto in productos:
    print("Producto:", producto)

print()
for posicion, producto in enumerate(productos, start=1):
    print(posicion, "-", producto)
