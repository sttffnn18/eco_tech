import sqlite3
from pathlib import Path
from datetime import date
from dominio.empleado import Empleado
from infraestructura.empleado_repositorio import EmpleadoRepositorio
from infraestructura.conexion import DB_PATH

def inicializar_bd():
    base_dir = Path(__file__).resolve().parent
    esquema_path = base_dir.parent / "db" / "01_esquema.sql"
    if not esquema_path.exists():
        esquema_path = base_dir / "db" / "01_esquema.sql"

    with sqlite3.connect(DB_PATH) as conn:
        with open(esquema_path, "r", encoding="utf-8") as f:
            conn.executescript(f.read())

def main():
    inicializar_bd()
    repo = EmpleadoRepositorio()

    print("--- 1. Guardar empleado ---")
    ana = Empleado("12345678-9", "Ana Rojas", date(2024, 3, 1), 950_000)
    repo.guardar(ana)
    print(f"Empleado guardado: {ana.nombre}")

    print("\n--- 2. Obtener por RUT ---")
    emp = repo.obtener("12345678-9")
    print(f"Obtenido: {emp}")

    print("\n--- 3. Listar todos ---")
    print(f"Total de empleados: {len(repo.listar())}")

    print("\n--- 4. Actualizar sueldo ---")
    ana.sueldo_base = 1_050_000
    repo.actualizar(ana)
    emp_actualizado = repo.obtener("12345678-9")
    print(f"Nuevo sueldo base: {emp_actualizado.sueldo_base}")

    print("\n--- 5. PRUEBA OBLIGATORIA DE INYECCIÓN SQL ---")
    payload = "' OR '1'='1"
    resultado_inyeccion = repo.listar(nombre_contiene=payload)
    print(f"Prueba de inyección con payload: {payload}")
    print(f"Resultados devueltos: {len(resultado_inyeccion)}")
    if len(resultado_inyeccion) == 0:
        print(" La consulta está parametrizada de forma segura.")
    else:
        print(" Se detectó vulnerabilidad a inyección SQL.")

    print("\n--- 6. Eliminar empleado ---")
    eliminado = repo.eliminar("12345678-9")
    print(f"¿Eliminado con éxito?: {eliminado}")

if __name__ == "__main__":
    main()