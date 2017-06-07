from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import date_not_future
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_constants.choices import YES_NO

from ..choices import DR_OPINION, STEROIDS_CHOICES
from .list_models import Neurological, MeningitisSymptom, AntibioticTreatment


class RecurrenceSymptom(BaseUuidModel):

    meningitis_symptom = models.ManyToManyField(
        MeningitisSymptom,
        blank=True,
        verbose_name='What are your current symptoms?')

    meningitis_symptom_other = models.CharField(
        verbose_name='If other symptom, please specify',
        max_length=50)

    patient_readmitted = models.CharField(
        verbose_name=('Has the patient been readmitted due to these recurrent'
                      'symptoms?'),
        max_length=5,
        choices=YES_NO,
        help_text='If Yes, complete AE CRF.')

    glasgow_coma_score = models.IntegerField(
        verbose_name='Score:',
        validators=[MinValueValidator(1), MaxValueValidator(15)],
        help_text='/15')

    recent_seizure = models.CharField(
        verbose_name=(
            'Recent seizure (<72 hrs):'),
        max_length=5,
        choices=YES_NO)

    behaviour_change = models.CharField(
        max_length=5,
        choices=YES_NO)

    confusion = models.CharField(
        max_length=5,
        choices=YES_NO)

    neurological = models.ManyToManyField(
        Neurological,
        blank=True,
        verbose_name='neurologic:')

    focal_neurologic_deficit = models.CharField(
        verbose_name='If focal neurologic deficit chosen, please specify',
        max_length=15,
        null=True,
        blank=True)

    cn_palsy = models.CharField(
        verbose_name='If CN Palsy chosen, please specify',
        max_length=15,
        null=True,
        blank=True)

    lp_completed = models.CharField(
        max_length=5,
        choices=YES_NO,
        help_text='If yes, complete LP form')

    amb_administered = models.CharField(
        max_length=5,
        choices=YES_NO)

    amb_duration = models.IntegerField(
        verbose_name='If yes, Specify length of course',
        validators=[MinValueValidator(1)],
        null=True,
        blank=True)

    tb_treatment = models.CharField(
        max_length=5,
        choices=YES_NO)

    steroids_administered = models.CharField(
        max_length=5,
        choices=YES_NO)

    steroids_duration = models.IntegerField(
        verbose_name='If yes, Specify length of course:',
        validators=[MinValueValidator(1)],
        null=True,
        blank=True)

    steroids_choices = models.CharField(
        verbose_name='If Yes',
        max_length=25,
        choices=STEROIDS_CHOICES)

    steroids_choices_other = models.CharField(
        blank=True,
        max_length=50,
        verbose_name='If other steroids, please specify')

    CD4_count = models.IntegerField(
        verbose_name='CD4 count (if available)',
        validators=[MinValueValidator(1)],
        null=True,
        blank=True)

    antibiotic_treatment = models.ManyToManyField(
        AntibioticTreatment,
        verbose_name='Antibiotics treatment',
        blank=True)

    antibiotic_treatment_other = models.CharField(
        verbose_name='If other antibiotic treatment, please specify',
        max_length=50,
        blank=True,
        null=True)

    on_arvs = models.CharField(
        max_length=5,
        choices=YES_NO)

    arv_date = models.DateField(
        verbose_name='Study date ARVs started.',
        validators=[date_not_future],
        null=True,
        blank=True)

    arvs_stopped = models.CharField(
        verbose_name='ARVs stopped this clinical episode?',
        max_length=5,
        choices=YES_NO)

    narrative_summary = models.TextField(
        verbose_name='Narrative Summary of recurrence of symptoms:',
        help_text=(
            'Please ensure the following forms have been completed:'
            ' LP, Bloods, Microbiology, Radiology'))

    dr_opinion = models.CharField(
        verbose_name='Study Dr’s opinion:',
        max_length=10,
        choices=DR_OPINION)

    dr_opinion_other = models.CharField(
        verbose_name='If other doctor opinion, please specify',
        blank=True,
        max_length=50,
        null=True)

    history = HistoricalRecords()

    class Meta(BaseUuidModel.Meta):
        app_label = 'ambition_subject'
