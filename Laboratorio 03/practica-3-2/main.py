"""Demostración de operaciones y validaciones de Novexa."""
from operaciones import sumar, restar, multiplicar, dividir
from validaciones import validar_texto, validar_precio

def main():
    servicio = validar_texto(" Diseño de logotipo ", "servicio")
    precio = validar_precio("85000")
    print(f"Servicio: {servicio}")
    print(f"Presupuesto base: ${precio:,.0f}")
    print(f"Dos servicios: ${multiplicar(precio, 2):,.0f}")
    print(f"Suma de ejemplo: {sumar(12, 8)}")
    print(f"Resta de ejemplo: {restar(12, 8)}")
    print(f"División de ejemplo: {dividir(12, 3)}")

if __name__ == "__main__":
    main()
