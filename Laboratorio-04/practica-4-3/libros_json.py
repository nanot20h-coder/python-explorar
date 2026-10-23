"""Ejercicio JSON con un catálogo de recursos, equivalente a un catálogo de libros."""
import json
from pathlib import Path

def guardar_catalogo(recursos, ruta="salida/recursos.json"):
    archivo = Path(ruta)
    archivo.parent.mkdir(parents=True, exist_ok=True)
    archivo.write_text(json.dumps(recursos, ensure_ascii=False, indent=4), encoding="utf-8")

def leer_catalogo(ruta="salida/recursos.json"):
    try:
        datos = json.loads(Path(ruta).read_text(encoding="utf-8"))
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as exc:
        raise ValueError("El archivo JSON está dañado o tiene formato inválido.") from exc
    if not isinstance(datos, list):
        raise ValueError("El catálogo debe contener una lista.")
    return datos

if __name__ == "__main__":
    guardar_catalogo([{"nombre": "Manual de marca", "tipo": "documento"}])
    print(leer_catalogo())
