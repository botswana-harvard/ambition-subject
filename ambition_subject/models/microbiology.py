from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import date_not_future
from edc_constants.choices import NOT_APPLICABLE, YES_NO

from ..choices import (
    BACTERIA_TYPE, BLOOD_CULTURE_RESULTS_ORGANISM, BIOPSY_RESULTS_ORGANISM,
    CULTURE_RESULTS, POS_NEG_NA, URINE_CULTURE_RESULTS_ORGANISM)
from .model_mixins import CrfModelMixin


class Microbiology(CrfModelMixin):

    urine_culture_performed = models.CharField(
        max_length=5,
        choices=YES_NO,
        help_text='only for patients with >50 white cells in urine')

    date_urine_taken = models.DateField(
        validators=[date_not_future],
        null=True,
        blank=True)

    urine_culture_results = models.CharField(
        verbose_name='Urine culture results, if completed',
        max_length=10,
        choices=CULTURE_RESULTS,
        default=NOT_APPLICABLE)

    urine_culture_organism = models.CharField(
        verbose_name='If Positive, organism:',
        max_length=25,
        choices=URINE_CULTURE_RESULTS_ORGANISM,
        default=NOT_APPLICABLE)

    urine_culture_organism_other = models.CharField(
        verbose_name='If other, please specify:',
        max_length=50,
        null=True,
        blank=True)

    blood_culture_performed = models.CharField(
        max_length=5,
        choices=YES_NO)

    blood_culture_results = models.CharField(
        verbose_name='Blood culture results, if completed:',
        max_length=10,
        choices=CULTURE_RESULTS,
        default=NOT_APPLICABLE)

    date_blood_taken = models.DateField(
        validators=[date_not_future],
        null=True,
        blank=True)

    day_blood_taken = models.IntegerField(
        verbose_name='If Positive, Study day positive culture sample taken:',
        validators=[MinValueValidator(1), MaxValueValidator(70)],
        null=True,
        blank=True)

    blood_culture_organism = models.CharField(
        verbose_name='If growth positive, organism:',
        max_length=50,
        choices=BLOOD_CULTURE_RESULTS_ORGANISM,
        default=NOT_APPLICABLE)

    blood_culture_organism_other = models.CharField(
        verbose_name='If other, specify:',
        max_length=50,
        null=True,
        blank=True)

    bacteria_identified = models.CharField(
        verbose_name='If bacteria, type:',
        max_length=50,
        choices=BACTERIA_TYPE,
        default=NOT_APPLICABLE)

    bacteria_identified_other = models.CharField(
        verbose_name='If other, specify:',
        max_length=100,
        null=True,
        blank=True)

    sputum_afb_performed = models.CharField(
        verbose_name='afb microscopy performed?',
        max_length=5,
        choices=YES_NO,
        help_text='Was sputum afb done?')

    date_sputum_afb_taken = models.DateField(
        validators=[date_not_future],
        null=True,
        blank=True)

    sputum_results_afb = models.CharField(
        verbose_name='afb results',
        max_length=10,
        choices=POS_NEG_NA)

    sputum_performed = models.CharField(
        verbose_name='Culture performed?',
        max_length=5,
        choices=YES_NO,
        help_text='Was sputum culture done?')

    date_sputum_taken = models.DateField(
        validators=[date_not_future],
        null=True,
        blank=True)

    sputum_results_culture = models.CharField(
        verbose_name='Culture results:',
        max_length=10,
        choices=POS_NEG_NA)

    sputum_results_positive = models.CharField(
        verbose_name='If culture is positive, please specify:',
        max_length=50,
        null=True,
        blank=True)

    sputum_genexpert_performed = models.CharField(
        verbose_name='Sputum gene expert performed.',
        max_length=5,
        choices=YES_NO,
        help_text='Was sputum gene expert done?')

    date_sputum_genexpert_taken = models.DateField(
        validators=[date_not_future],
        null=True,
        blank=True)

    sputum_result_genexpert = models.CharField(
        verbose_name='Gene expert results:',
        max_length=15,
        choices=POS_NEG_NA)

    tissue_biopsy_taken = models.CharField(
        max_length=5,
        choices=YES_NO)

    tissue_biopsy_results = models.CharField(
        verbose_name='If yes, results:',
        max_length=10,
        choices=CULTURE_RESULTS,
        default=NOT_APPLICABLE)

    date_biopsy_taken = models.DateField(
        validators=[date_not_future],
        null=True,
        blank=True)

    day_biopsy_taken = models.IntegerField(
        verbose_name='If Positive, Study day positive culture sample taken:',
        validators=[MinValueValidator(1), MaxValueValidator(70)],
        null=True,
        blank=True)

    tissue_biopsy_organism = models.CharField(
        verbose_name='If growth positive, organism:',
        max_length=50,
        choices=BIOPSY_RESULTS_ORGANISM,
        default=NOT_APPLICABLE)

    tissue_biopsy_organism_other = models.CharField(
        verbose_name='If other, please specify:',
        max_length=50,
        null=True,
        blank=True)

    histopathology_report = models.TextField(
        null=True,
        blank=True)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'
        verbose_name_plural = 'Microbiology'
