edad = int(input("Edad: "))
inscrito = input("¿Está inscrito? (si/no): ").strip().lower()
documentos = int(input("Documentos entregados: "))

edad_ok = edad >= 16
inscrito_ok = inscrito == "si"
documentos_ok = documentos >= 3

if edad_ok and inscrito_ok and documentos_ok:
    print("La solicitud cumple todos los requisitos.")
else:
    print("La solicitud NO cumple los requisitos. Faltan:")
    if not edad_ok:
        print("- La edad debe ser al menos 16 años.")
    if not inscrito_ok:
        print("- La persona debe estar inscrita.")
    if not documentos_ok:
        print("- Se requieren al menos 3 documentos.")
