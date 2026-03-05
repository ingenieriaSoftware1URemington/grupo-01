from datetime import date

from controllers.hotel import HotelController
from controllers.vuelo import VueloController
from controllers.turista import TuristaController
from controllers.sucursal import SucursalController
from controllers.reserva import ReservaController

def separador(titulo: str):
    print("\n" + "=" * 50)
    print(f"  {titulo}")
    print("=" * 50)

def main():

    # ── INSTANCIAR CONTROLADORES ───────────────────────────
    hotel_ctrl     = HotelController()
    vuelo_ctrl     = VueloController()
    turista_ctrl   = TuristaController()
    sucursal_ctrl  = SucursalController()
    reserva_ctrl   = ReservaController()

    # ══════════════════════════════════════════════════════
    # DATOS QUEMADOS
    # ══════════════════════════════════════════════════════
    separador("REGISTRANDO SUCURSALES")
    sucursal_bog = sucursal_ctrl.registrar_sucursal(1, "Bogota",    "Cra 7 #32-16")
    sucursal_med = sucursal_ctrl.registrar_sucursal(2, "Medellin",  "Calle 50 #40-20")
    sucursal_cal = sucursal_ctrl.registrar_sucursal(3, "Cali",      "Av 6N #23-10")

    separador("REGISTRANDO HOTELES")
    hotel_1 = hotel_ctrl.registrar_hotel(1, "Hotel Andino",     5)
    hotel_2 = hotel_ctrl.registrar_hotel(2, "Hotel Campestre",  2)
    hotel_3 = hotel_ctrl.registrar_hotel(3, "Hotel del Rio",    0)  # Sin plazas

    separador("REGISTRANDO VUELOS")
    vuelo_1 = vuelo_ctrl.registrar_vuelo(1, "Avianca",    10)
    vuelo_2 = vuelo_ctrl.registrar_vuelo(2, "Latam",      3)
    vuelo_3 = vuelo_ctrl.registrar_vuelo(3, "Wingo",      0)  # Sin cupos

    separador("REGISTRANDO TURISTAS")
    turista_1 = turista_ctrl.registrar_turista(1, "Ana Torres",    "310-000-0001")
    turista_2 = turista_ctrl.registrar_turista(2, "Carlos Ruiz",   "320-000-0002")
    turista_3 = turista_ctrl.registrar_turista(3, "Maria Lopez",   "300-000-0003")

    # ══════════════════════════════════════════════════════
    # PRUEBA 1: RESERVA EXITOSA DE HOTEL
    # ══════════════════════════════════════════════════════
    separador("PRUEBA 1: RESERVA EXITOSA DE HOTEL")
    print("Entrada  : Turista 'Ana Torres', Hotel 'Hotel Andino' (5 plazas), Sucursal Bogota")
    print("Proceso  : Se valida disponibilidad, se descuenta 1 plaza y se asocia a sucursal")
    print("Esperado : Reserva confirmada, Hotel Andino con 4 plazas")
    print("---")
    reserva_1 = reserva_ctrl.crear_reserva_hotel(
        turista_1, hotel_1, sucursal_bog, date.today()
    )
    print(f"Obtenido : Estado reserva = '{reserva_1.get_estado()}' | "
          f"Plazas Hotel Andino = {hotel_1.get_plazas()}")

    # ══════════════════════════════════════════════════════
    # PRUEBA 2: RESERVA SIN DISPONIBILIDAD
    # ══════════════════════════════════════════════════════
    separador("PRUEBA 2: RESERVA SIN DISPONIBILIDAD")
    print("Entrada  : Turista 'Carlos Ruiz', Hotel 'Hotel del Rio' (0 plazas), Sucursal Medellin")
    print("Proceso  : Se valida disponibilidad, el hotel no tiene plazas")
    print("Esperado : Reserva rechazada, mensaje de error")
    print("---")
    reserva_2 = reserva_ctrl.crear_reserva_hotel(
        turista_2, hotel_3, sucursal_med, date.today()
    )
    print(f"Obtenido : Reserva = {reserva_2}")  # Debe ser None

    # ══════════════════════════════════════════════════════
    # PRUEBA 3: CANCELACION DE RESERVA
    # ══════════════════════════════════════════════════════
    separador("PRUEBA 3: CANCELACION DE RESERVA")
    print("Entrada  : Reserva #1 confirmada, Hotel Andino con 4 plazas")
    print("Proceso  : Se cancela la reserva, se libera 1 plaza en el hotel")
    print("Esperado : Estado = 'Cancelada', Hotel Andino con 5 plazas")
    print("---")
    reserva_ctrl.cancelar_reserva(1)
    print(f"Obtenido : Estado reserva = '{reserva_1.get_estado()}' | "
          f"Plazas Hotel Andino = {hotel_1.get_plazas()}")

    # ══════════════════════════════════════════════════════
    # PRUEBA 4: ASOCIACION CORRECTA A SUCURSAL
    # ══════════════════════════════════════════════════════
    separador("PRUEBA 4: ASOCIACION CORRECTA A SUCURSAL")
    print("Entrada  : Turista 'Maria Lopez', Vuelo 'Latam' (3 cupos), Sucursal Cali")
    print("Proceso  : Se crea reserva de vuelo y se asocia a Sucursal Cali")
    print("Esperado : Sucursal Cali tiene 1 reserva registrada")
    print("---")
    reserva_3 = reserva_ctrl.crear_reserva_vuelo(
        turista_3, vuelo_2, sucursal_cal, date.today()
    )
    print(f"Obtenido : Reservas en Sucursal Cali = "
          f"{sucursal_cal.get_total_reservas()}")

    # ══════════════════════════════════════════════════════
    # CONSULTAS FINALES
    # ══════════════════════════════════════════════════════
    separador("CONSULTA: DISPONIBILIDAD FINAL DE HOTELES")
    hotel_ctrl.consultar_disponibilidad(1)  # Hotel Andino
    hotel_ctrl.consultar_disponibilidad(2)  # Hotel Campestre
    hotel_ctrl.consultar_disponibilidad(3)  # Hotel del Rio

    separador("CONSULTA: DISPONIBILIDAD FINAL DE VUELOS")
    vuelo_ctrl.consultar_disponibilidad(1)  # Avianca
    vuelo_ctrl.consultar_disponibilidad(2)  # Latam
    vuelo_ctrl.consultar_disponibilidad(3)  # Wingo

    separador("CONSULTA: RESERVAS POR SUCURSAL")
    sucursal_ctrl.consultar_reservas_sucursal(1)  # Bogota
    sucursal_ctrl.consultar_reservas_sucursal(2)  # Medellin
    sucursal_ctrl.consultar_reservas_sucursal(3)  # Cali

    separador("FIN DE LA SIMULACION")

if __name__ == "__main__":
    main()
