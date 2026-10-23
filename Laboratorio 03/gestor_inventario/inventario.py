"""Operaciones de inventario en memoria para Novexa."""
from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos Producto.")
        if any(p.nombre.casefold() == producto.nombre.casefold() for p in self.productos):
            raise ValueError(f"Ya existe un recurso llamado '{producto.nombre}'.")
        self.productos.append(producto)

    def buscar(self, nombre):
        nombre = nombre.strip().casefold()
        return next((p for p in self.productos if p.nombre.casefold() == nombre), None)

    def eliminar(self, nombre):
        producto = self.buscar(nombre)
        if producto is None:
            raise ValueError(f"No se encontró el recurso '{nombre}'.")
        self.productos.remove(producto)

    def listar(self):
        return list(self.productos)

    def valor_total(self):
        return sum(p.valor_total() for p in self.productos)
