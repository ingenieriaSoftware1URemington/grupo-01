from .reserva import Reserva
from datetime import date

class ReservaVuelo(Reserva):
    def __init__(self, id_reserva: int, fecha: date, turista: object, vuelo: object):
        super().__init__(id_reserva, fecha, turista)
        self.__vuelo = vuelo  # AGREGACIÓN

    def get_vuelo(self) -> object:
        return self.__vuelo

    # Consulta si el vuelo tiene cupos disponibles
    def validar_disponibilidad(self) -> bool:
        return self.__vuelo.get_cupos() > 0

    # Confirma la reserva descontando el cupo en el vuelo
    def confirmar(self) -> bool:
        if self.validar_disponibilidad():
            self.__vuelo.descontar_cupo()
            self._estado = "Confirmada"
            return True
        self._estado = "Rechazada"
        return False

    # Cancela la reserva liberando el cupo en el vuelo
    def cancelar(self) -> None:
        if self._estado == "Confirmada":
            self.__vuelo.liberar_cupo()
            self._estado = "Cancelada"