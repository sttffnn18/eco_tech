# infraestructura/departamento_repositorio.py
from dominio.departamento import Departamento # Asegúrate de que exista esta clase
from infraestructura.conexion import obtener_conexion

class DepartamentoRepositorio:
    
    @staticmethod
    def _fila_a_departamento(fila):
        # Función de mapeo exigida por el laboratorio
        return Departamento(
            id=fila[0],
            nombre=fila[1]
        )

    def guardar(self, departamento):
        with obtener_conexion() as conn:
            conn.execute(
                "INSERT INTO departamento (id, nombre) VALUES (?, ?)",
                (departamento.id, departamento.nombre),
            )
        return departamento

    def obtener(self, id):
        with obtener_conexion() as conn:
            fila = conn.execute(
                "SELECT id, nombre FROM departamento WHERE id = ?",
                (id,),
            ).fetchone()
        return self._fila_a_departamento(fila) if fila else None

    def listar(self, nombre_contiene=None):
        sql = "SELECT id, nombre FROM departamento"
        params = []
        if nombre_contiene:
            sql += " WHERE nombre LIKE ?"
            params.append(f"%{nombre_contiene}%")
            
        with obtener_conexion() as conn:
            filas = conn.execute(sql, params).fetchall()
        return [self._fila_a_departamento(f) for f in filas]

    def actualizar(self, departamento):
        with obtener_conexion() as conn:
            cur = conn.execute(
                "UPDATE departamento SET nombre = ? WHERE id = ?",
                (departamento.nombre, departamento.id),
            )
        return cur.rowcount

    def eliminar(self, id):
        with obtener_conexion() as conn:
            cur = conn.execute("DELETE FROM departamento WHERE id = ?", (id,))
        return cur.rowcount > 0