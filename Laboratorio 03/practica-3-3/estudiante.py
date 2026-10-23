"""Clase Estudiante como ejercicio de programación orientada a objetos."""
class Estudiante:
    def __init__(self, nombre, ficha):
        if not nombre.strip() or not ficha.strip():
            raise ValueError("Nombre y ficha son obligatorios.")
        self.nombre = nombre.strip()
        self.ficha = ficha.strip()

    def presentarse(self):
        return f"Soy {self.nombre}, estudiante de la ficha {self.ficha}."

if __name__ == "__main__":
    estudiante = Estudiante("Laura", "ADSO-2026")
    print(estudiante.presentarse())
