from datetime import date

from controllers.hotel import HotelController
from controllers.vuelo import VueloController
from controllers.turista import TuristaController
from controllers.sucursal import SucursalController
from controllers.reserva import ReservaController
from exceptions.agencia_exceptions import (
    RegistroDuplicadoError, DatoVacioError, ValorInvalidoError,
    NoEncontradoError, SinDisponibilidadError, EstadoInvalidoError
)

def separador(titulo: str):
    print("\n" + "=" * 50)
    print(f"  {titulo}")
    print("=" * 50)

def main():

    # ── INSTANCIAR CONTROLADORES ───────────────────────────
    hotel_ctrl    = HotelController()
    vuelo_ctrl    = VueloController()
    turista_ctrl  = TuristaController()
    sucursal_ctrl = SucursalController()
    reserva_ctrl  = ReservaController()

    # ══════════════════════════════════════════════════════
    # DATOS QUEMADOS
    # ══════════════════════════════════════════════════════
    separador("REGISTRANDO SUCURSALES")
    try:
        sucursal_bog = sucursal_ctrl.registrar_sucursal(1, "Bogota",   "Cra 7 #32-16")
        sucursal_med = sucursal_ctrl.registrar_sucursal(2, "Medellin", "Calle 50 #40-20")
        sucursal_cal = sucursal_ctrl.registrar_sucursal(3, "Cali",     "Av 6N #23-10")
    except (RegistroDuplicadoError, DatoVacioError) as e:
        print(e)

    separador("REGISTRANDO HOTELES")
    try:
        hotel_1 = hotel_ctrl.registrar_hotel(1, "Hotel Andino",    5)
        hotel_2 = hotel_ctrl.registrar_hotel(2, "Hotel Campestre", 2)
        hotel_3 = hotel_ctrl.registrar_hotel(3, "Hotel del Rio",   0)  # Sin plazas
    except (RegistroDuplicadoError, DatoVacioError, ValorInvalidoError) as e:
        print(e)

    separador("REGISTRANDO VUELOS")
    try:
        vuelo_1 = vuelo_ctrl.registrar_vuelo(1, "Avianca", 10)
        vuelo_2 = vuelo_ctrl.registrar_vuelo(2, "Latam",   3)
        vuelo_3 = vuelo_ctrl.registrar_vuelo(3, "Wingo",   0)  # Sin cupos
    except (RegistroDuplicadoError, DatoVacioError, ValorInvalidoError) as e:
        print(e)

    separador("REGISTRANDO TURISTAS")
    try:
        turista_1 = turista_ctrl.registrar_turista(1, "Ana Torres",  "310-000-0001")
        turista_2 = turista_ctrl.registrar_turista(2, "Carlos Ruiz", "320-000-0002")
        turista_3 = turista_ctrl.registrar_turista(3, "Maria Lopez", "300-000-0003")
    except (RegistroDuplicadoError, DatoVacioError) as e:
        print(e)

    # ══════════════════════════════════════════════════════
    # PRUEBA 1: RESERVA EXITOSA DE HOTEL
    # ══════════════════════════════════════════════════════
    separador("PRUEBA 1: RESERVA EXITOSA DE HOTEL")
    print("Entrada  : Turista 'Ana Torres', Hotel 'Hotel Andino' (5 plazas), Sucursal Bogota")
    print("Proceso  : Se valida disponibilidad, se descuenta 1 plaza y se asocia a sucursal")
    print("Esperado : Reserva confirmada, Hotel Andino con 4 plazas")
    print("---")
    try:
        reserva_1 = reserva_ctrl.crear_reserva_hotel(
            turista_1, hotel_1, sucursal_bog, date.today()
        )
        print(f"Obtenido : Estado = '{reserva_1.get_estado()}' | "
              f"Plazas Hotel Andino = {hotel_1.get_plazas()}")
    except SinDisponibilidadError as e:
        print(e)

    # ══════════════════════════════════════════════════════
    # PRUEBA 2: RESERVA SIN DISPONIBILIDAD
    # ══════════════════════════════════════════════════════
    separador("PRUEBA 2: RESERVA SIN DISPONIBILIDAD")
    print("Entrada  : Turista 'Carlos Ruiz', Hotel 'Hotel del Rio' (0 plazas), Sucursal Medellin")
    print("Proceso  : Se valida disponibilidad, el hotel no tiene plazas")
    print("Esperado : Excepcion SinDisponibilidadError lanzada")
    print("---")
    try:
        reserva_2 = reserva_ctrl.crear_reserva_hotel(
            turista_2, hotel_3, sucursal_med, date.today()
        )
    except SinDisponibilidadError as e:
        print(f"Obtenido : {e}")

    # ══════════════════════════════════════════════════════
    # PRUEBA 3: CANCELACION DE RESERVA
    # ══════════════════════════════════════════════════════
    separador("PRUEBA 3: CANCELACION DE RESERVA")
    print("Entrada  : Reserva #1 confirmada, Hotel Andino con 4 plazas")
    print("Proceso  : Se cancela la reserva, se libera 1 plaza en el hotel")
    print("Esperado : Estado = 'Cancelada', Hotel Andino con 5 plazas")
    print("---")
    try:
        reserva_ctrl.cancelar_reserva(1)
        print(f"Obtenido : Estado = '{reserva_1.get_estado()}' | "
              f"Plazas Hotel Andino = {hotel_1.get_plazas()}")
    except (NoEncontradoError, EstadoInvalidoError) as e:
        print(e)

    # ══════════════════════════════════════════════════════
    # PRUEBA 4: ASOCIACION CORRECTA A SUCURSAL
    # ══════════════════════════════════════════════════════
    separador("PRUEBA 4: ASOCIACION CORRECTA A SUCURSAL")
    print("Entrada  : Turista 'Maria Lopez', Vuelo 'Latam' (3 cupos), Sucursal Cali")
    print("Proceso  : Se crea reserva de vuelo y se asocia a Sucursal Cali")
    print("Esperado : Sucursal Cali tiene 1 reserva registrada")
    print("---")
    try:
        reserva_3 = reserva_ctrl.crear_reserva_vuelo(
            turista_3, vuelo_2, sucursal_cal, date.today()
        )
        print(f"Obtenido : Reservas en Sucursal Cali = "
              f"{sucursal_cal.get_total_reservas()}")
    except SinDisponibilidadError as e:
        print(e)

    # ══════════════════════════════════════════════════════
    # PRUEBA EXTRA: CANCELAR RESERVA YA CANCELADA
    # ══════════════════════════════════════════════════════
    separador("PRUEBA EXTRA: CANCELAR RESERVA YA CANCELADA")
    print("Entrada  : Reserva #1 ya cancelada")
    print("Esperado : Excepcion EstadoInvalidoError lanzada")
    print("---")
    try:
        reserva_ctrl.cancelar_reserva(1)
    except EstadoInvalidoError as e:
        print(f"Obtenido : {e}")

    # ══════════════════════════════════════════════════════
    # PRUEBA EXTRA: BUSCAR RESERVA INEXISTENTE
    # ══════════════════════════════════════════════════════
    separador("PRUEBA EXTRA: BUSCAR RESERVA INEXISTENTE")
    print("Entrada  : Reserva con id 99 no existe")
    print("Esperado : Excepcion NoEncontradoError lanzada")
    print("---")
    try:
        reserva_ctrl.cancelar_reserva(99)
    except NoEncontradoError as e:
        print(f"Obtenido : {e}")

    # ══════════════════════════════════════════════════════
    # CONSULTAS FINALES
    # ══════════════════════════════════════════════════════
    separador("CONSULTA: DISPONIBILIDAD FINAL DE HOTELES")
    for id_hotel in [1, 2, 3]:
        try:
            hotel_ctrl.consultar_disponibilidad(id_hotel)
        except NoEncontradoError as e:
            print(e)

    separador("CONSULTA: DISPONIBILIDAD FINAL DE VUELOS")
    for id_vuelo in [1, 2, 3]:
        try:
            vuelo_ctrl.consultar_disponibilidad(id_vuelo)
        except NoEncontradoError as e:
            print(e)

    separador("CONSULTA: RESERVAS POR SUCURSAL")
    for id_sucursal in [1, 2, 3]:
        try:
            sucursal_ctrl.consultar_reservas_sucursal(id_sucursal)
        except NoEncontradoError as e:
            print(e)

    separador("FIN DE LA SIMULACION")

if __name__ == "__main__":
    main()