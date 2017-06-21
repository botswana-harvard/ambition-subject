from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import YES_NO

from .model_mixins import CrfModelMixin
from ..choices import MG_MMOL_UNITS


class BloodResult(CrfModelMixin):

    wbc = models.DecimalField(
        decimal_places=1,
        max_digits=4,
        help_text='units in 10^3/μL')

    platelets = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(9999)],
        help_text='units in 10^9/L')

    haemoglobin = models.DecimalField(
        decimal_places=1,
        max_digits=4,
        help_text='units in g/dL',)

    absolute_neutrophil = models.DecimalField(
        decimal_places=2,
        max_digits=4,
        help_text='units in 10^3/μL',)

    creatinine = models.DecimalField(
        decimal_places=2,
        max_digits=4,
        help_text='units in  mg/dL or mmol/L',)

    creatinine_unit = models.CharField(
        choices=MG_MMOL_UNITS,
        max_length=6)

    sodium = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        help_text='units in mmol/L')

    potassium = models.DecimalField(
        decimal_places=1,
        max_digits=2,
        help_text='units in mmol/L')

    magnesium = models.DecimalField(
        decimal_places=2,
        max_digits=4,
        help_text='units in  mg/dL or mmol/L')

    magnesium_unit = models.CharField(
        choices=MG_MMOL_UNITS,
        max_length=6)

    alt = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        verbose_name='ALT',
        help_text='units in U/L')

    urea = models.DecimalField(
        decimal_places=1,
        max_digits=4,
        help_text='units in  mg/dL or mmol/L')

    urea_unit = models.CharField(
        choices=MG_MMOL_UNITS,
        max_length=6)

    abs_cd4 = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        help_text='units in /mm^3',)

    proteinuria = models.CharField(
        choices=YES_NO,
        max_length=5)

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

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'
