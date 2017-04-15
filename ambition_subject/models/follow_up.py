from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO
from edc_metadata.models import CrfMetadata

from ..choices import FLUCONAZOLE_DOSE
from .list_models import SignificantNewDiagnosis
from .model_mixins import CrfModelMixin


class FollowUp(CrfModelMixin):

    physical_symptoms = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Physical symptoms:')

    headache = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Headache:')

    visual_acuity_left_eye = models.DecimalField(
        decimal_places=3,
        max_digits=4,
        verbose_name='Viscuity Left Eye:')

    visual_acuity_right_eye = models.DecimalField(
        decimal_places=3,
        max_digits=4,
        verbose_name='Viscuity Right Eye:')

    glasgow_coma_score = models.IntegerField(
        validators=[MaxValueValidator(15), MinValueValidator(1)],
        verbose_name='Glasgow Coma Score:')

    confusion = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Confusion:')

    recent_seizure_less_72 = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Recent seizure (<72 hrs):')

    cn_palsy = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='CN palsy:')

    behaviour_change = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Behaviour change:')

    focal_neurology = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Focal neurology:')

    significant_new_diagnosis = models.ManyToManyField(
        SignificantNewDiagnosis,
        help_text='Please tick all relevant',
        verbose_name='Other significant new diagnoses since last visit?:')

    other_significant_new_diagnosis = models.CharField(
        blank=True,
        max_length=75,
        null=True,
        verbose_name='Other significant new diagnoses since last visit?:')

    diagnosis_date = models.DateField(
        blank=True,
        null=True,
        validators=[date_not_future],
        verbose_name='If any, date of diagnosis?:')

    fluconazole_dose = models.CharField(
        choices=FLUCONAZOLE_DOSE,
        max_length=25,
        verbose_name='Fluconazole dose (Day prior to visit)')

    other_fluconazole_dose = models.CharField(
        blank=True,
        max_length=75,
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
        verbose_name='Comments on Clinical care/Assessment /Plan:')

    history = HistoricalRecords()

    class Meta(CrfMetadata.Meta):
        app_label = 'ambition_subject'
