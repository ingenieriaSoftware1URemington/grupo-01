class Sucursal:
    def __init__(self, id_sucursal: int, nombre: str, direccion: str):
        self.__id_sucursal = id_sucursal
        self.__nombre = nombre
        self.__direccion = direccion
        # COMPOSICIÓN: las reservas nacen y viven dentro de la sucursal
        self.__lista_reservas = []

    # Getters
    def get_id(self) -> int:
        return self.__id_sucursal

    def get_nombre(self) -> str:
        return self.__nombre

    def get_direccion(self) -> str:
        return self.__direccion

    # Amarra la reserva a esta sucursal (trazabilidad)
    def agregar_reserva(self, reserva) -> None:
        self.__lista_reservas.append(reserva)

    # Consulta todas las reservas de esta sucursal
    def get_reservas(self) -> list:
        return self.__lista_reservas

    # Consulta cuántas reservas tiene esta sucursal
    def get_total_reservas(self) -> int:
        return len(self.__lista_reservas)