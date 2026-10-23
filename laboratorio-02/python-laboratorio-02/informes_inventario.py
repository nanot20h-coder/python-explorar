productos = [
    {"nombre": "Teclado", "precio": 85000, "cantidad": 4},
    {"nombre": "Mouse", "precio": 45000, "cantidad": 0},
    {"nombre": "Monitor", "precio": 700000, "cantidad": 2}
]

sin_existencias = [p["nombre"] for p in productos if p["cantidad"] == 0]
caros = [p["nombre"] for p in productos if p["precio"] > 100000]
cantidades_distintas = {p["cantidad"] for p in productos}
nombre_precio = {p["nombre"]: p["precio"] for p in productos}

print("Sin existencias:", sin_existencias)
print("Precio superior a $100.000:", caros)
print("Cantidades diferentes:", cantidades_distintas)
print("Nombre y precio:", nombre_precio)
