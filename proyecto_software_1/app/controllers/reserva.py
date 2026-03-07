from models.reservaHotel import ReservaHotel
from models.reservaVuelo import ReservaVuelo
from exceptions.agencia_exceptions import (
    NoEncontradoError, SinDisponibilidadError, EstadoInvalidoError
)
from datetime import date

class ReservaController:
    def __init__(self):
        self.__reservas = []
        self.__contador_id = 0

    def __generar_id(self) -> int:
        self.__contador_id += 1
        return self.__contador_id

    def crear_reserva_hotel(self, turista: object, hotel: object,
                             sucursal: object, fecha: date) -> ReservaHotel:
        reserva = ReservaHotel(self.__generar_id(), fecha, turista, hotel)
        if not reserva.confirmar():
            raise SinDisponibilidadError(
                f"No hay plazas disponibles en '{hotel.get_nombre()}'."
            )
        self.__reservas.append(reserva)
        sucursal.agregar_reserva(reserva)
        print(f"Reserva #{reserva.get_id()} de hotel confirmada "
              f"para '{turista.get_nombre()}'.")
        return reserva

    def crear_reserva_vuelo(self, turista: object, vuelo: object,
                             sucursal: object, fecha: date) -> ReservaVuelo:
        reserva = ReservaVuelo(self.__generar_id(), fecha, turista, vuelo)
        if not reserva.confirmar():
            raise SinDisponibilidadError(
                f"No hay cupos disponibles en vuelo '{vuelo.get_aerolinea()}'."
            )
        self.__reservas.append(reserva)
        sucursal.agregar_reserva(reserva)
        print(f"Reserva #{reserva.get_id()} de vuelo confirmada "
              f"para '{turista.get_nombre()}'.")
        return reserva

    def cancelar_reserva(self, id_reserva: int) -> bool:
        reserva = self.__buscar_por_id(id_reserva)
        if not reserva:
            raise NoEncontradoError(f"No se encontro la reserva #{id_reserva}.")
        if reserva.get_estado() != "Confirmada":
            raise EstadoInvalidoError(
                f"La reserva #{id_reserva} no esta confirmada, "
                f"su estado actual es '{reserva.get_estado()}'."
            )
        reserva.cancelar()
        print(f"Reserva #{id_reserva} cancelada exitosamente.")
        return True

    def consultar_reservas(self) -> list:
        return self.__reservas

    def consultar_por_turista(self, id_turista: int) -> list:
        resultado = [r for r in self.__reservas
                     if r.get_turista().get_id() == id_turista]
        if not resultado:
            raise NoEncontradoError(
                f"No se encontraron reservas para el turista #{id_turista}."
            )
        return resultado

    def __buscar_por_id(self, id_reserva: int) -> object:
        for reserva in self.__reservas:
            if reserva.get_id() == id_reserva:
                return reserva
        return None