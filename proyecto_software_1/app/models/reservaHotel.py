from .reserva import Reserva
from datetime import date

class ReservaHotel(Reserva):
    def __init__(self, id_reserva: int, fecha: date, turista: object, hotel: object):
        super().__init__(id_reserva, fecha, turista)
        self.__hotel = hotel  # AGREGACIÓN

    def get_hotel(self) -> object:
        return self.__hotel

    # Consulta si el hotel tiene plazas
    def validar_disponibilidad(self) -> bool:
        return self.__hotel.get_plazas() > 0

    # Confirma la reserva descontando la plaza en el hotel
    def confirmar(self) -> bool:
        if self.validar_disponibilidad():
            self.__hotel.descontar_plaza()
            self._estado = "Confirmada"
            return True
        self._estado = "Rechazada"
        return False

    # Cancela la reserva liberando la plaza en el hotel
    def cancelar(self) -> None:
        if self._estado == "Confirmada":
            self.__hotel.liberar_plaza()
            self._estado = "Cancelada"