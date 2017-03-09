from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import YES_NO, YES_NO_NA, POS_NEG

from ..choices import LP_REASON
from .crf_metadata import CrfMetadata


class LpCsf(CrfMetadata):

    reason_for_lp = models.CharField(
        choices=LP_REASON,
        max_length=50)

    opening_pressure = models.IntegerField(
        help_text='Units cm of H2O',
        validators=[MinValueValidator(1), MaxValueValidator(99)])

    closing_pressure = models.IntegerField(
        blank=True,
        help_text='Units cm of H2O',
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(99)])

    csf_amount_removed = models.IntegerField(
        help_text='Do not remove ≥ 40mL CSF. See management of raised ICP WPD',
        validators=[MinValueValidator(1), MaxValueValidator(40)])

    quantitative_culture = models.IntegerField(
        blank=True,
        help_text='Units CFU/ml',
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(9999999)])

    csf_culture = models.CharField(
        choices=YES_NO_NA,
        max_length=5,
        verbose_name='CSF culture: Other organism (non-crytococcus)')

    other_csf_culture = models.CharField(
        max_length=75,
        verbose_name='If yes, specify organism:')

    csf_wbc_cell_count = models.IntegerField(
        help_text='Units in cubic millimeters',
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        verbose_name='Total CSF WBC cell count:')

    differential_lymphocyte_count = models.IntegerField(
        help_text='Units in cubic millimeters',
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        verbose_name='Differential lymphocyte cell count:')

    differential_neutrophil_count = models.IntegerField(
        help_text='Units in cubic millimeters',
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        verbose_name='Differential neutrophil cell count:')

    india_ink = models.CharField(
        choices=POS_NEG,
        max_length=15)

    csf_glucose = models.DecimalField(
        help_text='Units in mmol/L',
        decimal_places=1,
        max_digits=3)

    csf_protein = models.IntegerField(
        help_text='Units in mg/dL',
        validators=[MinValueValidator(1), MaxValueValidator(999)])

    csf_cr_ag = models.CharField(
        choices=POS_NEG,
        max_length=15,
        verbose_name='CSF CrAg:')

    csf_cr_ag_titres = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(9999)],
        verbose_name='CSF CrAg Titres:')

    csf_cr_ag_lfa = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='CSF CrAG done by CSF CrAG LFA:')

    history = HistoricalRecords()

    class Meta:
        app_label = 'ambition_subject'
        verbose_name = 'LP/CSF Form'
