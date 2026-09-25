class Departamento:
    """Representa un Departamento de la empresa"""

    def __init__(self,nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleados(self,empleados):
        """Agrega un empleado ala lista del departamento"""
        self.empleados.append(empleados)