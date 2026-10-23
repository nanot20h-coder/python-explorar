"""Lee una cantidad entera positiva de forma segura."""
def leer_cantidad():
    while True:
        entrada = input("Cantidad de recursos a registrar: ").strip()
        try:
            cantidad = int(entrada)
            if cantidad <= 0:
                print("Ingresa un entero mayor que cero.")
                continue
            return cantidad
        except ValueError:
            print("Entrada inválida. Escribe un número entero.")

if __name__ == "__main__":
    print(f"Registrarás {leer_cantidad()} recursos.")
