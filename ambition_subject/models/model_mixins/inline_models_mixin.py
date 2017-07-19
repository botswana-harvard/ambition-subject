from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_fields.custom_fields import OtherCharField
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO_NA

from ...choices import (REASON_DRUG_MISSED, DAYS_MISSED,
                        DOSES_MISSED, SIGNIFICANT_DX)


class SignificantDiagnosesMixin(BaseUuidModel):

    other_significant_diagnoses = models.CharField(
        verbose_name='Other significant diagnosis since last visit?',
        max_length=5,
        choices=YES_NO_NA)

    possible_diagnoses = models.CharField(
        verbose_name='Significant diagnoses:',
        max_length=25,
        choices=SIGNIFICANT_DX,
        blank=True,
        null=True
    )

    dx_date = models.DateField(
        verbose_name='Date of diagnosis:',
        validators=[date_not_future],
        null=True,
        blank=True)

    dx_other = models.CharField(
        verbose_name='If other, please specify:',
        max_length=50,
        null=True,
        blank=True)

    history = HistoricalRecords()

    class Meta:
        abstract = True


class FluconazoleMissedDosesMixin(BaseUuidModel):

    flucon_day_missed = models.IntegerField(
        verbose_name='Day missed:',
        choices=DAYS_MISSED
    )

    flucon_missed_reason = models.CharField(
        verbose_name='Reason:',
        max_length=25,
        blank=True,
        choices=REASON_DRUG_MISSED)

    missed_reason_other = OtherCharField()

    history = HistoricalRecords()

    class Meta:
        abstract = True


class AmphotericinMissedDosesMixin(BaseUuidModel):

    ampho_day_missed = models.IntegerField(
        verbose_name='Day missed:',
        choices=DAYS_MISSED
    )

    ampho_missed_reason = models.CharField(
        verbose_name='Reason:',
        max_length=25,
        blank=True,
        choices=REASON_DRUG_MISSED)

    missed_reason_other = OtherCharField()

    history = HistoricalRecords()

    class Meta:
        abstract = True


class FlucytosineMissedDosesMixin(BaseUuidModel):

    flucy_day_missed = models.IntegerField(
        verbose_name='Day missed:',
        choices=DAYS_MISSED
    )

    flucy_doses_missed = models.IntegerField(
        verbose_name='Doses missed:',
        choices=DOSES_MISSED
    )

    flucy_missed_reason = models.CharField(
        verbose_name='Reason:',
        max_length=25,
        blank=True,
        choices=REASON_DRUG_MISSED)

    missed_reason_other = OtherCharField()

    history = HistoricalRecords()

    class Meta:
        abstract = True
