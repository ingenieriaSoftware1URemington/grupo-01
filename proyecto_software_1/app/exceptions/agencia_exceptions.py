# Clase base de la que heredan todas las excepciones del proyecto
class AgenciaError(Exception):
    def __init__(self, mensaje: str):
        super().__init__(mensaje)
        self.mensaje = mensaje

    def __str__(self):
        return f"[Error Agencia] {self.mensaje}"


# ── ERRORES DE REGISTRO ────────────────────────────────
class RegistroDuplicadoError(AgenciaError):
    """Se lanza cuando se intenta registrar un objeto con un id ya existente."""
    def __str__(self):
        return f"[Registro Duplicado] {self.mensaje}"


class DatoVacioError(AgenciaError):
    """Se lanza cuando un campo obligatorio llega vacio."""
    def __str__(self):
        return f"[Dato Vacio] {self.mensaje}"


class ValorInvalidoError(AgenciaError):
    """Se lanza cuando un valor numerico no cumple las reglas (ej: plazas negativas)."""
    def __str__(self):
        return f"[Valor Invalido] {self.mensaje}"


# ── ERRORES DE BUSQUEDA ────────────────────────────────
class NoEncontradoError(AgenciaError):
    """Se lanza cuando no se encuentra un objeto por su id."""
    def __str__(self):
        return f"[No Encontrado] {self.mensaje}"


# ── ERRORES DE RESERVA ─────────────────────────────────
class SinDisponibilidadError(AgenciaError):
    """Se lanza cuando no hay plazas o cupos disponibles."""
    def __str__(self):
        return f"[Sin Disponibilidad] {self.mensaje}"


class EstadoInvalidoError(AgenciaError):
    """Se lanza cuando se intenta cancelar una reserva que no esta confirmada."""
    def __str__(self):
        return f"[Estado Invalido] {self.mensaje}"