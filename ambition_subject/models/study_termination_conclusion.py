from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO

from ..choices import ARV_REGIMEN, REASON_STUDY_TERMINATED, FIRST_LINE_REGIMEN


class StudyTerminationConclusion(BaseUuidModel):

    date_patient_terminated_study = models.DateField(
        validators=[date_not_future])

    termination_study_day = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)])

    last_research_termination_date = models.DateField(
        blank=True,
        null=True,
        validators=[date_not_future],
        verbose_name='Date of last research follow-up (if different):')

    last_research_termination_study_day = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(99)],
        verbose_name='Last research follow-up study day if different')

    discharged_after_initial_admission = models.CharField(
        choices=YES_NO,
        max_length=5)

    initial_discharge_date = models.DateField(
        blank=True,
        null=True,
        validators=[date_not_future],
        verbose_name='If yes, date of initial discharge')

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
        max_length=25)

    withdrawal_of_consent_reason = models.CharField(
        blank=True,
        null=True,
        max_length=75)

    rifampicin_started_since_week4 = models.CharField(
        choices=YES_NO,
        max_length=5)

    rifampicin_started_study_day = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(99)])

    arv_regiment = models.CharField(
        choices=ARV_REGIMEN,
        max_length=50)

    is_naive = models.CharField(
        choices=YES_NO,
        max_length=5)

    date_started_arvs = models.DateField(
        blank=True,
        null=True,
        validators=[date_not_future])

    date_switched_arvs = models.DateField(
        blank=True,
        null=True,
        validators=[date_not_future])

    efv_or_nvp = models.CharField(
        choices=FIRST_LINE_REGIMEN,
        max_length=3,
        verbose_name='If first line, on EFV or NVP?')
