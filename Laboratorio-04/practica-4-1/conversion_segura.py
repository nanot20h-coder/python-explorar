"""Convierte texto a número usando excepciones."""
def convertir_a_float(texto):
    try:
        numero = float(texto)
    except (TypeError, ValueError) as exc:
        raise ValueError("El valor ingresado no es un número válido.") from exc
    if numero < 0:
        raise ValueError("El valor no puede ser negativo.")
    return numero

if __name__ == "__main__":
    for entrada in ("12000.5", "dato"):
        try:
            print(f"{entrada} -> {convertir_a_float(entrada)}")
        except ValueError as error:
            print(f"Error: {error}")
