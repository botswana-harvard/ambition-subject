from edc_base.model_managers import HistoricalRecords

from .model_mixins import CrfModelMixin, EducationModelMixin


class EducationHoh(EducationModelMixin, CrfModelMixin):

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        verbose_name = 'Health Economics: Education (Head of Household)'
        verbose_name_plural = 'Health Economics: Education (Head of Household)'
