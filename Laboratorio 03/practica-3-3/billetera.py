"""Billetera sencilla para simular un presupuesto de diseño."""
class Billetera:
    def __init__(self, saldo=0):
        if not isinstance(saldo, (int, float)) or saldo < 0:
            raise ValueError("El saldo inicial debe ser un número no negativo.")
        self.saldo = float(saldo)

    def ingresar(self, cantidad):
        self._validar_cantidad(cantidad)
        self.saldo += cantidad

    def pagar(self, cantidad):
        self._validar_cantidad(cantidad)
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= cantidad

    @staticmethod
    def _validar_cantidad(cantidad):
        if not isinstance(cantidad, (int, float)) or isinstance(cantidad, bool) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un número positivo.")

if __name__ == "__main__":
    billetera = Billetera(100000)
    billetera.pagar(25000)
    print(f"Saldo para servicios: ${billetera.saldo:,.0f}")
