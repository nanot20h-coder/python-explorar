edad = int(input("Edad: "))
autorizacion = input("¿Tiene autorización? (si/no): ").strip().lower()

if edad >= 18:
    print("Puede ingresar.")
elif autorizacion == "si":
    print("Puede ingresar con autorización.")
else:
    print("Acceso no permitido.")

# Pruebas: (20, no), (17, si), (17, no), (18, no)
