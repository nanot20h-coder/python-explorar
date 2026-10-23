calificaciones = [4.0, 3.5, 2.8, 4.5, 4.0, 5.0]

print("Tres primeras:", calificaciones[:3])
print("Dos últimas:", calificaciones[-2:])
print("Cantidad total:", len(calificaciones))
print("Ordenadas:", sorted(calificaciones))
print("Original (sin cambios):", calificaciones)
print("Veces que aparece 4.0:", calificaciones.count(4.0))
#count es una funcion que sirve para contrar cuantas veces se repite un elemento 