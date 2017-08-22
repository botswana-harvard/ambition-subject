from edc_base.model_managers import HistoricalRecords

from ..model_mixins import CrfModelMixin
from .base_death_report_tmg import BaseDeathReportTmg


class DeathReportTmg2(BaseDeathReportTmg, CrfModelMixin):

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        verbose_name_plural = 'Death report TMG 2'
