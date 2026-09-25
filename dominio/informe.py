from abc import ABC, abstractmethod


class Informe(ABC):
    @abstractmethod
    def exportar(self):
        pass


class InformeNomina(Informe):
    def __init__(self, mes, total_a_pagar):
        self.mes = mes
        self.total_a_pagar = total_a_pagar

    def exportar(self):
        return f"[INFORME NÓMINA] Mes: {self.mes} | Total Liquidado: ${self.total_a_pagar:,.0f}"


class InformeProyecto(Informe):
    def __init__(self, nombre_proyecto, horas_acumuladas):
        self.nombre_proyecto = nombre_proyecto
        self.horas_acumuladas = horas_acumuladas

    def exportar(self):
        return f"[INFORME PROYECTO] Proyecto: '{self.nombre_proyecto}' | Horas Totales: {self.horas_acumuladas}h"