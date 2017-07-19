from django.db import models
from edc_base.model_validators import date_not_future

from edc_constants.choices import YES_NO
from ..choices import AE_OUTCOME


from .model_mixins import CrfModelMixin, ClinicalAssessment


class AdverseEventFollowUp(ClinicalAssessment, CrfModelMixin):

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

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'
