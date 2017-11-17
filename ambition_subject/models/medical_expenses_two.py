from edc_base.model_managers import HistoricalRecords

from .model_mixins import CrfModelMixin


class MedicalExpensesTwo(CrfModelMixin):

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        verbose_name = 'Health Economics: Medical Expenses Part 2'
        verbose_name_plural = 'Health Economics: Medical Expenses Part 2'
