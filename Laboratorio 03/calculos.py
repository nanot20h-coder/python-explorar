"""Cálculos básicos de precios para servicios de diseño."""
def calcular_total(precio, cantidad=1):
    if precio < 0 or cantidad < 0:
        raise ValueError("El precio y la cantidad no pueden ser negativos.")
    return precio * cantidad

def aplicar_descuento(total, porcentaje):
    if total < 0:
        raise ValueError("El total no puede ser negativo.")
    if not 0 <= porcentaje <= 100:
        raise ValueError("El descuento debe estar entre 0 y 100.")
    return total * (1 - porcentaje / 100)

if __name__ == "__main__":
    subtotal = calcular_total(45000, 2)
    print(f"Subtotal: ${subtotal:,.0f}")
    print(f"Con descuento: ${aplicar_descuento(subtotal, 10):,.0f}")
