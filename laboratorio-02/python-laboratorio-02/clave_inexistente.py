# Error original: producto["precio"] -> KeyError
producto = {"codigo": "P001", "nombre": "Teclado"}

print(producto.get("precio", "Precio no registrado"))
