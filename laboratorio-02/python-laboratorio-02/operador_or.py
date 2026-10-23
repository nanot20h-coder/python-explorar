for tiene_carnet in (True, False):
    for tiene_autorizacion in (True, False):
        print("Carnet:", tiene_carnet, "| Autorización:", tiene_autorizacion, "->", end=" ")
        if tiene_carnet or tiene_autorizacion:
            print("Puede ingresar.")
        else:
            print("No puede ingresar.")
