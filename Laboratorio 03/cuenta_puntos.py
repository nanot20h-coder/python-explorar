"""Cuenta de puntos de fidelidad para clientes de Novexa."""
class CuentaPuntos:
    def __init__(self, titular, puntos=0):
        if not titular.strip():
            raise ValueError("El titular es obligatorio.")
        if not isinstance(puntos, int) or puntos < 0:
            raise ValueError("Los puntos deben ser un entero no negativo.")
        self.titular = titular.strip()
        self.puntos = puntos

    def acumular(self, puntos):
        if not isinstance(puntos, int) or puntos <= 0:
            raise ValueError("Los puntos a acumular deben ser un entero positivo.")
        self.puntos += puntos

    def canjear(self, puntos):
        if not isinstance(puntos, int) or puntos <= 0:
            raise ValueError("Los puntos a canjear deben ser un entero positivo.")
        if puntos > self.puntos:
            raise ValueError("No hay suficientes puntos.")
        self.puntos -= puntos

if __name__ == "__main__":
    cuenta = CuentaPuntos("Empresa Demo", 50)
    cuenta.acumular(20)
    cuenta.canjear(10)
    print(f"{cuenta.titular}: {cuenta.puntos} puntos")
