from django.db import models

from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO, YES_NO_NA

from .model_mixins import CrfModelMixin
from ..choices import RANKING_SCORE


class Week16(CrfModelMixin):

    patient_alive = models.CharField(
        verbose_name='Is the patient alive?',
        max_length=5,
        choices=YES_NO)

    death_datetime = models.DateTimeField(
        verbose_name='If dead, date and time of death:',
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

    ranking_score = models.IntegerField(
        verbose_name='Modified Ranking score:',
        choices=RANKING_SCORE)

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'
