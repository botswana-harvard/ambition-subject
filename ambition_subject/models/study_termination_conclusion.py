from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO

from ..choices import ARV_REGIMEN, FIRST_LINE_REGIMEN, REASON_STUDY_TERMINATED


class StudyTerminationConclusion(BaseUuidModel):

    date_patient_terminated_study = models.DateField(
        validators=[date_not_future])

    termination_study_day = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)])

    last_research_termination_date = models.DateField(
        verbose_name='Date of last research follow-up (if different)',
        blank=True,
        null=True,
        validators=[date_not_future])

    last_research_termination_study_day = models.IntegerField(
        verbose_name='Last research follow-up study day if different',
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(99)])

    discharged_after_initial_admission = models.CharField(
        verbose_name='If yes, date of initial discharge',
        max_length=5,
        choices=YES_NO)

    initial_discharge_date = models.DateField(
        blank=True,
        null=True,
        validators=[date_not_future])

    initial_discharge_study_date = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(99)])

    readmission_following_initial_discharge = models.CharField(
        choices=YES_NO,
        max_length=5)

    date_admitted = models.DateField(
        blank=True,
        null=True,
        validators=[date_not_future])

    date_discharged = models.DateField(
        blank=True,
        null=True,
        validators=[date_not_future])

    study_termination_reason = models.CharField(
        choices=REASON_STUDY_TERMINATED,
        max_length=75)
    
    study_termination_reason_death =  models.DateField(
        verbose_name='if reported to have died',
        blank=True,
        null=True,
        validators=[date_not_future])

    withdrawal_of_consent_reason = models.CharField(
        max_length=75,
        blank=True,
        null=True)

    rifampicin_started_since_week4 = models.CharField(
        max_length=5,
        choices=YES_NO)

    rifampicin_started_study_day = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(99)])

    arv_regimen = models.CharField(
        max_length=50,
        choices=ARV_REGIMEN)
    
    arv_regimen_other = models.CharField(
        verbose_name='If in other regimes, please specify',
        max_length=50,
        blank=True,
        null=True)

    is_naive = models.CharField(
        max_length=5,
        choices=YES_NO)

    date_started_arvs = models.DateField(
        blank=True,
        null=True,
        validators=[date_not_future])

    date_switched_arvs = models.DateField(
        blank=True,
        null=True,
        validators=[date_not_future])

    is_first_line_regimen = models.CharField(
        max_length=5,
        choices=YES_NO)

    efv_or_nvp = models.CharField(
        verbose_name='If first line, on EFV or NVP and or DTG?',
        max_length=3,
        choices=FIRST_LINE_REGIMEN,
        null=True)

    history = HistoricalRecords()

    class Meta:
        app_label = 'ambition_subject'
