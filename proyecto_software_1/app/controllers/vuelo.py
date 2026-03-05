from models.vuelo import Vuelo

class VueloController:
    def __init__(self):
        # Lista en memoria de todos los vuelos registrados
        self.__vuelos = []

    # ── REGISTRAR ──────────────────────────────────────────
    def registrar_vuelo(self, id_vuelo: int, aerolinea: str,
                         cupos: int) -> Vuelo:
        # Validar que no exista un vuelo con el mismo id
        if self.__buscar_por_id(id_vuelo):
            print(f"Error: ya existe un vuelo con el id {id_vuelo}.")
            return None

        # Validar que la aerolínea no esté vacía
        if not aerolinea.strip():
            print("Error: la aerolínea no puede estar vacía.")
            return None

        # Validar que los cupos sean positivos
        if cupos <= 0:
            print("Error: los cupos deben ser mayor a 0.")
            return None

        vuelo = Vuelo(id_vuelo, aerolinea, cupos)
        self.__vuelos.append(vuelo)
        print(f"Vuelo '{aerolinea}' registrado exitosamente.")
        return vuelo

    # ── CONSULTAR ──────────────────────────────────────────
    def consultar_vuelos(self) -> list:
        if not self.__vuelos:
            print("No hay vuelos registrados.")
            return []
        return self.__vuelos

    def consultar_vuelo(self, id_vuelo: int) -> Vuelo:
        vuelo = self.__buscar_por_id(id_vuelo)
        if not vuelo:
            print(f"Error: no se encontró el vuelo con id {id_vuelo}.")
            return None
        return vuelo

    # ── CONSULTAR DISPONIBILIDAD ───────────────────────────
    def consultar_disponibilidad(self, id_vuelo: int) -> int:
        vuelo = self.__buscar_por_id(id_vuelo)
        if not vuelo:
            print(f"Error: no se encontró el vuelo con id {id_vuelo}.")
            return None

        cupos = vuelo.get_cupos()
        print(f"Vuelo '{vuelo.get_aerolinea()}': "
              f"{cupos} cupos disponibles.")
        return cupos

    # ── ACTUALIZAR ─────────────────────────────────────────
    def actualizar_aerolinea(self, id_vuelo: int,
                              nueva_aerolinea: str) -> bool:
        vuelo = self.__buscar_por_id(id_vuelo)
        if not vuelo:
            print(f"Error: no se encontró el vuelo con id {id_vuelo}.")
            return False

        if not nueva_aerolinea.strip():
            print("Error: el nombre de la aerolínea no puede estar vacío.")
            return False

        print(f"Vuelo #{id_vuelo} actualizado a '{nueva_aerolinea}'.")
        return True

    # ── PRIVADO: búsqueda interna ──────────────────────────
    def __buscar_por_id(self, id_vuelo: int) -> Vuelo:
        for vuelo in self.__vuelos:
            if vuelo.get_id() == id_vuelo:
                return vuelo
        return None