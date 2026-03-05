from models.turista import Turista

class TuristaController:
    def __init__(self):
        # Lista en memoria de todos los turistas registrados
        self.__turistas = []

    # ── REGISTRAR ──────────────────────────────────────────
    def registrar_turista(self, id_turista: int, nombre: str,
                           telefono: str) -> Turista:
        # Validar que no exista un turista con el mismo id
        if self.__buscar_por_id(id_turista):
            print(f"Error: ya existe un turista con el id {id_turista}.")
            return None

        # Validar que nombre y teléfono no estén vacíos
        if not nombre.strip():
            print("Error: el nombre del turista no puede estar vacío.")
            return None

        if not telefono.strip():
            print("Error: el teléfono no puede estar vacío.")
            return None

        turista = Turista(id_turista, nombre, telefono)
        self.__turistas.append(turista)
        print(f"Turista '{nombre}' registrado exitosamente.")
        return turista

    # ── CONSULTAR ──────────────────────────────────────────
    def consultar_turistas(self) -> list:
        if not self.__turistas:
            print("No hay turistas registrados.")
            return []
        return self.__turistas

    def consultar_turista(self, id_turista: int) -> Turista:
        turista = self.__buscar_por_id(id_turista)
        if not turista:
            print(f"Error: no se encontró el turista con id {id_turista}.")
            return None
        return turista

    # ── ACTUALIZAR ─────────────────────────────────────────
    def actualizar_telefono(self, id_turista: int,
                             nuevo_telefono: str) -> bool:
        turista = self.__buscar_por_id(id_turista)
        if not turista:
            print(f"Error: no se encontró el turista con id {id_turista}.")
            return False

        if not nuevo_telefono.strip():
            print("Error: el nuevo teléfono no puede estar vacío.")
            return False

        print(f"Teléfono del turista '{turista.get_nombre()}' "
              f"actualizado a '{nuevo_telefono}'.")
        return True

    # ── BUSCAR POR NOMBRE ──────────────────────────────────
    def buscar_por_nombre(self, nombre: str) -> list:
        resultado = [t for t in self.__turistas
                     if nombre.lower() in t.get_nombre().lower()]
        if not resultado:
            print(f"No se encontraron turistas con el nombre '{nombre}'.")
        return resultado

    # ── PRIVADO: búsqueda interna ──────────────────────────
    def __buscar_por_id(self, id_turista: int) -> Turista:
        for turista in self.__turistas:
            if turista.get_id() == id_turista:
                return turista
        return None