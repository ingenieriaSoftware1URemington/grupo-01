class Vuelo:
    def _init_(self, id_vuelo: int, aerolinea: str, cupos: int):
        self.__id_vuelo = id_vuelo
        self.__aerolinea = aerolinea
        self.__cupos = cupos

    # Avisa cuántas sillas quedan en el avión
    def get_cupos(self): 
        return self.__cupos
    
    # Actualiza las sillas después de vender un tiquete
    def actualizar_cupos(self, cantidad: int):
        self.__cupos += cantidad