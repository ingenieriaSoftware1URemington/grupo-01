class Turista:
    def __init__(self, id_turista: int, nombre: str, telefono: str):
        self.__id_turista = id_turista
        self.__nombre = nombre
        self.__telefono = telefono

    def get_id(self) -> int:
        return self.__id_turista

    def get_nombre(self) -> str:
        return self.__nombre

    def get_telefono(self) -> str:
        return self.__telefono