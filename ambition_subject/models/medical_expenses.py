from edc_base.model_managers import HistoricalRecords

from .model_mixins import CrfModelMixin, MedicalExpensesModelMixin


class MedicalExpenses(MedicalExpensesModelMixin, CrfModelMixin):

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        verbose_name_plural = 'Medical Expenses'
