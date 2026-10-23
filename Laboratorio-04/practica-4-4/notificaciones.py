"""Notificaciones simples de operaciones de Novexa."""
class Notificador:
    def enviar(self, destinatario, mensaje):
        raise NotImplementedError("La subclase debe implementar enviar().")

class NotificadorConsola(Notificador):
    def enviar(self, destinatario, mensaje):
        if not destinatario.strip() or not mensaje.strip():
            raise ValueError("Destinatario y mensaje son obligatorios.")
        texto = f"Notificación para {destinatario.strip()}: {mensaje.strip()}"
        print(texto)
        return texto

if __name__ == "__main__":
    notificador = NotificadorConsola()
    notificador.enviar("equipo de diseño", "El logotipo fue actualizado.")
