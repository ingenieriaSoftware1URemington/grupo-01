from .reserva import Reserva
from datetime import date

class ReservaVuelo(Reserva):
    def _init_(self, id_reserva: int, fecha: date, turista: object, vuelo: object):
        super()._init_(id_reserva, fecha, turista)
        self.__vuelo = vuelo # Agregación del objeto Vuelo

    def validar_disponibilidad(self):
        return self.__vuelo.consultar_cupos() > 0