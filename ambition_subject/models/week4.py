from django.db import models

from edc_base.model_fields.custom_fields import OtherCharField
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO

from ..choices import FLUCONAZOLE_DOSE, YES_NO_ALREADY_ND
from .model_mixins import (
    CrfModelMixin, ClinicalAssessment, SignificantDiagnosesMixin)


class Week4DiagnosesManager(models.Manager):

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


class Week4(ClinicalAssessment, CrfModelMixin):

    fluconazole_dose = models.CharField(
        verbose_name='Fluconazole dose (Day prior to visit)',
        max_length=25,
        choices=FLUCONAZOLE_DOSE)

    fluconazole_dose_other = OtherCharField(
        verbose_name='If other, specify dose:',
        max_length=25)

    rifampicin_started = models.CharField(
        verbose_name='Rifampicin started since last visit?',
        max_length=25,
        choices=YES_NO_ALREADY_ND)

    rifampicin_start_date = models.DateField(
        verbose_name='Date rifampicin started',
        validators=[date_not_future],
        null=True,
        blank=True,)

    lp_done = models.CharField(
        verbose_name='LP done?',
        max_length=5,
        choices=YES_NO,
        help_text='If yes, ensure LP CRF completed.')

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'


class Week4Diagnoses(SignificantDiagnosesMixin):

    week4 = models.ForeignKey(Week4)

    objects = Week4DiagnosesManager()

    def natural_key(self):
        return (self.possible_diagnoses, self.dx_date) + self.week4.natural_key()
    natural_key.dependencies = ['ambition_subject.week4']

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'
        verbose_name_plural = 'Significant Diagnoses'
        unique_together = ('week4', 'possible_diagnoses', 'dx_date')
