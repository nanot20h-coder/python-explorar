"""Lee una edad entera entre 0 y 120 con validación."""
def leer_edad():
    while True:
        try:
            edad = int(input("Ingresa tu edad: ").strip())
            if 0 <= edad <= 120:
                return edad
            print("La edad debe estar entre 0 y 120.")
        except ValueError:
            print("Entrada inválida: escribe un número entero.")

if __name__ == "__main__":
    print(f"Edad registrada: {leer_edad()}")
