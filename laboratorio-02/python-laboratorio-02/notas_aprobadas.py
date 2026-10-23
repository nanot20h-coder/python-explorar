notas = [2.5, 3.0, 4.8, 1.9, 3.7, 5.0]

aprobadas = [nota for nota in notas if nota >= 3.0]
no_aprobadas = [nota for nota in notas if nota < 3.0]
dobles = [nota * 2 for nota in notas]

print("Aprobadas:", aprobadas)
print("No aprobadas:", no_aprobadas)
print("Multiplicadas por 2:", dobles)
