from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future

from .list_models import MissedVisitReason


class MissedVisitManager(models.Manager):

    def get_by_natural_key(self, subject_identifier):
        return self.get(
            subject_identifier=subject_identifier,)


class MissedVisit(BaseUuidModel):

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50)

    missed_study_visit_date = models.DateField(
        validators=[date_not_future])

    visit_missed = models.DecimalField(
        decimal_places=1,
        help_text='Insert visit code',
        max_digits=3)

    missed_visit_reason = models.ManyToManyField(
        MissedVisitReason,
        verbose_name='Reason(s) why participant missed the study visit;')

    missed_visit_reason_other = models.CharField(
        blank=True,
        max_length=50,
        null=True,
        verbose_name='If other reason, please specify:')

    notes_or_action_taken = models.TextField()

    objects = MissedVisitManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.subject_identifier,)
