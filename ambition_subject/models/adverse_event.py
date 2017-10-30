from django.db import models
from django.utils import timezone

from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import date_not_future, datetime_not_future
from edc_constants.choices import YES_NO, YES_NO_NA, YES_NO_UNKNOWN
from edc_constants.constants import NOT_APPLICABLE, UNKNOWN

from ..choices import AE_SEVERITY, AE_INTENSITY, RAE_REASON
from ..choices import STUDY_DRUG_RELATIONSHIP

from .model_mixins import CrfModelMixin


class AdverseEvent(CrfModelMixin):

    ae_description = models.TextField(
        verbose_name='Adverse Event (AE) description')

    ae_awareness_date = models.DateField(
        verbose_name='AE Awareness date',
        default=timezone.now,
        validators=[date_not_future])

    ae_start_date = models.DateField(
        verbose_name='Actual Start Date of AE',
        default=timezone.now,
        validators=[date_not_future])

    ae_severity_grade = models.CharField(
        verbose_name='Severity of AE',
        max_length=25,
        choices=AE_SEVERITY)

    ae_intensity = models.CharField(
        verbose_name='What is the intensity AE',
        max_length=25,
        choices=AE_INTENSITY)

    regimen = models.CharField(  # TODO: Get this from the Randomization
        verbose_name='Patient’s treatment regimen',
        max_length=50,
        help_text='Single Dose: (Ambisome 10 mg/kg day 1 (single dose) + '
        'fluconazole 1200mg/day + flucytosine 100mg/kg/day for 14 days); '
        'Control: (Amphotericin B 1 mg/kg for 7 days followed by fluconazole '
        '1200mg/day for 7 days, both given with flucytosine 100mg/kg/day for '
        '14 days)')

    ae_study_relation_possibility = models.CharField(
        verbose_name=(
            'Is the incident related to the patient involvement in the study?'),
        max_length=10,
        choices=YES_NO_UNKNOWN)

    ambisome_relation = models.CharField(
        verbose_name='Relationship to Ambisome:',
        max_length=25,
        choices=STUDY_DRUG_RELATIONSHIP)

    fluconazole_relation = models.CharField(
        verbose_name='Relationship to Fluconozole:',
        max_length=25,
        choices=STUDY_DRUG_RELATIONSHIP)

    amphotericin_b_relation = models.CharField(
        verbose_name='Relationship to Amphotericin B:',
        max_length=25,
        choices=STUDY_DRUG_RELATIONSHIP)

    flucytosine_relation = models.CharField(
        verbose_name='Relationship to Flucytosine:',
        max_length=25,
        choices=STUDY_DRUG_RELATIONSHIP)

    details_last_study_drug = models.TextField(
        verbose_name='Details of the last implicated drug (name, dose, route):',
        max_length=1000,
        null=True,
        blank=True)

    med_administered_datetime = models.DateTimeField(
        verbose_name='Date and time of last implicated study medication '
                     'administered',
        validators=[datetime_not_future],
        null=True,
        blank=True)

    ae_cause = models.CharField(
        verbose_name='Has a reason other than the specified study drug been '
                     ' identified as the cause of the event(s)?',
        choices=YES_NO,
        max_length=5)

    ae_cause_other = OtherCharField(
        verbose_name='If yes, specify',
        max_length=250,
        blank=True,
        null=True)

    ae_treatment = models.TextField(
        verbose_name='Specify action taken for treatment of AE:')

    ae_cm_recurrence = models.CharField(  # TODO: If yes Use rule group to open recurrence form
        verbose_name='Was the AE a recurrence of CM symptoms?',
        max_length=10,
        choices=YES_NO,
        default=UNKNOWN,
        help_text='If yes, fill in the Recurrence of Symptoms form')

    sa_event = models.CharField(
        verbose_name='Is this event a SAE?',
        max_length=5,
        choices=YES_NO,
        help_text='(i.e. results in death, in-patient '
                  'hospitalisation/prolongation, significant disability or is '
                  'life-threatening)')

    sae_possibility = models.CharField(
        verbose_name='If Yes, Reason for SAE:',
        max_length=50,
        choices=RAE_REASON,
        default=NOT_APPLICABLE)

    susar_possility = models.CharField(
        verbose_name=(
            'Is this a Suspected Unexpected Serious Adverse Reaction (SUSAR)?'),
        choices=YES_NO,
        max_length=5)

    susar_reported = models.CharField(
        verbose_name='If yes, SUSAR must be reported to Principal '
                     'Investigator and TMG immediately, is SUSAR Reported?',
        max_length=5,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,)

    susar_reported_datetime = models.DateTimeField(
        verbose_name='Date and time AE reported',
        blank=True,
        null=True,
        help_text='AEs ≥ Grade 3 or SAE must be reported to the Trial '
                  'Management Group (TMG) within 48hrs (Email to: '
                  'ambition_tmg@sgul.ac.uk)')

    history = HistoricalRecords()
