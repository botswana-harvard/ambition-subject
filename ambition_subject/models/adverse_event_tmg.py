from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import date_not_future

from .list_models import AEClassification
from .model_mixins import CrfModelMixin


class AdverseEventTMG(CrfModelMixin):

    ae_received_datetime = models.DateTimeField(
        blank=True,
        null=True,
        validators=[date_not_future],
        verbose_name='Date and time AE form received:')

    clinical_review_datetime = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Date and time of Clinical Review: ')

    investigator_comments = models.TextField(
        blank=True,
        null=True,
        verbose_name='Investigator Comments:')

    ae_classification = models.ManyToManyField(
        AEClassification,
        blank=True,
        verbose_name='Classification of AE (Tick all that apply):')

    ae_description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Description of AE:')

    officials_notified = models.DateTimeField(
        blank=True,
        null=True,
        validators=[date_not_future],
        verbose_name='Date and time Regulatory authorities notified (SUSARs)')

    investigator_returned = models.DateTimeField(
        blank=True,
        null=True,
        validators=[date_not_future],
        verbose_name=('Date and time form logged in data base and returned'
                      'to Local Investigator'))

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'
        verbose_name_plural = 'Adverse Event TMG'
