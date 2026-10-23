productos = ["Teclado", "Mouse"]

nombre = input("Nombre del producto nuevo: ").strip()

if nombre == "":
    print("El nombre no puede estar vacío.")
elif nombre in productos:
    print("El producto está repetido.")
else:
    productos.append(nombre)
    print("Producto agregado.")

print(productos)
