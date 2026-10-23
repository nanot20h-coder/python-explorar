"""Lógica de negocio del inventario digital de Novexa."""
from producto import Producto

class Inventario:
    def __init__(self):
        self._productos = []

    @property
    def productos(self):
        return list(self._productos)

    def registrar(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden registrar objetos Producto.")
        if self.buscar(producto.nombre):
            raise ValueError(f"Ya existe un recurso llamado '{producto.nombre}'.")
        self._productos.append(producto)

    def consultar_todos(self):
        return self.productos

    def buscar(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("Debes escribir un nombre para buscar.")
        clave = nombre.strip().casefold()
        return next((p for p in self._productos if p.nombre.casefold() == clave), None)

    def actualizar(self, nombre_actual, nombre, categoria, precio, cantidad, descripcion=""):
        actual = self.buscar(nombre_actual)
        if actual is None:
            raise KeyError(f"No existe el recurso '{nombre_actual}'.")
        nuevo = Producto(nombre, categoria, precio, cantidad, descripcion)
        duplicado = self.buscar(nuevo.nombre)
        if duplicado is not None and duplicado is not actual:
            raise ValueError(f"Ya existe otro recurso llamado '{nuevo.nombre}'.")
        actual.nombre, actual.categoria = nuevo.nombre, nuevo.categoria
        actual.precio, actual.cantidad = nuevo.precio, nuevo.cantidad
        actual.descripcion = nuevo.descripcion
        return actual

    def eliminar(self, nombre):
        producto = self.buscar(nombre)
        if producto is None:
            raise KeyError(f"No existe el recurso '{nombre}'.")
        self._productos.remove(producto)
        return producto

    def valor_total(self):
        return sum(p.valor_total() for p in self._productos)

    def informe(self):
        categorias = {}
        for p in self._productos:
            categorias[p.categoria] = categorias.get(p.categoria, 0) + p.cantidad
        return {"referencias": len(self._productos), "unidades": sum(p.cantidad for p in self._productos),
                "valor_total": self.valor_total(), "categorias": categorias}
