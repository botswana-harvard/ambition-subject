from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future

from .list_models import AEClassification


class AdverseEventManager(models.Manager):

    def get_by_natural_key(self, subject_identifier):
        return self.get(
            subject_identifier=subject_identifier,)


class AdverseEventTMG(BaseUuidModel):

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50)

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

    objects = AdverseEventManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.subject_identifier,)

    class Meta(BaseUuidModel.Meta):
        app_label = 'ambition_subject'
        verbose_name_plural = 'Adverse Event TMG'
