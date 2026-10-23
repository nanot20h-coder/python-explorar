# Gestor de inventario Novexa — Laboratorio 4

Aplicación de consola para administrar recursos digitales de identidad visual:
logotipos, plantillas, paletas de color, manuales de marca y otros archivos creativos.

## Requisitos
- Python 3.10 o posterior.
- Solo utiliza módulos de la biblioteca estándar (`json`, `csv`, `pathlib`).

## Ejecución
Abre una terminal dentro de esta carpeta y ejecuta:

```bash
python main.py
```

## Archivos generados
- `datos/productos.json`: almacenamiento persistente del inventario.
- `reportes/inventario.csv`: exportación del inventario para hojas de cálculo.

Ambas carpetas se crean automáticamente cuando se guardan datos o se exporta el reporte.
Los productos se validan al crearse y también al cargar los registros JSON. El programa
controla entradas inválidas, errores de lectura/escritura, JSON mal formado y duplicados.
