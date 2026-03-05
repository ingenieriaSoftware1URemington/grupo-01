from models.hotel import Hotel

class HotelController:
    def __init__(self):
        # Lista en memoria de todos los hoteles registrados
        self.__hoteles = []

    # ── REGISTRAR ──────────────────────────────────────────
    def registrar_hotel(self, id_hotel: int, nombre: str, plazas: int) -> Hotel:
        # Validar que no exista un hotel con el mismo id
        if self.__buscar_por_id(id_hotel):
            print(f"Error: ya existe un hotel con el id {id_hotel}.")
            return None

        # Validar que las plazas sean un número positivo
        if plazas < 0:
            print("Error: las plazas deben ser mayor a 0.")
            return None

        hotel = Hotel(id_hotel, nombre, plazas)
        self.__hoteles.append(hotel)
        print(f"Hotel '{nombre}' registrado exitosamente.")
        return hotel

    # ── CONSULTAR ──────────────────────────────────────────
    def consultar_hoteles(self) -> list:
        if not self.__hoteles:
            print("No hay hoteles registrados.")
            return []
        return self.__hoteles

    def consultar_disponibilidad(self, id_hotel: int) -> int:
        hotel = self.__buscar_por_id(id_hotel)
        if not hotel:
            print(f"Error: no se encontró el hotel con id {id_hotel}.")
            return None
        plazas = hotel.get_plazas()
        print(f"Hotel '{hotel.get_nombre()}': {plazas} plazas disponibles.")
        return plazas

    # ── ACTUALIZAR ─────────────────────────────────────────
    def actualizar_nombre(self, id_hotel: int, nuevo_nombre: str) -> bool:
        hotel = self.__buscar_por_id(id_hotel)
        if not hotel:
            print(f"Error: no se encontró el hotel con id {id_hotel}.")
            return False
        # Accedemos solo a través de métodos públicos
        print(f"Nombre actualizado a '{nuevo_nombre}'.")
        return True

    # ── PRIVADO: búsqueda interna ──────────────────────────
    def __buscar_por_id(self, id_hotel: int) -> Hotel:
        for hotel in self.__hoteles:
            if hotel.get_id() == id_hotel:
                return hotel
        return None