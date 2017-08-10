from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import datetime_not_future
from edc_constants.choices import YES_NO

from ..choices import CAUSE_OF_DEATH, TB_SITE_DEATH
from .model_mixins import CrfModelMixin


class DeathReport(CrfModelMixin):

    death_datetime = models.DateTimeField(
        validators=[datetime_not_future],
        verbose_name='Date and Time of Death')

    study_day = models.CharField(
        max_length=2,
        verbose_name='Study Day')

    death_as_inpatient = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Death as inpatient')

    cause_of_death_study_doctor_opinion = models.CharField(
        max_length=50,
        choices=CAUSE_OF_DEATH,
        verbose_name='Main cause of death (opinion of local study Dr and '
                     'local PI)',
        help_text='Tick only 1:(NB. Fill in AE CRF)')

    cause_other_study_doctor_opinion = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='If other, please specify:')

    cause_tb_study_doctor_opinion = models.CharField(
        max_length=25,
        choices=TB_SITE_DEATH,
        blank=True,
        null=True,
        verbose_name='If cause of death is TB, specify site of TB disease')

    death_narrative = models.TextField(
        verbose_name='Narrative')

    history = HistoricalRecords()
