class Hotel:
    def __init__(self, id_hotel: int, nombre: str, plazas_disponibles: int):
        self.__id_hotel = id_hotel
        self.__nombre = nombre
        self.__plazas_disponibles = plazas_disponibles

    def get_id(self) -> int:
        return self.__id_hotel

    def get_nombre(self) -> str:
        return self.__nombre

    def get_plazas(self) -> int:
        return self.__plazas_disponibles

    def descontar_plaza(self) -> bool:
        if self.__plazas_disponibles > 0:
            self.__plazas_disponibles -= 1
            return True
        return False

    def liberar_plaza(self) -> None:
        self.__plazas_disponibles += 1