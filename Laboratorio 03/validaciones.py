"""Validaciones de datos de entrada."""
def validar_texto(texto, campo="valor"):
    if not isinstance(texto, str) or not texto.strip():
        raise ValueError(f"{campo.capitalize()} no puede estar vacío.")
    return texto.strip()

def validar_precio(precio):
    try:
        precio = float(precio)
    except (TypeError, ValueError) as exc:
        raise ValueError("El precio debe ser un número.") from exc
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    return precio
