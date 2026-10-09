from datetime import date
from dominio.empleado import Empleado
from infraestructura.conexion import obtener_conexion

class EmpleadoRepositorio:

    @staticmethod
    def _fila_a_empleado(fila):
        return Empleado(
            rut=fila[0],
            nombre=fila[1],
            fecha_ingreso=date.fromisoformat(fila[2]) if isinstance(fila[2], str) else fila[2],
            sueldo_base=fila[3]
        )

    def guardar(self, empleado):
        with obtener_conexion() as conn:
            conn.execute(
                "INSERT OR REPLACE INTO persona (rut, nombre) VALUES (?, ?)",
                (empleado.rut, empleado.nombre)
            )
            conn.execute(
                """INSERT OR REPLACE INTO empleado (rut, fecha_ingreso, sueldo_base)
                   VALUES (?, ?, ?)""",
                (
                    empleado.rut,
                    empleado.fecha_ingreso.isoformat() if isinstance(empleado.fecha_ingreso, date) else empleado.fecha_ingreso,
                    empleado.sueldo_base
                )
            )
        return empleado

    def obtener(self, rut):
        with obtener_conexion() as conn:
            fila = conn.execute(
                """SELECT p.rut, p.nombre, e.fecha_ingreso, e.sueldo_base
                   FROM empleado e
                   JOIN persona p ON p.rut = e.rut
                   WHERE e.rut = ?""",
                (rut,)
            ).fetchone()
        return self._fila_a_empleado(fila) if fila else None

    def listar(self, nombre_contiene=None):
        sql = """SELECT p.rut, p.nombre, e.fecha_ingreso, e.sueldo_base
                 FROM empleado e
                 JOIN persona p ON p.rut = e.rut"""
        params = []
        
        if nombre_contiene:
            sql += " WHERE p.nombre LIKE ?"
            params.append(f"%{nombre_contiene}%")

        with obtener_conexion() as conn:
            filas = conn.execute(sql, params).fetchall()
        return [self._fila_a_empleado(f) for f in filas]

    def actualizar(self, empleado):
        with obtener_conexion() as conn:
            conn.execute(
                "UPDATE persona SET nombre = ? WHERE rut = ?",
                (empleado.nombre, empleado.rut)
            )
            cur = conn.execute(
                "UPDATE empleado SET sueldo_base = ? WHERE rut = ?",
                (empleado.sueldo_base, empleado.rut)
            )
        return cur.rowcount

    def eliminar(self, rut):
        with obtener_conexion() as conn:
            cur = conn.execute("DELETE FROM empleado WHERE rut = ?", (rut,))
            conn.execute("DELETE FROM persona WHERE rut = ?", (rut,))
        return cur.rowcount > 0