from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import YES_NO

from .model_mixins import CrfModelMixin, EducationModelMixin


class Education(EducationModelMixin, CrfModelMixin):

    household_head = models.CharField(
        verbose_name='Are you head of the household?',
        max_length=5,
        choices=YES_NO)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        verbose_name = 'Health Economics: Education'
        verbose_name_plural = 'Health Economics: Education'
