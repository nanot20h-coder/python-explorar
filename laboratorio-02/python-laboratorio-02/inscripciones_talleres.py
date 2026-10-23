python = {"Ana", "Carlos", "Laura", "Sara", "Mateo"}
java = {"Laura", "Sara", "David", "Pablo"}

print("En al menos un taller:", python | java)
print("En ambos talleres:", python & java)
print("Solo en Python:", python - java)
print("Solo en Java:", java - python)
print("En uno solo de los talleres:", python ^ java)
