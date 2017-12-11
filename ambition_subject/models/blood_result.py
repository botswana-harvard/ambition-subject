from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from edc_action_item.model_mixins import ActionItemModelMixin
from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE, NO
from edc_identifier.model_mixins import TrackingIdentifierModelMixin
from edc_registration.models import RegisteredSubject
from edc_reportable import CELLS_PER_MILLIMETER_CUBED, MILLIMOLES_PER_LITER
from edc_reportable import IU_LITER, GRAMS_PER_DECILITER, TEN_X_9_PER_LITER, TEN_X_3_PER_LITER
from edc_reportable import site_reportables

from ..action_items import BloodResultAction
from ..choices import MG_MMOL_UNITS, MG_UMOL_UNITS, REPORTABLE
from .model_mixins import CrfModelMixin, BiosynexSemiQuantitativeCragMixin


class BloodResult(CrfModelMixin, ActionItemModelMixin, TrackingIdentifierModelMixin,
                  BiosynexSemiQuantitativeCragMixin):

    action_cls = BloodResultAction

    tracking_identifier_prefix = 'BR'

    wbc = models.DecimalField(
        verbose_name='WBC',
        decimal_places=1,
        max_digits=4,
        null=True,
        blank=True)

    wbc_units = models.CharField(
        verbose_name='units',
        max_length=10,
        choices=((TEN_X_3_PER_LITER, TEN_X_3_PER_LITER), ),
        default=TEN_X_3_PER_LITER,
        null=True,
        blank=True)

    wbc_abnormal = models.CharField(
        verbose_name='abnormal',
        choices=YES_NO,
        default=NO,
        max_length=6,
        null=True,
        blank=True)

    wbc_reportable = models.CharField(
        verbose_name='reportable',
        choices=REPORTABLE,
        default=NOT_APPLICABLE,
        max_length=6,
        null=True,
        blank=True)

    platelets = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(9999)],
        null=True,
        blank=True)

    platelets_units = models.CharField(
        verbose_name='units',
        max_length=10,
        choices=((TEN_X_9_PER_LITER, TEN_X_9_PER_LITER), ),
        default=TEN_X_9_PER_LITER,
        null=True,
        blank=True)

    platelets_abnormal = models.CharField(
        verbose_name='abnormal',
        choices=YES_NO,
        default=NO,
        max_length=6,
        null=True,
        blank=True)

    platelets_reportable = models.CharField(
        verbose_name='reportable',
        choices=REPORTABLE,
        default=NOT_APPLICABLE,
        max_length=6,
        null=True,
        blank=True)

    haemoglobin = models.DecimalField(
        decimal_places=1,
        max_digits=4,
        null=True,
        blank=True)

    haemoglobin_units = models.CharField(
        verbose_name='units',
        max_length=10,
        choices=((GRAMS_PER_DECILITER, GRAMS_PER_DECILITER), ),
        default=GRAMS_PER_DECILITER,
        null=True,
        blank=True)

    haemoglobin_abnormal = models.CharField(
        verbose_name='abnormal',
        choices=YES_NO,
        default=NO,
        max_length=6,
        null=True,
        blank=True)

    haemoglobin_reportable = models.CharField(
        verbose_name='reportable',
        choices=REPORTABLE,
        default=NOT_APPLICABLE,
        max_length=6,
        null=True,
        blank=True)

    neutrophil = models.DecimalField(
        decimal_places=2,
        max_digits=4,
        null=True,
        blank=True)

    neutrophil_units = models.CharField(
        verbose_name='units',
        max_length=10,
        choices=((TEN_X_9_PER_LITER, TEN_X_9_PER_LITER), ),
        default=TEN_X_9_PER_LITER,
        null=True,
        blank=True)

    neutrophil_abnormal = models.CharField(
        verbose_name='abnormal',
        choices=YES_NO,
        default=NO,
        max_length=6,
        null=True,
        blank=True)

    neutrophil_reportable = models.CharField(
        verbose_name='reportable',
        choices=REPORTABLE,
        default=NOT_APPLICABLE,
        max_length=6,
        null=True,
        blank=True)

    creatinine = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        null=True,
        blank=True)

    creatinine_units = models.CharField(
        verbose_name='units',
        choices=MG_UMOL_UNITS,
        max_length=6,
        null=True,
        blank=True)

    creatinine_abnormal = models.CharField(
        verbose_name='abnormal',
        choices=YES_NO,
        default=NO,
        max_length=6,
        null=True,
        blank=True)

    creatinine_reportable = models.CharField(
        verbose_name='reportable',
        choices=REPORTABLE,
        default=NOT_APPLICABLE,
        max_length=6,
        null=True,
        blank=True)

    sodium = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        null=True,
        blank=True)

    sodium_units = models.CharField(
        verbose_name='units',
        max_length=10,
        choices=((MILLIMOLES_PER_LITER, MILLIMOLES_PER_LITER), ),
        default=MILLIMOLES_PER_LITER,
        null=True,
        blank=True)

    sodium_abnormal = models.CharField(
        verbose_name='abnormal',
        choices=YES_NO,
        default=NO,
        max_length=6,
        null=True,
        blank=True)

    sodium_reportable = models.CharField(
        verbose_name='reportable',
        choices=REPORTABLE,
        default=NOT_APPLICABLE,
        max_length=6,
        null=True,
        blank=True)

    potassium = models.DecimalField(
        decimal_places=1,
        max_digits=2,
        null=True,
        blank=True)

    potassium_units = models.CharField(
        verbose_name='units',
        max_length=10,
        choices=((MILLIMOLES_PER_LITER, MILLIMOLES_PER_LITER), ),
        default=MILLIMOLES_PER_LITER,
        null=True,
        blank=True)

    potassium_abnormal = models.CharField(
        verbose_name='abnormal',
        choices=YES_NO,
        default=NO,
        max_length=6,
        null=True,
        blank=True)

    potassium_reportable = models.CharField(
        verbose_name='reportable',
        choices=REPORTABLE,
        default=NOT_APPLICABLE,
        max_length=6,
        null=True,
        blank=True)

    magnesium = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        null=True,
        blank=True)

    magnesium_units = models.CharField(
        verbose_name='units',
        choices=MG_MMOL_UNITS,
        null=True,
        blank=True,
        max_length=6)

    magnesium_abnormal = models.CharField(
        verbose_name='abnormal',
        choices=YES_NO,
        default=NO,
        null=True,
        blank=True,
        max_length=6)

    magnesium_reportable = models.CharField(
        verbose_name='reportable',
        choices=REPORTABLE,
        default=NOT_APPLICABLE,
        null=True,
        blank=True,
        max_length=6)

    alt = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(2999)],
        verbose_name='ALT',
        null=True,
        blank=True)

    alt_units = models.CharField(
        verbose_name='units',
        max_length=10,
        choices=((IU_LITER, IU_LITER), ),
        default=IU_LITER,
        null=True,
        blank=True)

    alt_abnormal = models.CharField(
        verbose_name='abnormal',
        choices=YES_NO,
        default=NO,
        max_length=6,
        null=True,
        blank=True)

    alt_reportable = models.CharField(
        verbose_name='reportable',
        choices=REPORTABLE,
        default=NOT_APPLICABLE,
        max_length=6,
        null=True,
        blank=True)

    urea = models.DecimalField(
        decimal_places=2,
        max_digits=6,
        null=True,
        blank=True)

    urea_units = models.CharField(
        verbose_name='units',
        choices=MG_MMOL_UNITS,
        max_length=6,
        null=True,
        blank=True)

    urea_abnormal = models.CharField(
        verbose_name='abnormal',
        choices=YES_NO,
        default=NO,
        max_length=6,
        null=True,
        blank=True)

    urea_reportable = models.CharField(
        verbose_name='reportable',
        choices=REPORTABLE,
        default=NOT_APPLICABLE,
        max_length=6,
        null=True,
        blank=True)

    cd4 = models.IntegerField(
        verbose_name='abs CD4',
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        blank=True,
        null=True)

    cd4_units = models.CharField(
        verbose_name='units',
        max_length=10,
        choices=((CELLS_PER_MILLIMETER_CUBED, CELLS_PER_MILLIMETER_CUBED), ),
        default=CELLS_PER_MILLIMETER_CUBED,
        null=True,
        blank=True)

    cd4_abnormal = models.CharField(
        verbose_name='abnormal',
        choices=YES_NO,
        default=NO,
        max_length=6,
        null=True,
        blank=True)

    cd4_reportable = models.CharField(
        verbose_name='reportable',
        choices=REPORTABLE,
        default=NOT_APPLICABLE,
        max_length=6,
        null=True,
        blank=True)

    results_abnormal = models.CharField(
        verbose_name='Are any of the above results abnormal?',
        choices=YES_NO,
        max_length=5)

    results_reportable = models.CharField(
        verbose_name='If any results are abnormal, are results within Grade III '
                     'or above?',
        max_length=5,
        choices=YES_NO_NA,
        help_text=('If YES, this value will open Adverse Event Form.<br/><br/>'
                   'Note: On Day 1 only abnormal bloods should not be reported as Adverse'
                   'Events.'))

    summary = models.TextField(
        null=True,
        blank=True)

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.summary = '\n'.join(self.get_summary())
        super().save(*args, **kwargs)

    def get_summary(self):
        registered_subject = RegisteredSubject.objects.get(
            subject_identifier=self.subject_visit.subject_identifier)
        opts = dict(
            gender=registered_subject.gender,
            dob=registered_subject.dob,
            report_datetime=self.subject_visit.report_datetime)
        summary = []
        for field in [f.name for f in self._meta.fields]:
            value = getattr(self, field)
            grp = site_reportables.get('ambition').get(field)
            if value and grp:
                units = getattr(self, f'{field}_units')
                opts.update(units=units)
                grade = grp.get_grade(value, **opts)
                if grade and grade.grade:
                    summary.append(
                        f'{field}: {grade.description}.')
                elif not grade:
                    normal = grp.get_normal(value, **opts)
                    if not normal:
                        summary.append(f'{field}: {value} {units} is abnormal')
        return summary

    @property
    def action_item_reason(self):
        return self.summary

    @property
    def abnormal(self):
        return self.results_abnormal

    @property
    def reportable(self):
        return self.results_reportable

    class Meta(CrfModelMixin.Meta):
        pass
