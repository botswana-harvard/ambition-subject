from django.db import models

from ..choices import RANKING_SCORE
from .model_mixins import CrfModelMixin
from edc_base.model_validators import date_not_future
from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE


class Week16(CrfModelMixin):

    patient_alive = models.CharField(
        verbose_name='Is the patient alive?',
        max_length=5,
        choices=YES_NO)

    death_datetime = models.DateTimeField(
        verbose_name='If dead, date and time of death',
        validators=[date_not_future],
        null=True,
        blank=True)

    activities_help = models.CharField(
        verbose_name=(
            'Does the patient require help from anybody for everyday activities?'),
        max_length=5,
        choices=YES_NO_NA,
        help_text=('For example eating, drinking, washing, brushing teeth,'
                   ' going to the toilet.'))

    illness_problems = models.CharField(
        verbose_name='Has the illness left the patient with any other problems?',
        max_length=5,
        choices=YES_NO_NA)

    ranking_score = models.CharField(
        verbose_name='Modified Ranking score',
        max_length=10,
        choices=RANKING_SCORE,
        default=NOT_APPLICABLE)

    week16_narrative = models.TextField(
        verbose_name='Narrative',
        max_length=1000,
        null=True,
        blank=True)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        verbose_name_plural = 'Week16'
