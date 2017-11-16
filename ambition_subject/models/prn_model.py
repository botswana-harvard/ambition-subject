from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import YES_NO
from edc_constants.constants import NO, YES

from .model_mixins import CrfModelMixin


class PrnModel(CrfModelMixin):

    adverse_event = models.CharField(
        verbose_name='Adverse event?',
        max_length=5,
        choices=YES_NO,
        default=NO)

    adverse_event_tmg = models.CharField(
        verbose_name='Adverse event TMG?',
        max_length=5,
        choices=YES_NO,
        default=NO)

    adverse_event_followup = models.CharField(
        verbose_name='Adverse event follow up?',
        max_length=5,
        choices=YES_NO,
        default=NO)

    blood_result = models.CharField(
        verbose_name='Blood result?',
        max_length=5,
        choices=YES_NO,
        default=YES)

    microbiology = models.CharField(
        verbose_name='Microbiology?',
        max_length=5,
        choices=YES_NO,
        default=NO)

    radiology = models.CharField(
        verbose_name='Radiology?',
        max_length=5,
        choices=YES_NO,
        default=NO)

    recurrence_symptom = models.CharField(
        verbose_name='Recurrence of Symptoms?',
        max_length=5,
        choices=YES_NO,
        default=NO,
        null=True)

    protocol_deviation = models.CharField(
        verbose_name='Protocol Deviation?',
        max_length=5,
        choices=YES_NO,
        default=NO)

    lumbar_puncture = models.CharField(
        verbose_name='Lumbar puncture?',
        max_length=5,
        choices=YES_NO,
        default=YES,
        null=True)

    death_report = models.CharField(
        verbose_name='Death Report?',
        max_length=5,
        choices=YES_NO,
        default=NO)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        verbose_name = 'PRN Form'
        verbose_name_plural = 'PRN Forms'
