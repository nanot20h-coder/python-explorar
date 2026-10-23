productos = ["Teclado", "Mouse", "Monitor"]

nombre = input("Producto a eliminar: ").strip()

if nombre in productos:
    productos.remove(nombre)
    print("Producto eliminado.")
else:
    print("No se encontró el producto.")

print(productos)
