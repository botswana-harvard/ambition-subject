from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO
from edc_death_report.model_mixins import DeathReportModelMixin

from ..choices import CAUSE_OF_DEATH, TB_SITE_DEATH


class DeathReport(DeathReportModelMixin, BaseUuidModel):

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
        blank=True,
        choices=TB_SITE_DEATH,
        max_length=25,
        null=True,
        verbose_name='If cause of death is TB, specify site of TB disease')

    cause_of_death_tmg1_opinion = models.CharField(
        choices=CAUSE_OF_DEATH,
        help_text='Tick only 1:(NB. Fill in AE CRF)',
        max_length=50,
        verbose_name='Main cause of death (opinion of TMG member 1)')

    cause_other_tmg1_opinion = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='If other, please specify:')

    cause_tb_tmg1_opinion = models.CharField(
        blank=True,
        choices=TB_SITE_DEATH,
        max_length=25,
        null=True,
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
        blank=True,
        choices=TB_SITE_DEATH,
        max_length=25,
        null=True,
        verbose_name='If cause of death is TB, specify site of TB disease')

    narrative_summary = models.TextField(
        verbose_name='Narrative Summary:')

    history = HistoricalRecords()

    class Meta:
        app_label = 'ambition_subject'
