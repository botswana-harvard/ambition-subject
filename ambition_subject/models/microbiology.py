from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_constants.choices import YES_NO, POS_NEG

from ..choices import (
    BLOOD_CULTURE_RESULTS_ORGANISM, BIOPSY_RESULTS_ORGANISM, CULTURE_RESULTS,
    POS_NEG_NA, URINE_CULTURE_RESULTS_ORGANISM)
from .model_mixins import CrfModelMixin


class Microbiology(CrfModelMixin):

    urine_culture_performed = models.CharField(
        choices=YES_NO,
        max_length=5)

    urine_culture_results = models.CharField(
        blank=True,
        choices=CULTURE_RESULTS,
        max_length=10,
        null=True,
        verbose_name='Urine culture results, if completed')

    urine_culture_organism = models.CharField(
        blank=True,
        choices=URINE_CULTURE_RESULTS_ORGANISM,
        max_length=25,
        null=True,
        verbose_name='If Positive, organism:')

    urine_culture_organism_other = models.CharField(
        blank=True,
        max_length=50,
        null=True,
        verbose_name='If other, please specify:')

    blood_culture_performed = models.CharField(
        choices=YES_NO,
        max_length=5)

    blood_culture_results = models.CharField(
        blank=True,
        choices=CULTURE_RESULTS,
        max_length=10,
        null=True,
        verbose_name='Blood culture results, if completed:')

    study_day_positive_blood_taken = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(70)],
        verbose_name='If Positive, Study day positive culture sample taken:')

    blood_culture_organism = models.CharField(
        blank=True,
        choices=BLOOD_CULTURE_RESULTS_ORGANISM,
        max_length=50,
        null=True,
        verbose_name='If growth positive, organism:')

    blood_culture_organism_other = models.CharField(
        blank=True,
        max_length=50,
        null=True,
        verbose_name='If other, specify:')

    sputum_results_afb = models.CharField(
        choices=POS_NEG,
        max_length=10)

    sputum_results_culture = models.CharField(
        choices=POS_NEG,
        max_length=10)

    sputum_results_if_positive = models.CharField(
        blank=True,
        max_length=50,
        null=True,
        verbose_name='If culture is positive, please specify:')

    sputum_result_genexpert = models.CharField(
        choices=POS_NEG_NA,
        max_length=15)

    tissue_biopsy_taken = models.CharField(
        choices=YES_NO,
        max_length=5)

    tissue_biopsy_results = models.CharField(
        blank=True,
        choices=CULTURE_RESULTS,
        max_length=10,
        null=True,
        verbose_name='If yes, results:')

    study_day_positive_biopsy_taken = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(70)],
        verbose_name='If Positive, Study day positive culture sample taken:')

    tissue_biopsy_organism = models.CharField(
        blank=True,
        choices=BIOPSY_RESULTS_ORGANISM,
        max_length=50,
        null=True,
        verbose_name='If growth positive, organism:')

    tissue_biopsy_organism_other = models.CharField(
        blank=True,
        max_length=50,
        null=True,
        verbose_name='If other, please specify:')

    histopathology_report = models.TextField(
        blank=True,
        null=True)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'
        verbose_name_plural = 'Microbiology'
