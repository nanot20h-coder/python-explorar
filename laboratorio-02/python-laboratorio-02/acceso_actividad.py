# Se prueban las cuatro combinaciones de True y False
#for es un ciclo es decir se repite 
for esta_inscrito in (True, False):
    for tiene_documento in (True, False):
        print("Inscrito:", esta_inscrito, "| Documento:", tiene_documento, "->", end=" ")
        if esta_inscrito and tiene_documento:
            print("Puede ingresar.")
        else:
            print("No cumple todos los requisitos.")
