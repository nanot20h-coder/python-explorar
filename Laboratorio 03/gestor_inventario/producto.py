"""Modelo Producto para el inventario inicial de Novexa."""
class Producto:
    """Representa un logotipo, plantilla u otro recurso digital."""
    def __init__(self, nombre, categoria, precio, cantidad=1, descripcion=""):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del recurso es obligatorio.")
        if not isinstance(categoria, str) or not categoria.strip():
            raise ValueError("La categoría es obligatoria.")
        if not isinstance(precio, (int, float)) or isinstance(precio, bool) or precio < 0:
            raise ValueError("El precio debe ser un número no negativo.")
        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad < 0:
            raise ValueError("La cantidad debe ser un entero no negativo.")
        self.nombre = nombre.strip()
        self.categoria = categoria.strip()
        self.precio = float(precio)
        self.cantidad = cantidad
        self.descripcion = descripcion.strip() if isinstance(descripcion, str) else ""

    def valor_total(self):
        return self.precio * self.cantidad

    def to_dict(self):
        return {"nombre": self.nombre, "categoria": self.categoria, "precio": self.precio,
                "cantidad": self.cantidad, "descripcion": self.descripcion}

    @classmethod
    def from_dict(cls, datos):
        if not isinstance(datos, dict):
            raise ValueError("Cada producto debe estar representado por un objeto.")
        return cls(datos["nombre"], datos["categoria"], datos["precio"],
                   datos.get("cantidad", 1), datos.get("descripcion", ""))

    def __str__(self):
        return f"{self.nombre} | {self.categoria} | ${self.precio:,.0f} | unidades: {self.cantidad}"
