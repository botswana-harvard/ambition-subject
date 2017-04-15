from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import date_not_future
from edc_constants.choices import POS_NEG, YES_NO
from edc_metadata.models import CrfMetadata


class BloodResults(CrfMetadata):

    wbc = models.DecimalField(
        decimal_places=1,
        help_text='units in 10^3/',
        max_digits=4)

    platelets = models.IntegerField(
        help_text='units in 10^9/L',
        validators=[MinValueValidator(1), MaxValueValidator(9999)])

    haemoglobin = models.DecimalField(
        decimal_places=1,
        help_text='units in g/dL',
        max_digits=4)

    absolute_neutrophil = models.DecimalField(
        decimal_places=2,
        help_text='units in 10^3/μL',
        max_digits=4)

    creatinine = models.DecimalField(
        decimal_places=2,
        help_text='units in mg/dL',
        max_digits=4)

    sodium = models.IntegerField(
        help_text='units in mmol/L',
        validators=[MinValueValidator(1), MaxValueValidator(999)])

    potassium = models.DecimalField(
        decimal_places=1,
        help_text='units in mmol/L',
        max_digits=2)

    magnesium = models.DecimalField(
        decimal_places=3,
        help_text='units in mg/dL',
        max_digits=4)

    total_bilirubin = models.DecimalField(
        decimal_places=1,
        help_text='units in mg/dL',
        max_digits=4)

    alt = models.IntegerField(
        help_text='units in U/L',
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        verbose_name='ALT')

    crp = models.DecimalField(
        decimal_places=1,
        help_text='units in U/L',
        max_digits=4,
        verbose_name='CRP')

    urea = models.IntegerField(
        help_text='units in mg/dL',
        validators=[MinValueValidator(1), MaxValueValidator(999)])

    abs_cd4 = models.IntegerField(
        help_text='units in /mm^3',
        validators=[MinValueValidator(1), MaxValueValidator(999)])

    proteinuria = models.CharField(
        choices=YES_NO,
        max_length=5)

    urine_cr_ag = models.CharField(
        choices=POS_NEG,
        max_length=10,
        verbose_name='Urine CrAg')

    are_results_normal = models.CharField(
        choices=YES_NO,
        max_length=5)

    abnormal_results_in_ae_range = models.CharField(
        blank=True,
        choices=YES_NO,
        max_length=5,
        null=True,
        verbose_name='If results abnormal, are results within Grade III/IV '
                     'AE range?')

    history = HistoricalRecords()

    class Meta:
        app_label = 'ambition_subject'

