productos = ["Teclado", "Mouse", "Monitor"]
nuevos = ["Impresora", "Cámara"]

# 1. Reemplazar Mouse
productos[productos.index("Mouse")] = "Mouse inalámbrico"
print("1.", productos)

# 2. Insertar Parlantes en la primera posición
productos.insert(0, "Parlantes")
print("2.", productos)

# 3. Añadir los dos elementos de nuevos
productos.extend(nuevos)
print("3.", productos)

# 4. Eliminar Monitor
productos.remove("Monitor")
print("4.", productos)

# 5. Extraer el último elemento
ultimo = productos.pop()
print("5. Extraído:", ultimo)
print("Resultado final:", productos)
