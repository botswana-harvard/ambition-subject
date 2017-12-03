from edc_base.model_managers import HistoricalRecords

from .base_death_report_tmg import BaseDeathReportTmg


class DeathReportTmg1(BaseDeathReportTmg):

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'Death report TMG 1'
