from abc import ABC, abstractmethod
from datetime import date # Usamos date para fechas reales

class Reserva(ABC):
    def _init_(self, id_reserva: int, fecha: date, turista: object):
        self._id_reserva = id_reserva
        self._fecha = fecha # Tipo date
        self._turista = turista # Objeto Turista
        self._estado = "Pendiente"

    @abstractmethod
    def validar_disponibilidad(self):
        # Este método es una "promesa" que los hijos deben cumplir
        pass