from dominio.departamento import Departamento
from dominio.empleado import Empleado
from dominio.informe import InformeNomina, InformeProyecto


def main():
    dep = Departamento("Operaciones")
    ana = Empleado("12345678-9", "Ana Rojas", "2024-03-01", 950_000)
    dep.agregar_empleado(ana)

    print(dep)
    print(ana)
    print(f"Horas registradas: {ana.total_horas()}\n")


    informes = [
        InformeNomina("Marzo", 12500000),
        InformeNomina("Abril", 13100000),
        InformeProyecto("EcoTech Fase 2", 145.5),
    ]

    for informe in informes:
        print(informe.exportar())


if __name__ == "__main__":
    main()