"""Representación inicial de un producto digital."""
producto = {"nombre": "Logotipo principal", "tipo": "identidad visual", "precio": 80000}
print("Producto digital de Novexa")
for clave, valor in producto.items():
    print(f"{clave.capitalize()}: {valor}")
