from models.sucursal import Sucursal

class SucursalController:
    def __init__(self):
        # Lista en memoria de todas las sucursales
        self.__sucursales = []

    # ── REGISTRAR ──────────────────────────────────────────
    def registrar_sucursal(self, id_sucursal: int, nombre: str,
                            direccion: str) -> Sucursal:
        # Validar que no exista una sucursal con el mismo id
        if self.__buscar_por_id(id_sucursal):
            print(f"Error: ya existe una sucursal con el id {id_sucursal}.")
            return None

        # Validar que nombre y dirección no estén vacíos
        if not nombre.strip():
            print("Error: el nombre de la sucursal no puede estar vacío.")
            return None

        if not direccion.strip():
            print("Error: la dirección no puede estar vacía.")
            return None

        sucursal = Sucursal(id_sucursal, nombre, direccion)
        self.__sucursales.append(sucursal)
        print(f"Sucursal '{nombre}' registrada exitosamente.")
        return sucursal

    # ── CONSULTAR ──────────────────────────────────────────
    def consultar_sucursales(self) -> list:
        if not self.__sucursales:
            print("No hay sucursales registradas.")
            return []
        return self.__sucursales

    def consultar_sucursal(self, id_sucursal: int) -> Sucursal:
        sucursal = self.__buscar_por_id(id_sucursal)
        if not sucursal:
            print(f"Error: no se encontró la sucursal con id {id_sucursal}.")
            return None
        return sucursal

    # ── ACTUALIZAR ─────────────────────────────────────────
    def actualizar_nombre(self, id_sucursal: int,
                           nuevo_nombre: str) -> bool:
        sucursal = self.__buscar_por_id(id_sucursal)
        if not sucursal:
            print(f"Error: no se encontró la sucursal con id {id_sucursal}.")
            return False

        if not nuevo_nombre.strip():
            print("Error: el nuevo nombre no puede estar vacío.")
            return False

        print(f"Sucursal #{id_sucursal} actualizada a '{nuevo_nombre}'.")
        return True

    # ── CONSULTAR RESERVAS DE UNA SUCURSAL ─────────────────
    def consultar_reservas_sucursal(self, id_sucursal: int) -> list:
        sucursal = self.__buscar_por_id(id_sucursal)
        if not sucursal:
            print(f"Error: no se encontró la sucursal con id {id_sucursal}.")
            return []

        reservas = sucursal.get_reservas()
        if not reservas:
            print(f"La sucursal '{sucursal.get_nombre()}' "
                  f"no tiene reservas registradas.")
            return []

        print(f"Sucursal '{sucursal.get_nombre()}': "
              f"{sucursal.get_total_reservas()} reserva(s).")
        return reservas

    # ── PRIVADO: búsqueda interna ──────────────────────────
    def __buscar_por_id(self, id_sucursal: int) -> Sucursal:
        for sucursal in self.__sucursales:
            if sucursal.get_id() == id_sucursal:
                return sucursal
        return None