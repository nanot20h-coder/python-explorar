"""Clase Producto con validaciones básicas."""
class Producto:
    def __init__(self, nombre, precio, categoria="recurso digital"):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre es obligatorio.")
        if not isinstance(precio, (int, float)) or isinstance(precio, bool) or precio < 0:
            raise ValueError("El precio debe ser numérico y no negativo.")
        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.categoria = categoria.strip() or "recurso digital"

    def __str__(self):
        return f"{self.nombre} ({self.categoria}) - ${self.precio:,.0f}"

if __name__ == "__main__":
    print(Producto("Kit de marca", 120000, "identidad visual"))
