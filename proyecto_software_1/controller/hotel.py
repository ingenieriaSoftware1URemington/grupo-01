class Hotel:
    def _init_(self, id_hotel: int, nombre: str, plazas_disponibles: int):
        self.__id_hotel = id_hotel
        self.__nombre = nombre
        self.__plazas_disponibles = plazas_disponibles

    def consultar_plazas(self):
        return self.__plazas_disponibles

    def descontar_plaza(self):
        # Evita que se vendan más plazas de las que existen
        if self.__plazas_disponibles > 0:
            self.__plazas_disponibles -= 1
            return True
        return False