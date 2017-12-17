from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import YES_NO_NA, NOT_APPLICABLE

from ..choices import LP_REASON, POS_NEG, MG_MMOL_UNITS, MM3_PERC_UNITS
from ..choices import YES_NO_NOT_DONE_WAIT_RESULTS
from .model_mixins import CrfModelMixin, BiosynexSemiQuantitativeCragMixin
from ambition_subject.constants import AWAITING_RESULTS


class LumbarPunctureCsf(CrfModelMixin, BiosynexSemiQuantitativeCragMixin):

    reason_for_lp = models.CharField(
        verbose_name='Reason for LP',
        max_length=50,
        choices=LP_REASON)

    opening_pressure = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)],
        help_text=mark_safe('Units cm of H<sub>2</sub>O'))

    closing_pressure = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(99)],
        help_text=mark_safe('Units cm of H<sub>2</sub>O'))

    csf_amount_removed = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='CSF amount removed ',
        validators=[MinValueValidator(1)],
        help_text='Units ml')

    quantitative_culture = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0), MaxValueValidator(9999999)],
        help_text='Units CFU/ml')

    csf_culture = models.CharField(
        verbose_name='Other organism (non-Cryptococcus)',
        max_length=18,
        choices=YES_NO_NOT_DONE_WAIT_RESULTS,
        default=AWAITING_RESULTS,
        help_text='Complete after getting the results.')

    other_csf_culture = models.CharField(
        verbose_name='If YES, specify organism:',
        max_length=75,
        blank=True,
        null=True)

    csf_wbc_cell_count = models.IntegerField(
        verbose_name='Total CSF WBC cell count:',
        help_text=mark_safe('acceptable units are mm<sup>3</sup>'),
        validators=[MinValueValidator(0), MaxValueValidator(999)],
        null=True)

    differential_lymphocyte_count = models.IntegerField(
        verbose_name='Differential lymphocyte cell count:',
        validators=[MinValueValidator(0), MaxValueValidator(999)],
        blank=True,
        null=True,
        help_text=mark_safe('acceptable units are mm<sup>3</sup> or %'))

    differential_lymphocyte_unit = models.CharField(
        choices=MM3_PERC_UNITS,
        max_length=6,
        null=True,
        blank=True)

    differential_neutrophil_count = models.IntegerField(
        verbose_name='Differential neutrophil cell count:',
        validators=[MinValueValidator(0), MaxValueValidator(999)],
        blank=True,
        null=True,
        help_text=mark_safe('acceptable units are mm<sup>3</sup> or %'))

    differential_neutrophil_unit = models.CharField(
        choices=MM3_PERC_UNITS,
        max_length=6,
        null=True,
        blank=True)

    india_ink = models.CharField(
        max_length=15,
        choices=POS_NEG,
        null=True,)

    csf_glucose = models.DecimalField(
        verbose_name='CSF glucose:',
        decimal_places=1,
        max_digits=3,
        blank=True,
        null=True,
        help_text='Units in mmol/L or mg/dL')

    csf_glucose_units = models.CharField(
        verbose_name='CSF glucose units:',
        max_length=6,
        choices=MG_MMOL_UNITS,
        blank=True,
        null=True,)

    csf_protein = models.DecimalField(
        verbose_name='CSF protein:',
        decimal_places=2,
        max_digits=4,
        blank=True,
        null=True,
        help_text='Units in g/dL')

    csf_cr_ag = models.CharField(
        verbose_name='CSF CrAg:',
        max_length=15,
        choices=POS_NEG,
        null=True)

    csf_cr_ag_lfa = models.CharField(
        verbose_name='CSF CrAg done by CSF CrAg LFA:',
        max_length=5,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        verbose_name = 'Lumbar puncture/Cerebrospinal fluid'
        verbose_name_plural = 'Lumbar puncture/Cerebrospinal fluid'
