"""Registra eventos en una bitácora de texto."""
from datetime import datetime
from pathlib import Path

def registrar_evento(mensaje, ruta="salida/bitacora.txt"):
    if not isinstance(mensaje, str) or not mensaje.strip():
        raise ValueError("El mensaje de bitácora no puede estar vacío.")
    archivo = Path(ruta)
    archivo.parent.mkdir(parents=True, exist_ok=True)
    linea = f"[{datetime.now().isoformat(timespec='seconds')}] {mensaje.strip()}\\n"
    try:
        with archivo.open("a", encoding="utf-8") as destino:
            destino.write(linea)
    except OSError as exc:
        raise OSError(f"No fue posible registrar el evento en {archivo}.") from exc

if __name__ == "__main__":
    registrar_evento("Se guardó un recurso de marca.")
    print("Evento agregado a la bitácora.")
