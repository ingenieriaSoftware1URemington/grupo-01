from .reserva import Reserva
from datetime import date

class ReservaVuelo(Reserva):
    def _init_(self, id_reserva: int, fecha: date, turista: object, sucursal: object, vuelo: object):
        super()._init_(id_reserva, fecha, turista, sucursal)
        # AGREGACIÓN: La reserva contiene un vuelo.
        self.__vuelo = vuelo 

    # Aquí revisamos específicamente las sillas del avión
    def validar_disponibilidad(self):
        return self.__vuelo.get_cupos() > 0