from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import YES_NO
from ambition_subject.choices import PROTOCOL_VIOLATION, ACTION_REQUIRED


class ProtocolDeviationViolation (BaseUuidModel):

    safety = models.CharField(
        verbose_name='Safety of the participant',
        max_length=25,
        null=True,
        blank=True,
        choices=YES_NO)

    outcomes = models.CharField(
        verbose_name='Study outcomes',
        max_length=25,
        null=True,
        blank=True,
        choices=YES_NO)

    date_violation_datetime = models.DateTimeField(
        validators=[date_not_future],
        null=True,
        blank=False)

    protocol_violation_type = models.CharField(
        verbose_name='Type of Protocol Violation/Deviation',
        max_length=25,
        null=True,
        blank=True,
        choices=PROTOCOL_VIOLATION)

    description = models.TextField(
        verbose_name='Describe the violation fully. How the violation happened, what occurred?',
        null=True,
        blank=True)

    violation_reason = models.TextField(
        verbose_name='Explain the reason why the violation occurred',
        null=True,
        blank=True)

    corrective_action_datetime = models.DateTimeField(
        validators=[date_not_future],
        null=True,
        blank=False)

    corrective_action = models.CharField(
        verbose_name='Corrective action taken',
        max_length=125,
        null=True,
        blank=True)

    preventative_action_datetime = models.DateTimeField(
        validators=[date_not_future],
        null=True,
        blank=False)

    preventative_action = models.CharField(
        verbose_name='Preventative action taken',
        max_length=125,
        null=True,
        blank=True)

    action_required = models.CharField(
        verbose_name='action required',
        max_length=25,
        null=True,
        blank=True,
        choices=ACTION_REQUIRED)

    history = HistoricalRecords()

    class Meta():
        app_label = 'ambition_subject'
        verbose_name = 'ProtocolDeviationViolation'
