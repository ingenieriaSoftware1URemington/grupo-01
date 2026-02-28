from .reserva import Reserva
from datetime import date

class ReservaHotel(Reserva):
    def _init_(self, id_reserva: int, fecha: date, turista: object, hotel: object):
        # super() llena los datos del "molde" padre
        super()._init_(id_reserva, fecha, turista)
        self.__hotel = hotel # Agregación del objeto Hotel

    def validar_disponibilidad(self):
        # Mira si el hotel asociado tiene camas
        return self.__hotel.consultar_plazas() > 0