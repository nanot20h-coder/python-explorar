"""Menú principal del gestor de inventario persistente de Novexa."""

from producto import Producto
from inventario import Inventario
from almacenamiento import AlmacenamientoJSON
from reportes import Reportes


def solicitar_texto(mensaje, permitir_vacio=False):
    """Solicita texto y comprueba que no esté vacío."""
    while True:
        valor = input(mensaje).strip()

        if valor or permitir_vacio:
            return valor

        print("Este campo es obligatorio.")


def solicitar_numero(
    mensaje,
    entero=False,
    minimo=0,
    permitir_vacio=False,
):
    """Solicita un número y valida su tipo y valor mínimo."""
    while True:
        entrada = input(mensaje).strip()

        if permitir_vacio and not entrada:
            return None

        try:
            if entero:
                valor = int(entrada)
            else:
                valor = float(entrada)

            if valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue

            return valor

        except ValueError:
            if entero:
                print("Ingresa un número entero válido.")
            else:
                print("Ingresa un número válido.")


def mostrar_productos(inventario):
    """Lista todos los recursos registrados."""
    productos = inventario.listar()

    print("\n========== RECURSOS REGISTRADOS ==========")

    if not productos:
        print("No hay recursos registrados.")
        return

    for numero, producto in enumerate(productos, start=1):
        print(f"\n{numero}. {producto}")

        if producto.descripcion:
            print(f"   Descripción: {producto.descripcion}")


def registrar_recurso(inventario, almacenamiento):
    """Solicita los datos y registra un nuevo recurso."""
    print("\n========== REGISTRAR RECURSO ==========")

    nombre = solicitar_texto("Nombre del recurso: ")
    categoria = solicitar_texto("Categoría del recurso: ")

    precio = solicitar_numero(
        "Precio unitario: $",
        minimo=0,
    )

    cantidad = solicitar_numero(
        "Cantidad disponible: ",
        entero=True,
        minimo=0,
    )

    descripcion = solicitar_texto(
        "Descripción (opcional): ",
        permitir_vacio=True,
    )

    producto = Producto(
        nombre,
        categoria,
        precio,
        cantidad,
        descripcion,
    )

    inventario.agregar(producto)
    almacenamiento.guardar(inventario)

    print("\n¡Recurso registrado y guardado correctamente!")


def buscar_recurso(inventario):
    """Busca un recurso por su nombre."""
    print("\n========== BUSCAR RECURSO ==========")

    nombre = solicitar_texto(
        "Nombre del recurso que deseas buscar: "
    )

    producto = inventario.buscar(nombre)

    if producto is None:
        print("No se encontró un recurso con ese nombre.")
        return

    print("\nRecurso encontrado:")
    print(producto)

    if producto.descripcion:
        print(f"Descripción: {producto.descripcion}")


def actualizar_recurso(inventario, almacenamiento):
    """Actualiza los datos de un recurso existente."""
    print("\n========== ACTUALIZAR RECURSO ==========")

    nombre_actual = solicitar_texto(
        "Nombre actual del recurso: "
    )

    producto = inventario.buscar(nombre_actual)

    if producto is None:
        print("No se encontró un recurso con ese nombre.")
        return

    print("\nDatos actuales:")
    print(producto)
    print(
        "\nDeja un campo vacío y presiona Enter "
        "para conservar su valor actual."
    )

    nuevo_nombre = input(
        f"Nuevo nombre [{producto.nombre}]: "
    ).strip()

    if not nuevo_nombre:
        nuevo_nombre = producto.nombre

    nueva_categoria = input(
        f"Nueva categoría [{producto.categoria}]: "
    ).strip()

    if not nueva_categoria:
        nueva_categoria = producto.categoria

    nuevo_precio = solicitar_numero(
        f"Nuevo precio [{producto.precio:.2f}]: $",
        minimo=0,
        permitir_vacio=True,
    )

    if nuevo_precio is None:
        nuevo_precio = producto.precio

    nueva_cantidad = solicitar_numero(
        f"Nueva cantidad [{producto.cantidad}]: ",
        entero=True,
        minimo=0,
        permitir_vacio=True,
    )

    if nueva_cantidad is None:
        nueva_cantidad = producto.cantidad

    print(
        f"Descripción actual: "
        f"{producto.descripcion or '(sin descripción)'}"
    )

    nueva_descripcion = input(
        "Nueva descripción "
        "(Enter conserva la actual; escribe - para borrarla): "
    ).strip()

    if nueva_descripcion == "":
        nueva_descripcion = producto.descripcion
    elif nueva_descripcion == "-":
        nueva_descripcion = ""

    inventario.actualizar(
        nombre_actual,
        nuevo_nombre,
        nueva_categoria,
        nuevo_precio,
        nueva_cantidad,
        nueva_descripcion,
    )

    almacenamiento.guardar(inventario)

    print("\n¡Recurso actualizado y cambios guardados!")


