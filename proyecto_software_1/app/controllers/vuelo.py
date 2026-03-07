from models.vuelo import Vuelo
from exceptions.agencia_exceptions import (
    RegistroDuplicadoError, DatoVacioError,
    ValorInvalidoError, NoEncontradoError
)

class VueloController:
    def __init__(self):
        self.__vuelos = []

    def registrar_vuelo(self, id_vuelo: int, aerolinea: str, cupos: int) -> Vuelo:
        if self.__buscar_por_id(id_vuelo):
            raise RegistroDuplicadoError(f"Ya existe un vuelo con el id {id_vuelo}.")
        if not aerolinea.strip():
            raise DatoVacioError("El nombre de la aerolinea no puede estar vacio.")
        if cupos <= 0:
            raise ValorInvalidoError("Los cupos deben ser mayor a 0.")
        vuelo = Vuelo(id_vuelo, aerolinea, cupos)
        self.__vuelos.append(vuelo)
        print(f"Vuelo '{aerolinea}' registrado exitosamente.")
        return vuelo

    def consultar_vuelos(self) -> list:
        return self.__vuelos

    def consultar_vuelo(self, id_vuelo: int) -> Vuelo:
        vuelo = self.__buscar_por_id(id_vuelo)
        if not vuelo:
            raise NoEncontradoError(f"No se encontro el vuelo con id {id_vuelo}.")
        return vuelo

    def consultar_disponibilidad(self, id_vuelo: int) -> int:
        vuelo = self.__buscar_por_id(id_vuelo)
        if not vuelo:
            raise NoEncontradoError(f"No se encontro el vuelo con id {id_vuelo}.")
        cupos = vuelo.get_cupos()
        print(f"Vuelo '{vuelo.get_aerolinea()}': {cupos} cupos disponibles.")
        return cupos

    def actualizar_aerolinea(self, id_vuelo: int, nueva_aerolinea: str) -> bool:
        vuelo = self.__buscar_por_id(id_vuelo)
        if not vuelo:
            raise NoEncontradoError(f"No se encontro el vuelo con id {id_vuelo}.")
        if not nueva_aerolinea.strip():
            raise DatoVacioError("El nombre de la aerolinea no puede estar vacio.")
        print(f"Vuelo #{id_vuelo} actualizado a '{nueva_aerolinea}'.")
        return True

    def __buscar_por_id(self, id_vuelo: int) -> Vuelo:
        for vuelo in self.__vuelos:
            if vuelo.get_id() == id_vuelo:
                return vuelo
        return None