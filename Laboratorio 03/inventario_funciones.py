"""Funciones para administrar recursos digitales en memoria."""
def agregar_recurso(inventario, nombre, tipo):
    nombre, tipo = nombre.strip(), tipo.strip()
    if not nombre or not tipo:
        raise ValueError("El nombre y el tipo del recurso son obligatorios.")
    inventario.append({"nombre": nombre, "tipo": tipo})
    return inventario

def listar_recursos(inventario):
    return list(inventario)

if __name__ == "__main__":
    recursos = []
    agregar_recurso(recursos, "Logo principal", "logotipo")
    agregar_recurso(recursos, "Paleta corporativa", "colores")
    for recurso in listar_recursos(recursos):
        print(f"{recurso['nombre']} ({recurso['tipo']})")
