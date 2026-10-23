libros = [
    {"codigo": "L001", "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio": 1967},
    {"codigo": "L002", "titulo": "El coronel no tiene quien le escriba", "autor": "Gabriel García Márquez", "anio": 1961},
    {"codigo": "L003", "titulo": "La vorágine", "autor": "José Eustasio Rivera", "anio": 1924}
]

# Buscar por código
codigo_buscado = input("Código del libro: ").strip()
encontrado = None

for libro in libros:
    if libro["codigo"] == codigo_buscado:
        encontrado = libro
        break

if encontrado is not None:
    print("Código:", encontrado["codigo"])
    print("Título:", encontrado["titulo"])
    print("Autor:", encontrado["autor"])
    print("Año:", encontrado["anio"])
else:
    print("El libro no fue localizado.")

# Ampliación: agregar un libro nuevo sin repetir código
print()
print("--- Agregar un libro nuevo ---")
codigo = input("Código: ").strip()
repetido = False

for libro in libros:
    if libro["codigo"] == codigo:
        repetido = True
        break

if codigo == "":
    print("El código no puede estar vacío.")
elif repetido:
    print("Ese código ya existe.")
else:
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    anio = int(input("Año: "))
    libros.append({"codigo": codigo, "titulo": titulo, "autor": autor, "anio": anio})
    print("Libro agregado.")

print()
for libro in libros:
    print(libro["codigo"], "-", libro["titulo"], "-", libro["autor"], "-", libro["anio"])
