"""Guarda y consulta un historial sencillo de operaciones."""
from pathlib import Path
from datetime import datetime

RUTA_HISTORIAL = Path("salida/historial_operaciones.txt")

def registrar(operacion):
    if not isinstance(operacion, str) or not operacion.strip():
        raise ValueError("La operación no puede estar vacía.")
    RUTA_HISTORIAL.parent.mkdir(parents=True, exist_ok=True)
    try:
        with RUTA_HISTORIAL.open("a", encoding="utf-8") as archivo:
            archivo.write(f"{datetime.now().isoformat(timespec='seconds')} | {operacion.strip()}\\n")
    except OSError as exc:
        raise OSError("No fue posible guardar el historial.") from exc

def leer_historial():
    try:
        return RUTA_HISTORIAL.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return []
    except OSError as exc:
        raise OSError("No fue posible leer el historial.") from exc

if __name__ == "__main__":
    registrar("Exportación de inventario preparada")
    print("\\n".join(leer_historial()))
