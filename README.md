# Proyecto Eco Tech

## Decisiones de Diseño (Laboratorio C08)

1. **¿Se borra de verdad?**
   * Decisión: Se implementó un DELETE real (borrado físico) en la base de datos para la entidad Empleado y Departamento.

2. **¿Qué pasa con los hijos?**
   * Decisión: Se utiliza borrado en cascada. Si se elimina una persona/empleado, se eliminan los registros asociados para evitar datos huérfanos.

3. **¿Quién asigna el id?**
   * Decisión: El ID o RUT es asignado por el programa (lo ingresa el usuario o el sistema antes de enviarlo a la base de datos).
