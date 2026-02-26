class Hotel:
    def _init_(self, id_hotel: int, nombre: str, plazas_disponibles: int):
        self.__id_hotel = id_hotel
        self.__nombre = nombre
        self.__plazas_disponibles = plazas_disponibles

    # Avisa cuántas camas quedan libres[cite: 26].
    def get_plazas(self): 
        return self.__plazas_disponibles
    
    # Resta o suma plazas cuando se hace o cancela una reserva[cite: 27].
    def actualizar_plazas(self, cantidad: int):
        self.__plazas_disponibles += cantidad