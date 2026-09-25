class RegistroTiempo:
    def __init__(self, fecha, horas, descripcion):
        self.fecha = fecha
        self.set_horas(horas)
        self.descripcion = descripcion

    def set_horas(self, horas):
        if horas <= 0:
            raise ValueError("Las horas registradas deben ser mayores a cero.")
        self._horas = horas

    def get_horas(self):
        return self._horas

    def __str__(self):
        return f"Registro ({self.fecha}): {self._horas}h - {self.descripcion}"