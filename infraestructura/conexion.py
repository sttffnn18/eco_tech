import sqlite3
from pathlib import Path
from contextlib import contextmanager

DB_PATH = "ecotech.db"

def inicializar_bd():
    base_dir = Path(__file__).resolve().parent.parent
    esquema_path = base_dir / "db" / "01_esquema.sql"
    
    with sqlite3.connect(DB_PATH) as conn:
        # Crear tabla departamento si no existe en el esquema
        conn.execute("""
            CREATE TABLE IF NOT EXISTS departamento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL
            );
        """)
        if esquema_path.exists():
            with open(esquema_path, "r", encoding="utf-8") as f:
                conn.executescript(f.read())

@contextmanager
def obtener_conexion():
    inicializar_bd()
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = OFF;")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()