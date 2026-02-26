from .reserva import Reserva
from datetime import date

class ReservaHotel(Reserva):
    def _init_(self, id_reserva: int, fecha: date, turista: object, sucursal: object, hotel: object):
        # Le enviamos los datos generales al "padre" (Reserva)
        super()._init_(id_reserva, fecha, turista, sucursal)
        # AGREGACIÓN: La reserva contiene un hotel, pero el hotel existe por sí solo.
        self.__hotel = hotel 

    # Aquí revisamos específicamente las camas del hotel
    def validar_disponibilidad(self):
        return self.__hotel.get_plazas() > 0