from django.db import models

from edc_base.model_validators import date_not_future
from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import YES_NO

from ..choices import FLUCONAZOLE_DOSE

from .model_mixins import CrfModelMixin, ClinicalAssessment
from edc_base.model_fields.custom_fields import OtherCharField


class FollowUp(ClinicalAssessment, CrfModelMixin):

    fluconazole_dose = models.CharField(
        verbose_name='Fluconazole dose (Day prior to visit)',
        max_length=25,
        choices=FLUCONAZOLE_DOSE)

    fluconazole_dose_other = OtherCharField(
        verbose_name='Other fluconazole',
        choices=FLUCONAZOLE_DOSE,
        max_length=25)

    rifampicin_started = models.CharField(
        verbose_name='Rifampicin started since last visit?',
        max_length=5,
        choices=YES_NO)

    rifampicin_start_date = models.DateField(
        verbose_name='Date rifampicin started',
        validators=[date_not_future],
        null=True,
        blank=True,)

    fu_narrative = models.TextField(
        verbose_name='Narrative',
        max_length=300,
        blank=True,
        null=True,)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'
