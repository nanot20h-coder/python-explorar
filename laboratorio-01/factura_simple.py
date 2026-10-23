nombre_producto = "Teclado"
precio_unitario = 100000.0
cantidad = 2
porcentaje_descuento = 0.10

subtotal = precio_unitario * cantidad
valor_descuento = subtotal * porcentaje_descuento
total = subtotal - valor_descuento

print("-------------------------")
print("FACTURA")
print("-------------------------")
print("Producto:", nombre_producto)
print("Precio unitario: $", precio_unitario)
print("Cantidad:", cantidad)
print("Subtotal: $", subtotal)
print("Descuento: $", valor_descuento)
print("Total: $", total)