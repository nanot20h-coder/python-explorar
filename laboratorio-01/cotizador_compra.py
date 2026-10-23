print("=============================")
print("      COTIZADOR PYTHON")
print("=============================")

nombre_cliente = input("Nombre del cliente: ")
nombre_producto = input("Producto: ")
precio_unitario = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
descuento_porcentaje = float(input("Descuento (%): "))
impuesto_porcentaje = float(input("Impuesto (%): "))

descuento = descuento_porcentaje / 100
impuesto = impuesto_porcentaje / 100

subtotal = precio_unitario * cantidad

valor_descuento = subtotal * descuento

base = subtotal - valor_descuento

valor_impuesto = base * impuesto

total = base + valor_impuesto

print()
print("-----------------------------")
print("      RESUMEN DE COMPRA")
print("-----------------------------")
print("Cliente:", nombre_cliente)
print("Producto:", nombre_producto)
print("Precio unitario: $", precio_unitario)
print("Cantidad:", cantidad)
print("Subtotal: $", subtotal)
print("Descuento: $", valor_descuento)
print("Base: $", base)
print("Impuesto: $", valor_impuesto)
print("TOTAL: $", total)