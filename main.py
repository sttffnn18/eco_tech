from datetime import date
from dominio.empleado import Empleado
from infraestructura.empleado_repositorio import EmpleadoRepositorio

def pedir_sueldo():
    """Valida que el usuario ingrese un número correcto y mayor a cero."""
    while True:
        entrada = input("Ingrese el sueldo base del empleado: ")
        try:
            sueldo = float(entrada)
            if sueldo <= 0:
                print("Error: El sueldo debe ser mayor a cero.")
            else:
                return sueldo
        except ValueError:
            print("Error: Debe ingresar un numero valido, no texto.")

def main():
    repo = EmpleadoRepositorio()

    print("--- INICIANDO CICLO DE VIDA DEL DATO (CRUD) ---")
    
    # 1. GUARDAR (INSERT)
    # Utilizamos la funcion de validacion para cumplir con la rubrica
    print("Vamos a registrar a un nuevo empleado.")
    sueldo_validado = pedir_sueldo()
    nuevo_empleado = Empleado("12345678-9", "Ana Rojas", date(2024, 3, 1), sueldo_validado)
    
    repo.guardar(nuevo_empleado)
    print("Empleado guardado exitosamente en la base de datos.")

    # 2. LEER (SELECT)
    empleado_bd = repo.obtener("12345678-9")
    if empleado_bd:
        print(f"Leido desde BD: {empleado_bd.rut} - {empleado_bd.nombre} - Sueldo: {empleado_bd.sueldo_base}")
    
    # 3. ACTUALIZAR (UPDATE)
    if empleado_bd:
        empleado_bd.sueldo_base = 1050000
        repo.actualizar(empleado_bd)
        print("Sueldo actualizado correctamente.")

    # 4. PRUEBA DE INYECCION SQL - OBLIGATORIA
    print("\n--- EJECUTANDO PRUEBA DE SEGURIDAD (INYECCION SQL) ---")
    payload_inyeccion = "' OR '1'='1"
    resultados = repo.listar(nombre_contiene=payload_inyeccion)
    
    print(f"Registros encontrados con payload malicioso: {len(resultados)}")
    if len(resultados) == 0:
         print("EXITO: La consulta esta parametrizada. No hay vulnerabilidad.")
    else:
         print("PELIGRO: La prueba fallo, revisa si concatenaste texto en el SQL.")

if __name__ == "__main__":
    main()