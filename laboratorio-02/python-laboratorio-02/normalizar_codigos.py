codigos = [" p001 ", "P002", "", " p003", "  "]

normalizados = [
    codigo.strip().upper()
    for codigo in codigos
    if codigo.strip() != ""
]

print(normalizados)  # ['P001', 'P002', 'P003']
