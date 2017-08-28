from django.db import models

from edc_base.model_validators import date_not_future
from edc_base.model_managers import HistoricalRecords

from ..choices import (ACTIVITIES_MISSED, FLUCONAZOLE_DOSE,
                       RANKING_SCORE, YES_NO,
                       LOCATION_CARE, CARE_PROVIDER, TRANSPORT,
                       YES_NO_ND, YES_NO_ALREADY_ND)

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

    patient_help = models.CharField(
        verbose_name=('Does the patient require help from'
                      ' anybody for everyday activities? '),
        max_length=10,
        choices=YES_NO_ND,
        help_text=('For example eating, drinking, washing,'
                   ' brushing teeth, going to the toilet'))

    patient_problems = models.CharField(
        verbose_name='Has the illness left the patient with any other problems?',
        max_length=10,
        choices=YES_NO_ND)

    ranking_score = models.IntegerField(
        verbose_name='Modified Ranking score:',
        choices=RANKING_SCORE,
        null=True)

    history = HistoricalRecords()

    personal_he_spend = models.DecimalField(
        verbose_name='Over that last 4 weeks, how much have you '
        'spent on activities relating to your health?',
        decimal_places=2,
        max_digits=15,
        null=True,
        blank=True)

    proxy_he_spend = models.DecimalField(
        verbose_name='Over that last 4 weeks, how much'
        ' has someone else spent on activities relating to your health?',
        decimal_places=2,
        max_digits=15,
        null=True,
        blank=True)

    he_spend_last_4weeks = models.DecimalField(
        verbose_name='How much in total has been spent'
        ' on your healthcare in the last 4 weeks?',
        decimal_places=2,
        max_digits=4,
        null=True,
        blank=True)

    care_before_hospital = models.CharField(
        verbose_name='Have you received any treatment or care '
        'for your present condition, before coming to the hospital?',
        max_length=5,
        choices=YES_NO)

    location_care = models.CharField(
        verbose_name='If Yes, where did you receive treatment or care?',
        max_length=35,
        choices=LOCATION_CARE)

    location_care_other = OtherCharField(
        verbose_name='If Other Specify:',
        max_length=25,
        blank=True,
        null=True)

    transport_form = models.CharField(
        verbose_name='Which form of transport did you take to reach '
        'there?',
        max_length=5,
        choices=TRANSPORT)

    transport_cost = models.DecimalField(
        verbose_name='How much did you spend on the transport?',
        decimal_places=2,
        max_digits=4,
        null=True,
        blank=True)

    transport_duration = models.CharField(
        verbose_name='How long did it take you to reach there?',
        max_length=25,
        null=True,
        blank=True)

    care_provider = models.CharField(
        verbose_name='Who provided treatment or care for your'
        ' present condition, before coming to the hospital?',
        max_length=35,
        choices=CARE_PROVIDER)

    care_provider_other = OtherCharField(
        verbose_name='If Other Specify:',
        max_length=25,
        blank=True,
        null=True)

    paid_treatment = models.CharField(
        verbose_name='Did you pay for treatment of your present '
        'condition?',
        max_length=5,
        choices=YES_NO)

    paid_treatment_amount = models.DecimalField(
        verbose_name=(
            'How much did you pay for the treatment of your present '
            'condition?'),
        decimal_places=2,
        max_digits=4,
        null=True,
        blank=True)

    medication_bought = models.CharField(
        verbose_name=(
            'did you buy other medication '
            ' for the treatment of your present condition?'),
        max_length=5,
        choices=YES_NO)

    medication_payment = models.DecimalField(
        verbose_name=(
            'How much did you pay?'),
        decimal_places=2,
        max_digits=4,
        null=True,
        blank=True)

    other_place_visited = models.CharField(
        verbose_name='Before this, did you go to another place '
        'for the treatment of the present situation?',
        max_length=5,
        choices=YES_NO)

    duration_present_condition = models.CharField(
        verbose_name='How long have you been sick with your current '
        'condition?',
        max_length=25,
        blank=True,
        null=True)

    activities_missed = models.CharField(
        verbose_name='What would you have been doing '
        'if you were not sick with your present condition',
        max_length=15,
        choices=ACTIVITIES_MISSED)

    activities_missed_other = OtherCharField(
        verbose_name='If Other, Specify',
        max_length=25,
        blank=True,
        null=True)

    time_off_work = models.CharField(
        verbose_name='How much time did you take off work?',
        max_length=25,
        blank=True,
        null=True)

    carer_time_off = models.CharField(
        verbose_name='How much time did a caring family member take '
        'off work to accompany you to the hospital?',
        max_length=25,
        blank=True,
        null=True)

    loss_of_earnings = models.CharField(
        verbose_name='Did you lose earnings as a result?',
        max_length=5,
        choices=YES_NO)

    earnings_lost_amount = models.DecimalField(
        verbose_name='How much did you lose?',
        decimal_places=2,
        max_digits=4,
        blank=True,
        null=True)


class FollowUpDiagnoses(SignificantDiagnosesMixin):

    follow_up = models.ForeignKey(FollowUp)

    objects = FollowUpDiagnosesManager()

    def natural_key(self):
        return (self.possible_diagnoses, self.dx_date) + self.follow_up.natural_key()
    natural_key.dependencies = ['ambition_subject.followup']

    class Meta(CrfModelMixin.Meta):
        verbose_name_plural = 'Follow Up Diagnoses'
        unique_together = ('follow_up', 'possible_diagnoses', 'dx_date')
