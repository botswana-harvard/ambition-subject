from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO

from ..choices import ARV_REGIMEN, FIRST_LINE_REGIMEN, REASON_STUDY_TERMINATED
from .model_mixins.crf_model_mixin import CrfModelMixin
from edc_base.model_fields.custom_fields import OtherCharField


class StudyTerminationConclusion(CrfModelMixin):
    
    date_patient_terminated = models.DateField(
        verbose_name='Date patient terminated study',
        validators=[date_not_future])
    
    date_last_study_fu = models.DateField(
        verbose_name='Date of last follow-up as part of the study',
        validators=[date_not_future])
    
    discharged_after_initial_admission = models.CharField(
        verbose_name='Was patient discharged after initial admission?',
        max_length=6,
        choices= YES_NO)
    
    date_initial_discharge = models.DateField(
        verbose_name='Date of initial discharge',
        validators=[date_not_future],
        blank=True,
        null=True)
         
    readmission_after_initial_discharge = models.CharField(
        verbose_name='Was the patient readmitted following intial discharge?',
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
        choices=REASON_STUDY_TERMINATED)
    
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
        verbose_name='Is the patient willing to complete the 10 week FU visit only?',
        max_length=12,
        choices=YES_NO)
    
    willing_to_complete_centre = models.CharField(
        verbose_name='Is the patient willing to complete the 10 week FU visit only at their new care centre?',
        max_length=17,
        choices=YES_NO)
    
    date_willing_to_complete = models.DateField(
        verbose_name=' Date the 10W FU due',
        validators=[date_not_future],
        blank=True,
        null=True)
    
    late_protocol_exclusion = models.CharField(
        verbose_name='late protocol exclusion met?',
        max_length=4,
        choices=YES_NO)
    
    rifampicin_started= models.CharField(
        verbose_name='Rifampicin started since week 4?',
        max_length=5,
        choices=YES_NO)
    
    included_in_error = models.CharField(
        verbose_name='Included in error',
        max_length=75,
        blank=True,
        null=True)
    
    first_line_regimen_patients = models.CharField(
        verbose_name='First line ARV regimen started for naive patients (or regimen switched for those already on ARVs)',
        max_length=75,
        choices=ARV_REGIMEN)
    
    first_line_regimen_patients_other = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='If other, please specify:')
    
    second_line_regimen_patients = models.CharField(
        verbose_name='Second line ARV regimen started for naive patients (or regimen switched for those already on ARVs)',
        max_length=75,
        choices=ARV_REGIMEN)
    
    second_line_regimen_patients_other = OtherCharField()
    
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
    
    class Meta:
        app_label='ambition_subject'
        consent_model = 'ambition_subject.subjectconsent'
         
    
    
    
    
    