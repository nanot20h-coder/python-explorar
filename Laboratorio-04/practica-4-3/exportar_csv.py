"""Exporta recursos de Novexa a un archivo CSV."""
import csv
from pathlib import Path

def exportar_csv(recursos, ruta="salida/recursos.csv"):
    archivo = Path(ruta)
    archivo.parent.mkdir(parents=True, exist_ok=True)
    columnas = ("nombre", "categoria", "precio", "cantidad")
    try:
        with archivo.open("w", newline="", encoding="utf-8-sig") as destino:
            escritor = csv.DictWriter(destino, fieldnames=columnas, extrasaction="ignore")
            escritor.writeheader()
            for recurso in recursos:
                escritor.writerow({col: recurso.get(col, "") for col in columnas})
    except (OSError, csv.Error) as exc:
        raise RuntimeError(f"No fue posible exportar el CSV: {exc}") from exc
    return archivo

if __name__ == "__main__":
    exportar_csv([{"nombre": "Logotipo", "categoria": "Marca", "precio": 80000, "cantidad": 1}])
    print("Archivo CSV creado en salida/recursos.csv")
