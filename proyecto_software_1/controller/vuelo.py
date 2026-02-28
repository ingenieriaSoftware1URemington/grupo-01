class Vuelo:
    def _init_(self, id_vuelo: int, aerolinea: str, cupos: int):
        self.__id_vuelo = id_vuelo
        self.__aerolinea = aerolinea
        self.__cupos = cupos

    def consultar_cupos(self):
        return self.__cupos

    def descontar_cupo(self):
        if self.__cupos > 0:
            self.__cupos -= 1
            return True
        return False