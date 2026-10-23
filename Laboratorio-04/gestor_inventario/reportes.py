"""Generación de informes y exportación a CSV."""

import csv
from pathlib import Path

from inventario import Inventario


class Reportes:
    """Genera reportes del inventario."""

    def __init__(self, ruta_csv="reportes/inventario.csv"):
        self.ruta_csv = Path(ruta_csv)

    @staticmethod
    def mostrar_resumen(inventario):
        """Muestra el número de recursos y el valor del inventario."""
        productos = inventario.productos

        print("\n========== RESUMEN DEL INVENTARIO ==========")

        if not productos:
            print("No hay recursos registrados.")
            return

        unidades_totales = sum(
            producto.cantidad
            for producto in productos
        )

        print(f"Recursos registrados: {len(productos)}")
        print(f"Unidades totales: {unidades_totales}")

        print("\nValor del inventario por categoría:")

        resumen = inventario.resumen_por_categoria()

        for categoria, valor in sorted(resumen.items()):
            print(f"- {categoria}: ${valor:,.2f}")

        print(
            f"\nValor económico total: "
            f"${inventario.valor_total():,.2f}"
        )

        print("============================================")

    def exportar_csv(self, inventario):
        """Exporta los productos a un archivo CSV."""
        if not isinstance(inventario, Inventario):
            raise TypeError(
                "Se esperaba un objeto de tipo Inventario."
            )

        self.ruta_csv.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        columnas = [
            "nombre",
            "categoria",
            "precio",
            "cantidad",
            "descripcion",
            "valor_total",
        ]

        try:
            with self.ruta_csv.open(
                "w",
                newline="",
                encoding="utf-8-sig",
            ) as archivo:
                escritor = csv.DictWriter(
                    archivo,
                    fieldnames=columnas,
                )

                escritor.writeheader()

                for producto in inventario.productos:
                    fila = producto.to_dict()
                    fila["valor_total"] = (
                        f"{producto.valor_total():.2f}"
                    )
                    escritor.writerow(fila)

        except (OSError, csv.Error) as error:
            raise OSError(
                f"No se pudo exportar el reporte CSV: {error}"
            ) from error

        return self.ruta_csv