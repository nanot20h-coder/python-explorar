"""Crea y lee un documento JSON con información de Novexa."""
import json
from pathlib import Path

def guardar_json(ruta, datos):
    archivo = Path(ruta)
    archivo.parent.mkdir(parents=True, exist_ok=True)
    try:
        archivo.write_text(json.dumps(datos, ensure_ascii=False, indent=4), encoding="utf-8")
    except (OSError, TypeError, ValueError) as exc:
        raise RuntimeError(f"No se pudo guardar el JSON: {exc}") from exc

if __name__ == "__main__":
    datos = {"plataforma": "Novexa", "modulo": "identidad visual", "activo": True}
    guardar_json("salida/novexa.json", datos)
    print("JSON guardado en salida/novexa.json")
