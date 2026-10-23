"""Menú interactivo para el gestor de inventario de Novexa."""
from producto import Producto
from inventario import Inventario


def texto(mensaje, opcional=False):
    while True:
        valor = input(mensaje).strip()
        if valor or opcional:
            return valor
        print("Este campo es obligatorio.")


def numero(mensaje, entero=False, minimo=0):
    while True:
        try:
            valor = int(input(mensaje).strip()) if entero else float(input(mensaje).strip())
            if valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Intenta nuevamente.")


def mostrar_producto(p):
    print(f"Nombre: {p.nombre} | Categoría: {p.categoria} | Precio: ${p.precio:,.2f} | "
          f"Cantidad: {p.cantidad} | Valor total: ${p.valor_total():,.2f}")
    print(f"Descripción: {p.descripcion or 'Sin descripción'}")


def registrar(inv):
    p = Producto(texto("Nombre del recurso: "), texto("Categoría: "),
                 numero("Precio unitario: $"), numero("Cantidad: ", entero=True),
                 texto("Descripción (opcional): ", opcional=True))
    inv.registrar(p)
    print("Recurso registrado correctamente.")


def consultar(inv):
    productos = inv.consultar_todos()
    if not productos:
        print("El inventario está vacío.")
    for p in productos:
        mostrar_producto(p)


def buscar(inv):
    p = inv.buscar(texto("Nombre del recurso: "))
    mostrar_producto(p) if p else print("No se encontró el recurso.")


def actualizar(inv):
    nombre = texto("Nombre actual del recurso: ")
    p = inv.buscar(nombre)
    if p is None:
        print("No se encontró el recurso.")
        return
    print("Deja un campo vacío para conservar su valor actual.")
    nombre_nuevo = texto(f"Nombre [{p.nombre}]: ", True) or p.nombre
    categoria = texto(f"Categoría [{p.categoria}]: ", True) or p.categoria
    precio_txt = texto(f"Precio [{p.precio}]: ", True)
    cantidad_txt = texto(f"Cantidad [{p.cantidad}]: ", True)
    descripcion = texto(f"Descripción [{p.descripcion}]: ", True) or p.descripcion
    try:
        precio = p.precio if not precio_txt else float(precio_txt)
        cantidad = p.cantidad if not cantidad_txt else int(cantidad_txt)
        inv.actualizar(nombre, nombre_nuevo, categoria, precio, cantidad, descripcion)
        print("Recurso actualizado correctamente.")
    except ValueError as e:
        print(f"Datos inválidos: {e}")


def eliminar(inv):
    nombre = texto("Nombre del recurso a eliminar: ")
    p = inv.buscar(nombre)
    if p is None:
        print("No se encontró el recurso.")
    elif input(f"¿Eliminar '{p.nombre}'? (s/n): ").strip().lower() == "s":
        inv.eliminar(nombre)
        print("Recurso eliminado.")
    else:
        print("Operación cancelada.")


def informe(inv):
    datos = inv.informe()
    print("\n=== INFORME DEL INVENTARIO NOVEXA ===")
    print(f"Referencias registradas: {datos['referencias']}")
    print(f"Unidades disponibles: {datos['unidades']}")
    print(f"Valor total estimado: ${datos['valor_total']:,.2f}")
    print("Unidades por categoría:")
    if not datos['categorias']:
        print("  Sin datos")
    for categoria, cantidad in sorted(datos['categorias'].items()):
        print(f"  {categoria}: {cantidad}")


def main():
    inv = Inventario()
    acciones = {"1": registrar, "2": consultar, "3": buscar, "4": actualizar, "5": eliminar, "6": informe}
    while True:
        print("\n========== NOVEXA ==========")
        print("1. Registrar recurso")
        print("2. Consultar inventario")
        print("3. Buscar recurso")
        print("4. Actualizar recurso")
        print("5. Eliminar recurso")
        print("6. Generar informe")
        print("0. Salir")
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "0":
            print("Gracias por usar Novexa. ¡Hasta pronto!")
            break
        if opcion not in acciones:
            print("Opción inválida. Selecciona una opción del menú.")
            continue
        try:
            acciones[opcion](inv)
        except (ValueError, TypeError, KeyError) as error:
            print(f"No se pudo completar la operación: {error}")

if __name__ == "__main__":
    main()
