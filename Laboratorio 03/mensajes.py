"""Mensajes reutilizables para informar el resultado de acciones."""
def mensaje_exito(accion):
    return f"Operación completada correctamente: {accion}."

def mensaje_error(accion):
    return f"No se pudo completar la operación: {accion}."

if __name__ == "__main__":
    print(mensaje_exito("guardar el logotipo"))
    print(mensaje_error("cargar el recurso digital"))
