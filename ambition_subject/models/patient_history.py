from django.core.validators import MinValueValidator, RegexValidator
from django.db import models

from edc_base.model.fields.custom_fields import OtherCharField
from edc_base.model_mixins import BaseUuidModel
from edc_base.model.models import HistoricalRecords
from edc_base.model.validators import date_not_future

from edc_constants.choices import YES_NO

from ..choices import (
    ARV_REGIMEN, FIRST_LINE_REGIMEN, MEDICATION_HISTORY, TB_SITE)
from ..models.list_models import Neurological, Symptoms

bp_validator = RegexValidator(
    '^\d{1,3}\/\d{1,3}$', message='Enter a valid BP in SYS/DIA format')


class PatientHistory (BaseUuidModel):

    current_symptoms = models.ManyToManyField(
        Symptoms,
        related_name="symptoms",
        blank=True,
        verbose_name=(
            'What are your current symptoms'))

    headache_duration = models.IntegerField(
        verbose_name='If headache, how many days did it last?',
        validators=[MinValueValidator(1)],
        null=True,
        blank=False,
        help_text='')

    visual_loss_duration = models.IntegerField(
        verbose_name='If visual loss, how many days did it last?',
        validators=[MinValueValidator(1)],
        null=True,
        blank=False,
        help_text='')

    med_history = models.CharField(
        verbose_name="Previous medical history of Tubercolosis?",
        max_length=15,
        null=True,
        blank=True,
        choices=YES_NO,
        help_text="")

    tb_site = models.CharField(
        verbose_name='If Yes, site of TB?',
        default=None,
        null=True,
        blank=True,
        choices=TB_SITE,
        help_text=""
    )

    tb_treatment = models.CharField(
        verbose_name="Are you currently taking TB treatment?",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=False,
        help_text="")

    taking_rifampicin = models.CharField(
        verbose_name="If yes, are you currently also taking Rifampicin?",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=False,
        help_text="")

    rifampicin_started_date = models.DateField(
        verbose_name=(
            'If yes, when did you first start taking Rifampicin?'),
        validators=[date_not_future],
        null=True,
        blank=True,
    )

    previous_infection = models.CharField(
        verbose_name="Previous opportunistic infection?",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=False,
        help_text="")

    infection_date = models.DateField(
        verbose_name=(
            'If yes, what was the date of infection?'),
        validators=[date_not_future],
        null=True,
        blank=True,
    )

    taking_arv = models.CharField(
        verbose_name="Already taking ARVs?",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=False,
        help_text="")

    arv_date = models.DateField(
        verbose_name=(
            'If yes, date ARVs were started.'),
        validators=[date_not_future],
        null=True,
        blank=True,
    )

    arvs = models.CharField(
        verbose_name=(
            'What ARV regimen are you currently prescribed?'),
        null=True,
        blank=True,
        choices=ARV_REGIMEN,
    )

    first_line_choice = models.CharField(
        verbose_name="If first line, are you on EFV or NVP?",
        max_length=25,
        choices=FIRST_LINE_REGIMEN,
        null=True,
        blank=False,
        help_text="")

    patient_adherence = models.CharField(
        verbose_name="Is the patient reportedly adherent?",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=False,
        help_text="")

    last_dose = models.IntegerField(
        verbose_name='If no, how many months since the last dose was taken?',
        validators=[MinValueValidator(1)],
        null=True,
        blank=False,
        help_text='')

    last_viral_load = models.DecimalField(
        verbose_name='Last Viral Load, if known?',
        null=True,
        blank=False,
        help_text='copies/mL')

    temp = models.DecimalField(
        verbose_name='Temperature: ',
        null=True,
        blank=False,
        help_text='°C')

    heart_rate = models.IntegerField(
        verbose_name='Heart Rate: ',
        null=True,
        blank=False,
        help_text='bpm')

    blood_pressure = models.CharField(
        verbose_name='Blood Pressure: ',
        max_length=15,
        validators=[bp_validator],
        null=True,
        blank=True,
        help_text='in mmHg. format SYS/DIA, e.g. 120/80')

    respiratory_rate = models.IntegerField(
        verbose_name='Respiratory Rate: ',
        null=True,
        blank=False,
        help_text='breaths/min')

    glasgow_coma_score = models.IntegerField(
        verbose_name='Glasgow Coma Score: ',
        null=True,
        blank=False,
        help_text='/15')

    neurological = models.ManyToManyField(
        Neurological,
        blank=True,
        null=True,
        verbose_name=('Neurological'))

    neurological_other = OtherCharField()

    focal_neurologic_deficit = models.CharField(
        verbose_name="If focal neurologic deficit chosen, please specify:",
        max_length=25,
        null=True,
        blank=False,
        help_text="")

    visual_acuity_day = models.DateField(
        verbose_name="Study day visual acuity recorded?",
        validators=[date_not_future],
        null=True,
        blank=False,
        help_text="")

    left_acuity = models.DecimalField(
        verbose_name='Visual acuity Left eye: ',
        null=True,
        blank=False,
        help_text='')

    right_acuity = models.DecimalField(
        verbose_name='Visual acuity Right eye: ',
        null=True,
        blank=False,
        help_text='')

    lung_exam = models.CharField(
        verbose_name="Abnormal lung exam:",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=False,
        help_text="")

    cryptococcal_lesions = models.CharField(
        verbose_name="Cryptococcal related skin lesions:",
        max_length=25,
        choices=YES_NO,
        null=True,
        blank=False,
        help_text="")

    other_medications = models.CharField(
        verbose_name="Other medications:",
        max_length=25,
        choices=MEDICATION_HISTORY,
        null=True,
        blank=False,
        help_text="")

    other_medications_other = OtherCharField()

    history = HistoricalRecords()

    class Meta():
        app_label = 'ambition_subject'
        verbose_name = 'PatientHistory'
        verbose_name_plural = 'PatientHistory'
