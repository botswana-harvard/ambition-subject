from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO, YES_NO_NA

from ..choices import (ARV_REGIMEN, FIRST_LINE_REGIMEN,
                       REASON_STUDY_TERMINATED, YES_NO_ALREADY)
from .model_mixins.crf_model_mixin import CrfModelMixin


class StudyTerminationConclusion(CrfModelMixin):

    date_patient_terminated = models.DateField(
        verbose_name='Date patient terminated on study:',
        validators=[date_not_future])

    date_last_study_fu = models.DateField(
        verbose_name='Date of last research follow up (if different):',
        validators=[date_not_future],
        blank=True,
        null=True)

    discharged_after_initial_admission = models.CharField(
        verbose_name='Was the patient discharged after initial admission?',
        max_length=6,
        choices=YES_NO)

    date_initial_discharge = models.DateField(
        verbose_name='Date of initial discharge',
        validators=[date_not_future],
        blank=True,
        null=True)

    readmission_after_initial_discharge = models.CharField(
        verbose_name='Was the patient readmitted following initial discharge?',
        max_length=7,
        choices=YES_NO)

    date_readmission = models.DateField(
        verbose_name='Date of readmission',
        validators=[date_not_future],
        blank=True,
        null=True)

    date_discharged = models.DateField(
        verbose_name='Date discharged',
        validators=[date_not_future],
        blank=True,
        null=True)

    termination_reason = models.CharField(
        verbose_name='Reason for study termination',
        max_length=75,
        choices=REASON_STUDY_TERMINATED,
        help_text=(
            'If included in error, be sure to fill in protocol deviation form.'))

    death_date = models.DateField(
        verbose_name='Date of Death',
        validators=[date_not_future],
        blank=True,
        null=True)

    consent_withdrawal_reason = models.CharField(
        verbose_name='Reason for withdrawing consent',
        max_length=75,
        blank=True,
        null=True)

    willing_to_complete_10W_FU = models.CharField(
        verbose_name='Is the patient willing to complete the 10 week FU '
        'visit only?',
        max_length=12,
        choices=YES_NO_NA)

    willing_to_complete_centre = models.CharField(
        verbose_name='Is the patient willing to complete the 10 week FU '
        'visit only at their new care centre?',
        max_length=17,
        choices=YES_NO_NA)

    date_willing_to_complete = models.DateField(
        verbose_name=' Date the 10W FU due',
        validators=[date_not_future],
        blank=True,
        null=True)

    included_in_error_date = models.DateField(
        verbose_name='If included in error, date',
        validators=[date_not_future],
        blank=True,
        null=True)

    included_in_error = models.TextField(
        verbose_name='If included in error, narrative:',
        max_length=300,
        blank=True,
        null=True
    )

    rifampicin_started = models.CharField(
        verbose_name='Rifampicin started since week 4?',
        max_length=30,
        choices=YES_NO_ALREADY)

    first_line_regimen_patients = models.CharField(
        verbose_name='ART regimen started for naive patients (or regimen'
        ' switched for those already on ARVs)',
        max_length=75,
        choices=ARV_REGIMEN)

    first_line_regimen_patients_other = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='If other, please specify:')

    date_arvs_started_or_switched = models.DateField(
        blank=True,
        null=True,
        validators=[date_not_future])

    first_line_env = models.CharField(
        verbose_name='If first line, on EFV or NVP and or DTG?',
        max_length=3,
        choices=FIRST_LINE_REGIMEN,
        null=True)

    arvs_delay_reason = models.CharField(
        verbose_name='Reason ARVs not started',
        max_length=75,
        blank=True,
        null=True)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'
        consent_model = 'ambition_subject.subjectconsent'
        verbose_name = 'Study Termination/Conclusion'
        verbose_name_plural = 'Study Terminations/Conclusions'
