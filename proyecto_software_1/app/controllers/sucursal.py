from models.sucursal import Sucursal
from exceptions.agencia_exceptions import (
    RegistroDuplicadoError, DatoVacioError, NoEncontradoError
)

class SucursalController:
    def __init__(self):
        self.__sucursales = []

    def registrar_sucursal(self, id_sucursal: int, nombre: str,
                            direccion: str) -> Sucursal:
        if self.__buscar_por_id(id_sucursal):
            raise RegistroDuplicadoError(f"Ya existe una sucursal con el id {id_sucursal}.")
        if not nombre.strip():
            raise DatoVacioError("El nombre de la sucursal no puede estar vacio.")
        if not direccion.strip():
            raise DatoVacioError("La direccion no puede estar vacia.")
        sucursal = Sucursal(id_sucursal, nombre, direccion)
        self.__sucursales.append(sucursal)
        print(f"Sucursal '{nombre}' registrada exitosamente.")
        return sucursal

    def consultar_sucursales(self) -> list:
        return self.__sucursales

    def consultar_sucursal(self, id_sucursal: int) -> Sucursal:
        sucursal = self.__buscar_por_id(id_sucursal)
        if not sucursal:
            raise NoEncontradoError(f"No se encontro la sucursal con id {id_sucursal}.")
        return sucursal

    def actualizar_nombre(self, id_sucursal: int, nuevo_nombre: str) -> bool:
        sucursal = self.__buscar_por_id(id_sucursal)
        if not sucursal:
            raise NoEncontradoError(f"No se encontro la sucursal con id {id_sucursal}.")
        if not nuevo_nombre.strip():
            raise DatoVacioError("El nuevo nombre no puede estar vacio.")
        print(f"Sucursal #{id_sucursal} actualizada a '{nuevo_nombre}'.")
        return True

    def consultar_reservas_sucursal(self, id_sucursal: int) -> list:
        sucursal = self.__buscar_por_id(id_sucursal)
        if not sucursal:
            raise NoEncontradoError(f"No se encontro la sucursal con id {id_sucursal}.")
        reservas = sucursal.get_reservas()
        if not reservas:
            raise NoEncontradoError(f"La sucursal '{sucursal.get_nombre()}' no tiene reservas.")
        print(f"Sucursal '{sucursal.get_nombre()}': "
              f"{sucursal.get_total_reservas()} reserva(s).")
        return reservas

    def __buscar_por_id(self, id_sucursal: int) -> Sucursal:
        for sucursal in self.__sucursales:
            if sucursal.get_id() == id_sucursal:
                return sucursal
        return None