"""Cotizador simple de servicios creativos ofrecidos en Novexa."""
SERVICIOS = {"logo": 80000, "manual_marca": 150000, "paquete_redes": 60000}

def cotizar(servicio, cantidad=1):
    if servicio not in SERVICIOS:
        raise ValueError(f"Servicio desconocido. Opciones: {', '.join(SERVICIOS)}")
    if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad < 1:
        raise ValueError("La cantidad debe ser un entero positivo.")
    return SERVICIOS[servicio] * cantidad

if __name__ == "__main__":
    for nombre in SERVICIOS:
        print(f"{nombre}: ${cotizar(nombre):,}")
