class Vuelo:
    def __init__(self, id_vuelo: int, aerolinea: str, cupos: int):
        self.__id_vuelo = id_vuelo
        self.__aerolinea = aerolinea
        self.__cupos = cupos

    # Getters
    def get_id(self) -> int:
        return self.__id_vuelo

    def get_aerolinea(self) -> str:
        return self.__aerolinea

    def get_cupos(self) -> int:
        return self.__cupos

    # Descuenta 1 cupo al confirmar reserva
    def descontar_cupo(self) -> bool:
        if self.__cupos > 0:
            self.__cupos -= 1
            return True
        return False

    # Devuelve 1 cupo al cancelar una reserva
    def liberar_cupo(self) -> None:
        self.__cupos += 1