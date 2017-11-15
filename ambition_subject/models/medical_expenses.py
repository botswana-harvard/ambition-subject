from .model_mixins import CrfModelMixin, MedicalExpensesMixin


class MedicalExpenses(MedicalExpensesMixin, CrfModelMixin):

    class Meta(CrfModelMixin.Meta):
        verbose_name_plural = 'Medical Expenses'
