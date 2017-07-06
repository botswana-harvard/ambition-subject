from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import YES_NO, YES_NO_NA

from ..choices import LP_REASON, POS_NEG, MG_MMOL_UNITS, MM3_PERC_UNITS
from .model_mixins import CrfModelMixin
from edc_constants.constants import NOT_APPLICABLE


class LumbarPunctureCsf(CrfModelMixin):

    reason_for_lp = models.CharField(
        verbose_name='Reason for LP',
        max_length=50,
        choices=LP_REASON)

    opening_pressure = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)],
        help_text='Units cm of H2O')

    closing_pressure = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(99)],
        help_text='Units cm of H2O')

    csf_amount_removed = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(40)],
        help_text='Do not remove ≥ 40mL CSF. See management of raised ICP WPD')

    quantitative_culture = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(9999999)],
        help_text='Units CFU/ml')

    csf_culture = models.CharField(
        verbose_name='CSF culture: Other organism (non-crytococcus)',
        max_length=5,
        choices=YES_NO_NA)

    other_csf_culture = models.CharField(
        verbose_name='If yes, specify organism:',
        max_length=75,
        blank=True,
        null=True)

    csf_wbc_cell_count = models.IntegerField(
        verbose_name='Total CSF WBC cell count:',
        help_text='acceptable units are mm3',
        validators=[MinValueValidator(0), MaxValueValidator(999)],
        null=True)

    differential_lymphocyte_count = models.IntegerField(
        verbose_name='Differential lymphocyte cell count:',
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        blank=True,
        null=True,
        help_text='acceptable units are mm3 or %')

    differential_lymphocyte_unit = models.CharField(
        choices=MM3_PERC_UNITS,
        max_length=6,
        default=NOT_APPLICABLE)

    differential_neutrophil_count = models.IntegerField(
        verbose_name='Differential neutrophil cell count:',
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        blank=True,
        null=True,
        help_text='acceptable units are mm3 or %')

    differential_neutrophil_unit = models.CharField(
        choices=MM3_PERC_UNITS,
        max_length=3,
        default=NOT_APPLICABLE)

    india_ink = models.CharField(
        max_length=15,
        choices=POS_NEG,
        null=True,)

    csf_glucose = models.DecimalField(
        decimal_places=1,
        max_digits=3,
        blank=True,
        null=True,
        help_text='Units in mmol/L or mg/dL')

    csf_glucose_units = models.CharField(
        max_length=6,
        choices=MG_MMOL_UNITS,
        default=NOT_APPLICABLE,
        blank=True,
        null=True,)

    csf_protein = models.DecimalField(
        decimal_places=1,
        max_digits=3,
        blank=True,
        null=True,
        help_text='Units in g/dL')

    csf_cr_ag = models.CharField(
        verbose_name='CSF CrAg:',
        max_length=15,
        choices=POS_NEG,
        null=True)

    csf_cr_ag_lfa = models.CharField(
        verbose_name='CSF CrAG done by CSF CrAG LFA:',
        max_length=5,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'
        verbose_name = 'Lumbar Puncture/Cerebrospinal Fluid'
        verbose_name_plural = 'Lumbar Puncture/Cerebrospinal Fluid'
