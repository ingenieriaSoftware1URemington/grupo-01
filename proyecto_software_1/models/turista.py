class Turista:
    def _init_(self, id_turista: int, nombre: str, telefono: str):
        self.__id_turista = id_turista
        self.__nombre = nombre
        self.__telefono = telefono

    # Getters para el encapsulamiento
    def get_id(self): return self.__id_turista
    def get_nombre(self): return self.__nombre