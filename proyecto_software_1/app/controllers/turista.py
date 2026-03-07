from models.turista import Turista
from exceptions.agencia_exceptions import (
    RegistroDuplicadoError, DatoVacioError, NoEncontradoError
)

class TuristaController:
    def __init__(self):
        self.__turistas = []

    def registrar_turista(self, id_turista: int, nombre: str,
                           telefono: str) -> Turista:
        if self.__buscar_por_id(id_turista):
            raise RegistroDuplicadoError(f"Ya existe un turista con el id {id_turista}.")
        if not nombre.strip():
            raise DatoVacioError("El nombre del turista no puede estar vacio.")
        if not telefono.strip():
            raise DatoVacioError("El telefono no puede estar vacio.")
        turista = Turista(id_turista, nombre, telefono)
        self.__turistas.append(turista)
        print(f"Turista '{nombre}' registrado exitosamente.")
        return turista

    def consultar_turistas(self) -> list:
        return self.__turistas

    def consultar_turista(self, id_turista: int) -> Turista:
        turista = self.__buscar_por_id(id_turista)
        if not turista:
            raise NoEncontradoError(f"No se encontro el turista con id {id_turista}.")
        return turista

    def actualizar_telefono(self, id_turista: int,
                             nuevo_telefono: str) -> bool:
        turista = self.__buscar_por_id(id_turista)
        if not turista:
            raise NoEncontradoError(f"No se encontro el turista con id {id_turista}.")
        if not nuevo_telefono.strip():
            raise DatoVacioError("El nuevo telefono no puede estar vacio.")
        print(f"Telefono de '{turista.get_nombre()}' "
              f"actualizado a '{nuevo_telefono}'.")
        return True

    def buscar_por_nombre(self, nombre: str) -> list:
        resultado = [t for t in self.__turistas
                     if nombre.lower() in t.get_nombre().lower()]
        if not resultado:
            raise NoEncontradoError(f"No se encontraron turistas con el nombre '{nombre}'.")
        return resultado

    def __buscar_por_id(self, id_turista: int) -> Turista:
        for turista in self.__turistas:
            if turista.get_id() == id_turista:
                return turista
        return None