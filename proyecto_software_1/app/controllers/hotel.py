from models.hotel import Hotel
from exceptions.agencia_exceptions import (
    RegistroDuplicadoError, DatoVacioError,
    ValorInvalidoError, NoEncontradoError
)

class HotelController:
    def __init__(self):
        self.__hoteles = []

    def registrar_hotel(self, id_hotel: int, nombre: str, plazas: int) -> Hotel:
        if self.__buscar_por_id(id_hotel):
            raise RegistroDuplicadoError(f"Ya existe un hotel con el id {id_hotel}.")
        if not nombre.strip():
            raise DatoVacioError("El nombre del hotel no puede estar vacio.")
        if plazas < 0:
            raise ValorInvalidoError("Las plazas deben ser mayor o igual a 0.")
        hotel = Hotel(id_hotel, nombre, plazas)
        self.__hoteles.append(hotel)
        print(f"Hotel '{nombre}' registrado exitosamente.")
        return hotel

    def consultar_hoteles(self) -> list:
        return self.__hoteles

    def consultar_disponibilidad(self, id_hotel: int) -> int:
        hotel = self.__buscar_por_id(id_hotel)
        if not hotel:
            raise NoEncontradoError(f"No se encontro el hotel con id {id_hotel}.")
        plazas = hotel.get_plazas()
        print(f"Hotel '{hotel.get_nombre()}': {plazas} plazas disponibles.")
        return plazas

    def actualizar_nombre(self, id_hotel: int, nuevo_nombre: str) -> bool:
        hotel = self.__buscar_por_id(id_hotel)
        if not hotel:
            raise NoEncontradoError(f"No se encontro el hotel con id {id_hotel}.")
        if not nuevo_nombre.strip():
            raise DatoVacioError("El nuevo nombre no puede estar vacio.")
        print(f"Nombre actualizado a '{nuevo_nombre}'.")
        return True

    def __buscar_por_id(self, id_hotel: int) -> Hotel:
        for hotel in self.__hoteles:
            if hotel.get_id() == id_hotel:
                return hotel
        return None