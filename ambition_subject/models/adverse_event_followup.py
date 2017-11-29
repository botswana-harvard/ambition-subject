from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_validators import date_not_future
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.utils import get_utcnow
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin

from ..choices import AE_OUTCOME
from .model_mixins import CrfModelMixin
from .adverse_event import AdverseEvent


class AdverseEventFollowUp(NonUniqueSubjectIdentifierFieldMixin, BaseUuidModel):

    adverse_event = models.ForeignKey(AdverseEvent, on_delete=PROTECT)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow)

    outcome = models.CharField(
        blank=False,
        null=False,
        max_length=25,
        choices=AE_OUTCOME)

    outcome_date = models.DateField(
        validators=[date_not_future],
        help_text='Date of Outcome')

    relevant_history = models.TextField(
        verbose_name='Description Summary Of Adverse Event Outcome',
        max_length=1000,
        blank=False,
        null=False,
        help_text='Indicate Adverse Event, Clinical results,'
        'medications given, dosage,treatment plan and outcomes.')

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.subject_identifier = self.adverse_event.subject_identifier
        super().save(*args, **kwargs)

    class Meta(CrfModelMixin.Meta):
        pass
