"""Almacenamiento persistente mediante archivos JSON."""

import json
from pathlib import Path

from producto import Producto
from inventario import Inventario


class AlmacenamientoJSON:
    """Guarda y recupera el inventario desde un archivo JSON."""

    def __init__(self, ruta="datos/productos.json"):
        self.ruta = Path(ruta)

    def guardar(self, inventario):
        """Guarda todos los productos registrados en formato JSON."""
        if not isinstance(inventario, Inventario):
            raise TypeError(
                "Se esperaba un objeto de tipo Inventario."
            )

        self.ruta.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        datos = [
            producto.to_dict()
            for producto in inventario.productos
        ]

        archivo_temporal = self.ruta.with_suffix(
            self.ruta.suffix + ".tmp"
        )

        try:
            archivo_temporal.write_text(
                json.dumps(
                    datos,
                    ensure_ascii=False,
                    indent=4,
                ),
                encoding="utf-8",
            )

            archivo_temporal.replace(self.ruta)

        except (OSError, TypeError, ValueError) as error:
            try:
                if archivo_temporal.exists():
                    archivo_temporal.unlink()
            except OSError:
                pass

            raise OSError(
                f"No se pudo guardar el inventario: {error}"
            ) from error

    def cargar(self):
        """Lee el JSON y reconstruye los objetos del inventario."""
        if not self.ruta.exists():
            return Inventario()

        try:
            contenido = self.ruta.read_text(encoding="utf-8")
            datos = json.loads(contenido)

        except json.JSONDecodeError as error:
            raise ValueError(
                f"El archivo '{self.ruta}' contiene JSON inválido."
            ) from error

        except OSError as error:
            raise OSError(
                f"No se pudo leer el archivo '{self.ruta}': {error}"
            ) from error

        if not isinstance(datos, list):
            raise ValueError(
                "El archivo JSON debe contener una lista de productos."
            )

        productos = []

        for posicion, registro in enumerate(datos, start=1):
            try:
                producto = Producto.from_dict(registro)
                productos.append(producto)

            except (KeyError, TypeError, ValueError) as error:
                raise ValueError(
                    f"El producto de la posición {posicion} "
                    f"contiene datos inválidos: {error}"
                ) from error

        try:
            return Inventario(productos)

        except (TypeError, ValueError) as error:
            raise ValueError(
                f"El inventario guardado contiene datos duplicados "
                f"o inválidos: {error}"
            ) from error