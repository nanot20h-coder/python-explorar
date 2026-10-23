categorias = ("Periféricos", "Componentes", "Accesorios", "Papelería")

for numero, categoria in enumerate(categorias, start=1):
    print(numero, "-", categoria)

elegida = input("Categoría: ").strip()

if elegida in categorias:
    print("La categoría pertenece a las opciones permitidas.")
else:
    print("La categoría no está permitida.")

print("Categorías disponibles:", len(categorias))
