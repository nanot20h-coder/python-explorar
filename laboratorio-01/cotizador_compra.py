
print("=============================")
print("      COTIZADOR PYTHON")
print("=============================")


def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto:
            return texto

        print("Este campo no puede estar vacío.")


def pedir_decimal(mensaje, minimo=0, maximo=None):
    while True:
        try:
            valor = float(input(mensaje))

            if valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
            elif maximo is not None and valor > maximo:
                print(f"El valor no puede superar {maximo}.")
            else:
                return valor

        except ValueError:
            print("Error: ingrese un valor numérico válido.")


def pedir_entero(mensaje, minimo=1):
    while True:
        try:
            valor = int(input(mensaje))

            if valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
            else:
                return valor

        except ValueError:
            print("Error: ingrese un número entero válido.")


nombre_cliente = pedir_texto("Nombre del cliente: ")
nombre_producto = pedir_texto("Producto: ")

precio_unitario = pedir_decimal("Precio unitario: ", minimo=0.01)
cantidad = pedir_entero("Cantidad: ")

descuento_porcentaje = pedir_decimal(
    "Descuento (%): ", minimo=0, maximo=100
)

impuesto_porcentaje = pedir_decimal(
    "Impuesto (%): ", minimo=0, maximo=100
)

subtotal = precio_unitario * cantidad

valor_descuento = subtotal * descuento_porcentaje / 100

base = subtotal - valor_descuento

valor_impuesto = base * impuesto_porcentaje / 100

total = base + valor_impuesto

print()
print("-----------------------------")
print("      RESUMEN DE COMPRA")
print("-----------------------------")
print("Cliente:", nombre_cliente)
print("Producto:", nombre_producto)
print(f"Precio unitario: ${precio_unitario:,.2f}")
print("Cantidad:", cantidad)
print(f"Subtotal: ${subtotal:,.2f}")
print(f"Descuento: ${valor_descuento:,.2f}")
print(f"Base: ${base:,.2f}")
print(f"Impuesto: ${valor_impuesto:,.2f}")
print(f"TOTAL: ${total:,.2f}")
