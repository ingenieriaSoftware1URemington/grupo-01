from abc import ABC, abstractmethod
from datetime import date # Importamos esto para usar fechas reales

# ABC significa que es una clase abstracta: no puedes crear una "Reserva" vacía.
class Reserva(ABC):
    def _init_(self, id_reserva: int, fecha: date, turista: object, sucursal: object):
        self._id_reserva = id_reserva
        self._fecha = fecha # Aquí guardamos la fecha como tipo date
        self._turista = turista # Quién viaja
        self._sucursal = sucursal # Qué oficina lo vendió (Trazabilidad)[cite: 8].
        self._estado = "Confirmada"

    # Obliga a las clases hijas a revisar si hay cupo antes de vender[cite: 39].
    @abstractmethod
    def validar_disponibilidad(self):
        pass