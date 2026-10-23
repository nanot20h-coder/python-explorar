"""Calcula compras de recursos digitales controlando errores."""
def calcular_compra(precio, cantidad):
    try:
        precio = float(precio)
        cantidad = int(cantidad)
    except (TypeError, ValueError) as exc:
        raise ValueError("Precio o cantidad tienen un formato inválido.") from exc
    if precio < 0 or cantidad <= 0:
        raise ValueError("El precio no puede ser negativo y la cantidad debe ser positiva.")
    return precio * cantidad

if __name__ == "__main__":
    try:
        print(f"Total: ${calcular_compra('25000', '3'):,.0f}")
    except ValueError as error:
        print(f"Compra no válida: {error}")