def eliminar_recurso(inventario, almacenamiento):
    """Elimina un recurso después de solicitar confirmación."""
    print("\n========== ELIMINAR RECURSO ==========")

    nombre = solicitar_texto(
        "Nombre exacto del recurso que deseas eliminar: "
    )

    producto = inventario.buscar(nombre)

    if producto is None:
        print("No se encontró un recurso con ese nombre.")
        return

    print(f"\nRecurso seleccionado: {producto}")

    confirmacion = input(
        "¿Estás segura de que deseas eliminarlo? (s/n): "
    ).strip().lower()

    if confirmacion == "s":
        inventario.eliminar(nombre)
        almacenamiento.guardar(inventario)

        print("Recurso eliminado y cambios guardados.")
    else:
        print("Operación cancelada.")


def mostrar_informe(inventario):
    """Muestra el informe general del inventario."""
    Reportes.mostrar_resumen(inventario)


def exportar_csv(inventario, reportes):
    """Genera un archivo CSV con los datos del inventario."""
    ruta = reportes.exportar_csv(inventario)

    print("\nReporte exportado correctamente.")
    print(f"Ubicación del archivo: {ruta.resolve()}")


def main():
    """Carga los datos y ejecuta el menú principal."""
    almacenamiento = AlmacenamientoJSON(
        "datos/productos.json"
    )

    reportes = Reportes(
        "reportes/inventario.csv"
    )

    try:
        inventario = almacenamiento.cargar()

    except (OSError, ValueError, TypeError) as error:
        print("\nNo fue posible cargar el inventario.")
        print(f"Detalle: {error}")
        print(
            "Revisa el archivo JSON antes de volver a ejecutar "
            "la aplicación."
        )
        return

    print(
        f"\nSe cargaron {len(inventario.productos)} "
        "recurso(s) del inventario."
    )

    while True:
        print("\n============================================")
        print("       NOVEXA - GESTOR DE INVENTARIO")
        print("============================================")
        print("1. Consultar todos los recursos")
        print("2. Registrar recurso")
        print("3. Buscar recurso")
        print("4. Actualizar recurso")
        print("5. Eliminar recurso")
        print("6. Mostrar informe del inventario")
        print("7. Exportar inventario a CSV")
        print("0. Guardar y salir")
        print("============================================")

        opcion = input("Selecciona una opción: ").strip()

        try:
            if opcion == "1":
                mostrar_productos(inventario)

            elif opcion == "2":
                registrar_recurso(
                    inventario,
                    almacenamiento,
                )

            elif opcion == "3":
                buscar_recurso(inventario)

            elif opcion == "4":
                actualizar_recurso(
                    inventario,
                    almacenamiento,
                )

            elif opcion == "5":
                eliminar_recurso(
                    inventario,
                    almacenamiento,
                )

            elif opcion == "6":
                mostrar_informe(inventario)

            elif opcion == "7":
                exportar_csv(
                    inventario,
                    reportes,
                )

            elif opcion == "0":
                almacenamiento.guardar(inventario)
                print("\nDatos guardados correctamente.")
                print("¡Gracias por utilizar Novexa!")
                break

            else:
                print(
                    "Opción no válida. "
                    "Selecciona una opción del menú."
                )

        except (OSError, ValueError, TypeError, KeyError) as error:
            print(f"\nNo se pudo completar la operación: {error}")


if __name__ == "__main__":
    main()