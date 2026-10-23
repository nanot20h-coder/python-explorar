lista1 = ["Ana", "Carlos", "Laura", "Ana"]
lista2 = ["Laura", "Sara", "Carlos", "David"]

participantes = set(lista1) | set(lista2)
print("Personas diferentes:", len(participantes))

participantes.add("Pablo")
participantes.discard("David")

print("Después de los cambios:", participantes)
print("Cantidad final:", len(participantes))
