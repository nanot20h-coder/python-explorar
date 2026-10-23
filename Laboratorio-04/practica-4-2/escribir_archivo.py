"""Escribe un archivo de texto con codificación UTF-8."""
from pathlib import Path

def escribir_resumen(ruta, contenido):
    ruta = Path(ruta)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    try:
        ruta.write_text(contenido, encoding="utf-8")
    except OSError as exc:
        raise OSError(f"No fue posible escribir en {ruta}.") from exc
    return ruta

if __name__ == "__main__":
    archivo = escribir_resumen("salida/resumen_novexa.txt", "Novexa organiza recursos digitales.")
    print(f"Archivo creado: {archivo.resolve()}")
