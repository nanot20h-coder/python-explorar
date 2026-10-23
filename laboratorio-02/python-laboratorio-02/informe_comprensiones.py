ventas = [
    {"producto": "Teclado", "categoria": "Periféricos", "total": 150000},
    {"producto": "Mouse", "categoria": "Periféricos", "total": 70000},
    {"producto": "Disco SSD", "categoria": "Componentes", "total": 280000},
    {"producto": "Memoria USB", "categoria": "Accesorios", "total": 45000}
]

# Una transformación primero con for...
altas_for = []
for venta in ventas:
    if venta["total"] > 100000:
        altas_for.append(venta["producto"])

# ...y ahora con comprensión
altas = [venta["producto"] for venta in ventas if venta["total"] > 100000]

categorias = {venta["categoria"] for venta in ventas}
producto_valor = {venta["producto"]: venta["total"] for venta in ventas}
suma_total = sum([venta["total"] for venta in ventas])

print("Ventas superiores a $100.000 (for):", altas_for)
print("Ventas superiores a $100.000 (comprensión):", altas)
print("Categorías diferentes:", categorias)
print("Producto y valor:", producto_valor)
print("Suma de ventas:", suma_total)
