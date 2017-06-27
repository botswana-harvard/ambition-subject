from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE

from ..choices import ARV_REGIMEN, FIRST_LINE_REGIMEN, TB_SITE, ECOG_SCORE
from ..validators import bp_validator
from .list_models import Medication, Neurological, Symptom
from .model_mixins import CrfModelMixin


class PatientHistory(CrfModelMixin):

    symptom = models.ManyToManyField(
        Symptom,
        blank=True,
        related_name='symptoms',
        verbose_name='What are your current symptoms?')

    headache_duration = models.IntegerField(
        verbose_name='If headache, how many days did it last?',
        validators=[MinValueValidator(1)],
        null=True,
        blank=True)

    visual_loss_duration = models.IntegerField(
        verbose_name='If visual loss, how many days did it last?',
        validators=[MinValueValidator(1)],
        null=True,
        blank=True)

    med_history = models.CharField(
        verbose_name='Previous medical history of Tubercolosis?',
        max_length=5,
        choices=YES_NO)

    tb_site = models.CharField(
        verbose_name='If Yes, site of TB?',
        max_length=15,
        choices=TB_SITE,
        default=NOT_APPLICABLE)

    tb_treatment = models.CharField(
        verbose_name='Are you currently taking TB treatment?',
        max_length=5,
        choices=YES_NO)

    taking_rifampicin = models.CharField(
        verbose_name='If yes, are you currently also taking Rifampicin?',
        max_length=5,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE)

    rifampicin_started_date = models.DateField(
        verbose_name='If yes, when did you first start taking Rifampicin?',
        validators=[date_not_future],
        null=True,
        blank=True)

    previous_infection = models.CharField(
        verbose_name='Previous opportunistic infection other than TB?',
        max_length=5,
        choices=YES_NO)

    previous_infection_specify = models.CharField(
        verbose_name='If yes, specify',
        null=True,
        blank=True,
        max_length=50)

    infection_date = models.DateField(
        verbose_name='If yes, what was the date of infection?',
        validators=[date_not_future],
        null=True,
        blank=True)

    new_hiv_diagnosis = models.CharField(
        verbose_name='Is this a new HIV diagnosis?',
        max_length=5,
        choices=YES_NO)

    taking_arv = models.CharField(
        verbose_name='If Yes,Already taking ARVs?',
        max_length=5,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE)

    arv_date = models.DateField(
        verbose_name='If yes, date ARVs were started.',
        validators=[date_not_future],
        null=True,
        blank=True)

    arv_regimen = models.CharField(
        verbose_name='What ARV regimen are you currently prescribed?',
        max_length=50,
        choices=ARV_REGIMEN,
        default=NOT_APPLICABLE)

    arv_regimen_other = OtherCharField()

    first_line_choice = models.CharField(
        verbose_name='If first line:',
        max_length=5,
        choices=FIRST_LINE_REGIMEN,
        null=True,
        default=NOT_APPLICABLE)

    patient_adherence = models.CharField(
        verbose_name='Is the patient reportedly adherent?',
        max_length=5,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE)

    last_dose = models.IntegerField(
        verbose_name='If no, how many months since the last dose was taken?',
        validators=[MinValueValidator(1)],
        null=True,
        blank=True)

    last_viral_load = models.DecimalField(
        verbose_name='Last Viral Load, if known?',
        decimal_places=3,
        max_digits=8,
        null=True,
        blank=True,
        help_text='copies/mL')

    temp = models.DecimalField(
        verbose_name='Temperature:',
        decimal_places=1,
        max_digits=3,
        help_text='°C')

    heart_rate = models.IntegerField(
        verbose_name='Heart Rate:',
        validators=[MinValueValidator(1)],
        help_text='bpm')

    blood_pressure = models.CharField(
        verbose_name='Blood Pressure:',
        max_length=6,
        validators=[bp_validator],
        help_text='in mmHg. format SYS/DIA, e.g. 120/80')

    respiratory_rate = models.IntegerField(
        verbose_name='Respiratory Rate:',
        validators=[MinValueValidator(1)],
        help_text='breaths/min')

    weight = models.DecimalField(
        verbose_name='Weight:',
        decimal_places=1,
        max_digits=4,
        help_text='Kg')

    glasgow_coma_score = models.IntegerField(
        verbose_name='Glasgow Coma Score:',
        validators=[MinValueValidator(1), MaxValueValidator(15)],
        help_text='/15')

    neurological = models.ManyToManyField(
        Neurological,
        blank=True)

    neurological_other = OtherCharField()

    focal_neurologic_deficit = models.TextField(
        verbose_name='If focal neurologic deficit chosen, please specify details:',
        null=True,
        blank=True)

    visual_acuity_day = models.DateField(
        verbose_name='Study day visual acuity recorded?',
        validators=[date_not_future],
        null=True,
        blank=True)

    left_acuity = models.DecimalField(
        verbose_name='Visual acuity Left eye:',
        decimal_places=3,
        max_digits=4,
        null=True,
        blank=True)

    right_acuity = models.DecimalField(
        verbose_name='Visual Acuity Right eye',
        decimal_places=3,
        max_digits=4,
        null=True,
        blank=True)

    ecog_score = models.CharField(
        verbose_name='ECOG Disability score',
        max_length=15,
        choices=ECOG_SCORE)

    lung_exam = models.CharField(
        verbose_name='Abnormal lung exam:',
        max_length=5,
        choices=YES_NO)

    cryptococcal_lesions = models.CharField(
        verbose_name='Cryptococcal related skin lesions:',
        max_length=5,
        choices=YES_NO)

    other_meds = models.CharField(
        verbose_name='Other medication',
        max_length=5,
        choices=YES_NO)

    other_meds_tmp_smx = OtherCharField(
        verbose_name='Is (Yes) Other medications is TMP-SMX:',
        choices=YES_NO)

    specify_medications_other = models.TextField(
        verbose_name='...if "Other", specify',
        max_length=150,
        blank=True,
        null=True)

    specify_medications = models.ManyToManyField(
        Medication,
        blank=True)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'
        verbose_name_plural = 'Patients History'
