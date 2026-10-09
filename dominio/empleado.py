from dominio.persona import Persona


class Empleado(Persona):
    def __init__(self, rut, nombre, fecha_ingreso, sueldo_base):
        super().__init__(rut, nombre)
        self.rut = rut  # <--- Aseguramos que 'rut' esté accesible directamente
        self.fecha_ingreso = fecha_ingreso
        self.set_sueldo_base(sueldo_base)
        self.registros = []
        self.departamento = None

    @property
    def sueldo_base(self):
        return self._sueldo_base

    @sueldo_base.setter
    def sueldo_base(self, valor):
        self.set_sueldo_base(valor)

    def set_sueldo_base(self, sueldo_base):
        if sueldo_base < 0:
            raise ValueError("El sueldo base no puede ser negativo.")
        self._sueldo_base = sueldo_base

    def get_sueldo_base(self):
        return self._sueldo_base

    def registrar_hora(self, registro):
        self.registros.append(registro)

    def total_horas(self):
        return sum(reg.get_horas() for reg in self.registros) if self.registros else 0

    def __str__(self):
        return f"Empleado: {self.nombre} | RUT: {self.rut} | Sueldo Base: ${self._sueldo_base:,.0f}"