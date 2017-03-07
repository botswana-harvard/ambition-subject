from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future, datetime_is_future
from edc_constants.choices import YES_NO

from .list_models import AEClassification

from ..choices import (
    AE_SEVERITY, AE_INTENSITY, PATIENT_TREATMENT_GROUP, RAE_REASON,
    STUDY_DRUG_RELATIONSHIP)


class AdverseEvent(BaseUuidModel):

    ae_awareness_date = models.DateField(
        verbose_name='AE Awareness date',
        validators=[date_not_future])

    description = models.TextField(
        verbose_name='Adverse Event (AE) description')

    ae_start_date = models.DateField(
        validators=[date_not_future],
        verbose_name='Actual Start Date of AE')

    ae_severity = models.CharField(
        choices=AE_SEVERITY,
        max_length=25,
        verbose_name='Severity of AE')

    ae_intensity = models.CharField(
        choices=AE_INTENSITY,
        max_length=25,
        verbose_name='What is the intensity of the AE?')

    patient_treatment_group = models.CharField(
        choices=PATIENT_TREATMENT_GROUP,
        max_length=50,
        verbose_name='Patient’s treatment group')

    incident_study_relationship = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Is the incident related to patient involvement in the '
                     'study?')

    incident_drug_relationship_ambisome = models.CharField(
        choices=STUDY_DRUG_RELATIONSHIP,
        max_length=25,
        verbose_name='Relationship to study drug Ambisome:')

    incident_drug_relationship_fluconozole = models.CharField(
        choices=STUDY_DRUG_RELATIONSHIP,
        max_length=25,
        verbose_name='Relationship to study drug Fluconozole:')

    last_implicated_medication_administered_datetime = models.DateTimeField(
        validators=[datetime_is_future],
        verbose_name='Date and time of last implicated study medication '
                     'administered')

    last_implicated_medication = models.CharField(
        max_length=50,
        verbose_name='Last implicated study medicine:')

    last_implicated_medication_dose = models.CharField(
        max_length=50,
        verbose_name='Last implicated study medicine dose:')

    last_implicated_medication_route = models.CharField(
        max_length=50,
        verbose_name='Last implicated study medicine route:')

    other_ae_event_cause = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Has a reason other than the specified study drug been '
                     ' identified as the cause of the event(s)?')

    other_ae_event_cause_specify = models.CharField(
        blank=True,
        max_length=100,
        null=True,
        verbose_name='If yes, specify')

    action_taken_treatment = models.TextField(
        verbose_name='Specify action taken for treatment of AE:')

    recurrence_cm_symptoms = models.CharField(
        choices=YES_NO,
        help_text='If yes, fill in the Recurrence of Symptoms form',
        max_length=5,
        verbose_name='Was the AE a recurrence of CM symptoms?')

    is_sae_event = models.CharField(
        choices=YES_NO,
        help_text='(i.e. results in death, in-patient '
                  'hospitalisation/prolongation, significant disability or is '
                  'life-threatening)',
        max_length=5,
        verbose_name='Is this event a SAE?')

    sae_event_reason = models.CharField(
        blank=True,
        choices=RAE_REASON,
        null=True,
        max_length=50,
        verbose_name='If Yes, Reason for SAE:')

    is_susar = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Is this a Suspected Unexpected Serious Adverse Reaction '
                     '(SUSAR)?')

    susar_reported = models.CharField(
        blank=True,
        choices=YES_NO,
        null=True,
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

    ae_form_received_datetime = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Date and time AE form received:')

    clinical_review_datetime = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Date and time of Clinical Review: ')

    investigator_comments = models.TextField(
        blank=True,
        null=True,
        verbose_name='Investigator Comments:')

    ae_classification = models.ManyToManyField(
        AEClassification,
        related_name='ae_classification',
        verbose_name='Classification of AE (Tick all that apply):')

    investigator_ae_description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Description of AE:')

    regulatory_officials_notified_datetime = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Date and time Regulatory authorities notified (SUSARs)')

    history = HistoricalRecords()

    class Meta:
        app_label = 'ambition_subject'
        verbose_name = 'Adverse Event'
