from django.db import models

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

    ae_start_date = models.DateField(
        validators=[date_not_future],
        verbose_name='Actual Start Date of AE')

    ae_severity_grade = models.CharField(
        choices=AE_SEVERITY,
        max_length=25,
        verbose_name='Severity of AE')

    ae_intensity = models.CharField(
        choices=AE_INTENSITY,
        max_length=25,
        verbose_name='What is the intensity AE')

    regimen = models.CharField(  # TODO: Get this from the Randomization
        # choices=PATIENT_TREATMENT_GROUP,
        max_length=50,
        verbose_name='Patient’s treatment regimen')

    ae_study_relation_possibility = models.CharField(
        choices=YES_NO_UNKNOWN,
        max_length=10,
        verbose_name=(
            'Is the incident related to the patient involvement in the study?'))

    possiblity_detail = models.TextField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name='If No or Unknown, please give a short explanation.')

    ambisome_relation = models.CharField(
        choices=STUDY_DRUG_RELATIONSHIP,
        max_length=25,
        verbose_name='Relationship to Ambisome:')

    fluconazole_relation = models.CharField(
        choices=STUDY_DRUG_RELATIONSHIP,
        max_length=25,
        verbose_name='Relationship to Fluconozole:')

    amphotericin_b_relation = models.CharField(
        choices=STUDY_DRUG_RELATIONSHIP,
        max_length=25,
        verbose_name='Relationship to Amphotericin B:')

    flucytosine_relation = models.CharField(
        choices=STUDY_DRUG_RELATIONSHIP,
        max_length=25,
        verbose_name='Relationship to Flucytosine:')

    details_last_study_drug = models.CharField(
        max_length=100,
        verbose_name='Details of the last study drug administered.')

    med_administered_datetime = models.DateTimeField(
        validators=[datetime_not_future],
        verbose_name='Date and time of last implicated study medication '
                     'administered')

    implicated_med = models.CharField(
        max_length=50,
        verbose_name='Last implicated study medicine:')

    implicated_med_dose = models.CharField(
        max_length=50,
        verbose_name='Last implicated study medicine dose:')

    implicated_med_route = models.CharField(
        max_length=50,
        verbose_name='Last implicated study medicine route:')

    ae_cause = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Has a reason other than the specified study drug been '
                     ' identified as the cause of the event(s)?')

    ae_cause_other = OtherCharField(
        blank=True,
        max_length=100,
        null=True,
        verbose_name='If yes, specify')

    ae_treatment = models.TextField(
        verbose_name='Specify action taken for treatment of AE:')

    ae_cm_recurrence = models.CharField(  # TODO: If yes Use rule group to open recurrence form
        default=UNKNOWN,
        choices=YES_NO_UNKNOWN,
        help_text='If yes, fill in the Recurrence of Symptoms form',
        max_length=10,
        verbose_name='Was the AE a recurrence of CM symptoms?')

    is_sa_event = models.CharField(
        choices=YES_NO,
        help_text='(i.e. results in death, in-patient '
                  'hospitalisation/prolongation, significant disability or is '
                  'life-threatening)',
        max_length=5,
        verbose_name='Is this event a SAE?')

    # TODO: If reason == Death Use rule group to open Death form
    sae_possibility = models.CharField(
        choices=RAE_REASON,
        default=NOT_APPLICABLE,
        max_length=50,
        verbose_name='If Yes, Reason for SAE:')

    susar_possility = models.CharField(
        verbose_name=(
            'Is this a Suspected Unexpected Serious Adverse Reaction (SUSAR)?'),
        choices=YES_NO,
        max_length=5)

    susar_reported = models.CharField(
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        max_length=5,
        verbose_name='If yes, SUSAR must be reported to Principal '
                     'Investigator and TMG immediately, is SUSAR Reported?')

    susar_reported_datetime = models.DateTimeField(
        blank=True,
        help_text='AEs ≥ Grade 3 or SAE must be reported to the Trial '
                  'Management Group (TMG) within 48hrs (Email to: '
                  'ambition_tmg@sgul.ac.uk)',
        null=True,
        verbose_name='Date and time AE reported')

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'
        verbose_name = 'Adverse Event'
