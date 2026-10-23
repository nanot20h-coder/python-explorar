"""Lógica de negocio del inventario de recursos digitales."""

from producto import Producto


class Inventario:
    """Administra los productos sin depender del menú de consola."""

    def __init__(self, productos=None):
        self._productos = []

        for producto in productos or []:
            self.agregar(producto)

    @property
    def productos(self):
        """Devuelve una copia de los productos registrados."""
        return list(self._productos)

    def agregar(self, producto):
        """Registra un producto si no existe otro con el mismo nombre."""
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos de tipo Producto.")

        if self.buscar(producto.nombre) is not None:
            raise ValueError(
                f"Ya existe un recurso llamado '{producto.nombre}'."
            )

        self._productos.append(producto)
        return producto

    def listar(self):
        """Devuelve todos los productos registrados."""
        return self.productos

    def buscar(self, nombre):
        """Busca un producto por su nombre, sin distinguir mayúsculas."""
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("Debes ingresar un nombre válido.")

        nombre_buscado = nombre.strip().casefold()

        for producto in self._productos:
            if producto.nombre.casefold() == nombre_buscado:
                return producto

        return None

    def actualizar(
        self,
        nombre_actual,
        nuevo_nombre,
        nueva_categoria,
        nuevo_precio,
        nueva_cantidad,
        nueva_descripcion,
    ):
        """Actualiza un producto después de validar sus nuevos datos."""
        producto_actual = self.buscar(nombre_actual)

        if producto_actual is None:
            raise KeyError(
                f"No se encontró el recurso '{nombre_actual}'."
            )

        nombre_normalizado = nuevo_nombre.strip().casefold()

        for otro_producto in self._productos:
            if (
                otro_producto is not producto_actual
                and otro_producto.nombre.casefold() == nombre_normalizado
            ):
                raise ValueError(
                    f"Ya existe otro recurso llamado '{nuevo_nombre}'."
                )

        # Se crea primero un objeto validado para evitar actualizaciones parciales.
        producto_actualizado = Producto(
            nuevo_nombre,
            nueva_categoria,
            nuevo_precio,
            nueva_cantidad,
            nueva_descripcion,
        )

        indice = self._productos.index(producto_actual)
        self._productos[indice] = producto_actualizado

        return producto_actualizado

    def eliminar(self, nombre):
        """Elimina un producto del inventario."""
        producto = self.buscar(nombre)

        if producto is None:
            raise KeyError(
                f"No se encontró el recurso '{nombre}'."
            )

        self._productos.remove(producto)
        return producto

    def valor_total(self):
        """Calcula el valor económico de todos los productos."""
        return sum(
            producto.valor_total()
            for producto in self._productos
        )

    def resumen_por_categoria(self):
        """Calcula el valor acumulado de cada categoría."""
        resumen = {}

        for producto in self._productos:
            categoria = producto.categoria
            resumen[categoria] = (
                resumen.get(categoria, 0)
                + producto.valor_total()
            )

        return resumen