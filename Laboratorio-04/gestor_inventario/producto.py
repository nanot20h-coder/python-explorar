"""Modelo de un recurso digital del inventario."""


class Producto:
    """Representa un producto o recurso digital."""

    CAMPOS_REQUERIDOS = (
        "nombre",
        "categoria",
        "precio",
        "cantidad",
        "descripcion",
    )

    def __init__(
        self,
        nombre,
        categoria,
        precio,
        cantidad=1,
        descripcion="",
    ):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del recurso es obligatorio.")

        if not isinstance(categoria, str) or not categoria.strip():
            raise ValueError("La categoría del recurso es obligatoria.")

        if (
            not isinstance(precio, (int, float))
            or isinstance(precio, bool)
        ):
            raise TypeError("El precio debe ser numérico.")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")

        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise TypeError("La cantidad debe ser un número entero.")

        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        if not isinstance(descripcion, str):
            raise TypeError("La descripción debe ser texto.")

        self.nombre = nombre.strip()
        self.categoria = categoria.strip()
        self.precio = float(precio)
        self.cantidad = cantidad
        self.descripcion = descripcion.strip()

    def valor_total(self):
        """Calcula el valor total de este recurso."""
        return self.precio * self.cantidad

    def to_dict(self):
        """Convierte el objeto en un diccionario para guardarlo en JSON."""
        return {
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "descripcion": self.descripcion,
        }

    @classmethod
    def from_dict(cls, datos):
        """Reconstruye un objeto Producto y valida los datos almacenados."""
        if not isinstance(datos, dict):
            raise ValueError(
                "Cada producto almacenado debe ser un diccionario."
            )

        faltantes = [
            campo
            for campo in cls.CAMPOS_REQUERIDOS
            if campo not in datos
        ]

        if faltantes:
            raise ValueError(
                f"Faltan campos obligatorios: {', '.join(faltantes)}."
            )

        return cls(
            nombre=datos["nombre"],
            categoria=datos["categoria"],
            precio=datos["precio"],
            cantidad=datos["cantidad"],
            descripcion=datos["descripcion"],
        )

    def __str__(self):
        return (
            f"{self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:,.2f} | "
            f"Cantidad: {self.cantidad} | "
            f"Valor total: ${self.valor_total():,.2f}"
        )