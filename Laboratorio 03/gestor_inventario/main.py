"""Aplicación de consola del gestor de recursos digitales de Novexa."""
from producto import Producto
from inventario import Inventario

def main():
    inventario = Inventario()
    inventario.agregar(Producto("Logotipo Novexa", "Logotipos", 80000, 1, "Logo principal"))
    inventario.agregar(Producto("Plantilla para redes", "Plantillas", 25000, 4, "Plantilla editable"))
    print("=== Inventario Novexa ===")
    for producto in inventario.listar():
        print(producto)
    print(f"Valor total del inventario: ${inventario.valor_total():,.0f}")

if __name__ == "__main__":
    main()
