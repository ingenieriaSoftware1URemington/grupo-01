from abc import ABC, abstractmethod
from datetime import date

class Reserva(ABC):
    def __init__(self, id_reserva: int, fecha: date, turista: object):
        self._id_reserva = id_reserva
        self._fecha = fecha
        self._turista = turista
        self._estado = "Pendiente"  # Aún no confirmada

    @abstractmethod
    def validar_disponibilidad(self) -> bool:
        pass

    # Getters
    def get_id(self) -> int:
        return self._id_reserva

    def get_estado(self) -> str:
        return self._estado

    def get_turista(self) -> object:
        return self._turista

    def get_fecha(self) -> date:
        return self._fecha