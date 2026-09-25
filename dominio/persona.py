class Persona:
    """Representa a una persona dentro de EcoTech."""

    def __init__(self, rut, nombre):
        self.set_rut(rut)
        self.nombre = nombre

    def set_rut(self, rut):
        """Invariante: Valida que el RUT sea un texto no vacío."""
        if not isinstance(rut, str) or not rut.strip():
            raise ValueError("El RUT debe ser una cadena de texto válida.")
        self._rut = rut

    def get_rut(self):
        return self._rut

    def __str__(self):
        return f"Persona: {self.nombre} (RUT: {self._rut})"