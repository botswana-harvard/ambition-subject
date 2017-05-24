from django.core.validators import MaxValueValidator
from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import YES_NO

from ..choices import FLUCONAZOLE_DOSE

from .model_mixins import CrfModelMixin, ClinicalAssessment


class FollowUp(ClinicalAssessment, CrfModelMixin):

    fluconazole_dose = models.CharField(
        choices=FLUCONAZOLE_DOSE,
        max_length=25,
        verbose_name='Fluconazole dose (Day prior to visit)')

    other_fluconazole_dose = models.CharField(
        blank=True,
        max_length=75,
        null=True,
        verbose_name='Please other Fluconazole dose')

    other_fluconazole_dose_reason = models.CharField(
        blank=True,
        max_length=150,
        null=True,
        verbose_name='Please other Fluconazole dose and reason')

    is_rifampicin_started = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Rifampicin started since last visit?')

    study_day_rifampicin_started = models.IntegerField(
        blank=True,
        null=True,
        validators=[MaxValueValidator(70)],
        verbose_name='Study day started rifampicin?')

    clinical_care_comments = models.TextField(
        blank=True,
        null=True,
        verbose_name='Comments on Clinical care/Assessment /Plan:')

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'
