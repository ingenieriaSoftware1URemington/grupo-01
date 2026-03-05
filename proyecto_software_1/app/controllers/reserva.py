from models.reservaHotel import ReservaHotel
from models.reservaVuelo import ReservaVuelo
from datetime import date

class ReservaController:
    def _init_(self):
        # Lista en memoria de todas las reservas
        self.__reservas = []
        self.__contador_id = 0  # Genera ids automáticamente

    # ── PRIVADO: genera id único ───────────────────────────
    def __generar_id(self) -> int:
        self.__contador_id += 1
        return self.__contador_id

    # ── CREAR RESERVA HOTEL ────────────────────────────────
    def crear_reserva_hotel(self, turista: object, hotel: object,
                             sucursal: object, fecha: date) -> ReservaHotel:
        reserva = ReservaHotel(self.__generar_id(), fecha, turista, hotel)

        if reserva.confirmar():
            self.__reservas.append(reserva)
            sucursal.agregar_reserva(reserva)  # Trazabilidad
            print(f"Reserva #{reserva.get_id()} de hotel confirmada "
                  f"para '{turista.get_nombre()}'.")
            return reserva

        print(f"Error: no hay plazas disponibles en '{hotel.get_nombre()}'.")
        return None

    # ── CREAR RESERVA VUELO ────────────────────────────────
    def crear_reserva_vuelo(self, turista: object, vuelo: object,
                             sucursal: object, fecha: date) -> ReservaVuelo:
        reserva = ReservaVuelo(self.__generar_id(), fecha, turista, vuelo)

        if reserva.confirmar():
            self.__reservas.append(reserva)
            sucursal.agregar_reserva(reserva)  # Trazabilidad
            print(f"Reserva #{reserva.get_id()} de vuelo confirmada "
                  f"para '{turista.get_nombre()}'.")
            return reserva

        print(f"Error: no hay cupos disponibles en vuelo "
              f"'{vuelo.get_aerolinea()}'.")
        return None

    # ── CANCELAR RESERVA ───────────────────────────────────
    def cancelar_reserva(self, id_reserva: int) -> bool:
        reserva = self.__buscar_por_id(id_reserva)

        if not reserva:
            print(f"Error: no se encontró la reserva #{id_reserva}.")
            return False

        if reserva.get_estado() != "Confirmada":
            print(f"Error: la reserva #{id_reserva} "
                  f"no está confirmada.")
            return False

        reserva.cancelar()
        print(f"Reserva #{id_reserva} cancelada exitosamente.")
        return True

    # ── CONSULTAR ──────────────────────────────────────────
    def consultar_reservas(self) -> list:
        if not self.__reservas:
            print("No hay reservas registradas.")
            return []
        return self.__reservas

    def consultar_por_turista(self, id_turista: int) -> list:
        resultado = [r for r in self.__reservas
                     if r.get_turista().get_id() == id_turista]
        if not resultado:
            print(f"No se encontraron reservas para el turista #{id_turista}.")
        return resultado

    # ── PRIVADO: búsqueda interna ──────────────────────────
    def __buscar_por_id(self, id_reserva: int) -> object:
        for reserva in self.__reservas:
            if reserva.get_id() == id_reserva:
                return reserva
        return None