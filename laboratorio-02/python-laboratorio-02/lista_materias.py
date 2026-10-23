materias = ["Matemáticas", "Programación", "Inglés", "Bases de datos"]

for numero, materia in enumerate(materias, start=1):
    print(numero, "-", materia)

# Agrega un elemento y vuelve a ejecutar
materias.append("Redes")
print()
for numero, materia in enumerate(materias, start=1):
    print(numero, "-", materia)
