class Sucursal:
    def _init_(self, id_sucursal: int, nombre: str, direccion: str):
        self.__id_sucursal = id_sucursal
        self.__nombre = nombre
        self.__direccion = direccion
        # COMPOSICIÓN: Esta lista guardará todas las reservas hechas en esta oficina.
        self.__lista_reservas = [] 

    # Este método "amarra" la reserva a esta sucursal específica[cite: 38].
    def agregar_reserva(self, reserva):
        self.__lista_reservas.append(reserva)