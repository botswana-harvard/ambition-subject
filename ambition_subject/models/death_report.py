from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO

from ..choices import CAUSE_OF_DEATH, TB_SITE_DEATH


class Death(BaseUuidModel):

    death_date = models.DateField(
        validators=[date_not_future])

    study_day = models.CharField(
        max_length=2,
        verbose_name='Study Day')

    death_as_inpatient = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Death as inpatient')

    cause_of_death_study_doctor_opinion = models.CharField(
        choices=CAUSE_OF_DEATH,
        help_text='Tick only 1:(NB. Fill in AE CRF)',
        max_length=50,
        verbose_name='Main cause of death (opinion of local study Dr and '
                     'local PI)')

    cause_other_study_doctor_opinion = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='If other, please specify:')

    cause_tb_study_doctor_opinion = models.CharField(
        choices=TB_SITE_DEATH,
        max_length=25,
        verbose_name='If cause of death is TB, specify site of TB disease')

    cause_of_death_tmg1_opinion = models.CharField(
        choices=CAUSE_OF_DEATH,
        help_text='Tick only 1:(NB. Fill in AE CRF)',
        max_length=50,
        verbose_name='Main cause of death (opinion of TMG member 1)')

    cause_of_death_agreed = models.CharField(
        choices=YES_NO,
        help_text='If No, complete Q10 below',
        max_length=5,
        verbose_name='Cause of death agreed between Study dr and TMG member?')

    cause_other_tmg1_opinion = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='If other, please specify:')

    cause_tb_tmg1_opinion = models.CharField(
        choices=TB_SITE_DEATH,
        max_length=25,
        verbose_name='If cause of death is TB, specify site of TB disease')

    cause_of_death_tmg2_opinion = models.CharField(
        choices=CAUSE_OF_DEATH,
        help_text='Tick only 1:(NB. Fill in AE CRF)',
        max_length=50,
        verbose_name='Main cause of death (opinion of TMG member 2)')

    cause_other_tmg2_opinion = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='If other, please specify:')

    cause_tb_tmg2_opinion = models.CharField(
        choices=TB_SITE_DEATH,
        max_length=25,
        verbose_name='If cause of death is TB, specify site of TB disease')

    narrative_summary = models.TextField(
        verbose_name='Narrative Summary:')

    history = HistoricalRecords()

    class Meta:
        app_label = 'ambition_subject'
