from django.db import models

from edc_base.model_validators import date_not_future
from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import YES_NO

from ..choices import FLUCONAZOLE_DOSE, RANKING_SCORE, YES_NO_ND

from .model_mixins import (
    CrfModelMixin, ClinicalAssessment, SignificantDiagnosesMixin)
from edc_base.model_fields.custom_fields import OtherCharField


class FollowUpDiagnosesManager(models.Manager):

    def get_by_natural_key(self, possible_diagnoses, dx_date, subject_identifier,
                           visit_schedule_name, schedule_name, visit_code):
        return self.get(
            possible_diagnoses=possible_diagnoses,
            dx_date=dx_date,
            subject_visit__subject_identifier=subject_identifier,
            subject_visit__visit_schedule_name=visit_schedule_name,
            subject_visit__schedule_name=schedule_name,
            subject_visit__visit_code=visit_code
        )


class FollowUp(ClinicalAssessment, CrfModelMixin):

    fluconazole_dose = models.CharField(
        verbose_name='Fluconazole dose (Day prior to visit)',
        max_length=25,
        choices=FLUCONAZOLE_DOSE)

    fluconazole_dose_other = OtherCharField(
        verbose_name='Other fluconazole, specify',
        max_length=25)

    rifampicin_started = models.CharField(
        verbose_name='Rifampicin started since last visit?',
        max_length=5,
        choices=YES_NO_ND)

    rifampicin_start_date = models.DateField(
        verbose_name='Date rifampicin started',
        validators=[date_not_future],
        null=True,
        blank=True,)

    patient_help = models.CharField(
        verbose_name=('Does the patient require help from'
                      ' anybody for everyday activities? '),
        max_length=5,
        choices=YES_NO,
        help_text=('For example eating, drinking, washing,'
                   ' brushing teeth, going to the toilet'))

    patient_problems = models.CharField(
        verbose_name='Has the illness left the patient with any other problems?',
        max_length=5,
        choices=YES_NO)

    ranking_score = models.IntegerField(
        verbose_name='Modified Ranking score:',
        choices=RANKING_SCORE)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'


class FollowUpDiagnoses(SignificantDiagnosesMixin):

    follow_up = models.ForeignKey(FollowUp)

    objects = FollowUpDiagnosesManager()

    def natural_key(self):
        return (self.possible_diagnoses, self.dx_date) + self.follow_up.natural_key()
    natural_key.dependencies = ['ambition_subject.followup']

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'
        verbose_name_plural = 'Significant Diagnoses'
        unique_together = ('possible_diagnoses', 'dx_date')
