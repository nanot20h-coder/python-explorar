"""Ejemplo de herencia para distintos recursos digitales."""
class RecursoDigital:
    def __init__(self, nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre es obligatorio.")
        self.nombre = nombre.strip()

    def describir(self):
        return f"Recurso digital: {self.nombre}"

class Logotipo(RecursoDigital):
    def __init__(self, nombre, formato):
        super().__init__(nombre)
        if formato.lower() not in {"svg", "png", "jpg", "pdf"}:
            raise ValueError("Formato no compatible.")
        self.formato = formato.lower()

    def describir(self):
        return f"Logotipo: {self.nombre} (formato {self.formato.upper()})"

if __name__ == "__main__":
    print(RecursoDigital("Paleta de color").describir())
    print(Logotipo("Logo Novexa", "svg").describir())
