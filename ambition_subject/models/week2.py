from django.core.validators import MinValueValidator
from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_fields.custom_fields import OtherCharField
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO

from ..choices import (REASON_DRUG_MISSED, DAYS_MISSED)
from .list_models import Antibiotic, Day14Medication, OtherDrug
from .model_mixins import CrfModelMixin, ClinicalAssessment


class Week2(ClinicalAssessment, CrfModelMixin):

    discharged = models.CharField(
        verbose_name='Discharged?',
        max_length=25,
        choices=YES_NO)

    discharge_date = models.DateField(
        validators=[date_not_future],
        null=True,
        blank=True)

    died = models.CharField(
        verbose_name='Died?',
        max_length=25,
        choices=YES_NO)

    death_date = models.DateField(
        validators=[date_not_future],
        null=True,
        blank=True)

    ampho_start_date = models.DateField(
        verbose_name='Amphotericin B start date: ',
        validators=[date_not_future],
        null=True,
        blank=True)

    ampho_end_date = models.DateField(
        verbose_name='Amphotericin B end date: ',
        validators=[date_not_future],
        null=True,
        blank=True)

    ampho_duration = models.IntegerField(
        verbose_name='Amphotericin B treatment duration',
        null=True,
        blank=True)

    flucon_start_date = models.DateField(
        verbose_name='Fluconazole start date:',
        validators=[date_not_future],
        null=True,
        blank=True)

    flucon_stop_date = models.DateField(
        verbose_name='Fluconazole end date:',
        validators=[date_not_future],
        null=True,
        blank=True)

    flucon_duration = models.IntegerField(
        verbose_name='Fluconazole treatment duration:',
        null=True,
        blank=True)

    flucy_start_date = models.DateField(
        verbose_name='Flucytosine start date:',
        validators=[date_not_future],
        null=True,
        blank=True)

    flucy_stop_date = models.DateField(
        verbose_name='Flucytosine end date:',
        validators=[date_not_future],
        null=True,
        blank=True)

    flucy_duration = models.IntegerField(
        verbose_name='Flucytosine treatment duration:',
        null=True,
        blank=True)

    ambi_start_date = models.DateField(
        verbose_name='Ambisome start date:',
        validators=[date_not_future],
        null=True,
        blank=True)

    ambi_stop_date = models.DateField(
        verbose_name='Ambisome end date:',
        validators=[date_not_future],
        null=True,
        blank=True)

    ambi_duration = models.IntegerField(
        verbose_name='Ambisome treatment duration:',
        null=True,
        blank=True)

    other_drug = models.ManyToManyField(
        OtherDrug,
        verbose_name="Other drugs/interventions given during first 14 days",)

    other_drug_other = models.CharField(
        verbose_name='If other, please specify:',
        blank=True,
        max_length=50,
        null=True)

    antibiotic = models.ManyToManyField(
        Antibiotic,
        verbose_name="Were any of the following antibiotics given?",)

    antibiotic_other = models.CharField(
        verbose_name='If other antibiotics, please specify:',
        max_length=50,
        null=True,
        blank=True)

    blood_received = models.CharField(
        verbose_name='Blood transfusion received?',
        max_length=25,
        choices=YES_NO)

    units = models.IntegerField(
        verbose_name='If yes, No. of units',
        validators=[MinValueValidator(1)],
        null=True,
        blank=True)

    temperature = models.FloatField(
        verbose_name='Temperature',
        null=True,
        blank=True,
        default=None)

    weight = models.IntegerField(
        help_text='Weight in Kilograms')

    medicines = models.ManyToManyField(
        Day14Medication,
        verbose_name='Medicines receieved on Day 14:')

    medicine_other = models.CharField(
        verbose_name='If other, please specify:',
        max_length=50,
        null=True,
        blank=True)

    significant_dx = models.CharField(
        verbose_name='Other significant diagnoses since enrolment?',
        max_length=25,
        choices=YES_NO)

    significant_dx_datetime = models.DateTimeField(
        validators=[date_not_future],
        null=True,
        blank=True)

    flucon_missed_doses = models.CharField(
        verbose_name='Were any Fluconazole drug doses missed?',
        max_length=25,
        choices=YES_NO)

    amphotericin_missed_doses = models.CharField(
        verbose_name='Were any Amphotericin b drug doses missed?',
        max_length=25,
        choices=YES_NO)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'


class FluconazoleMissedDoses(BaseUuidModel):

    week2 = models.ForeignKey(Week2)

    day_missed = models.IntegerField(
        verbose_name='Day missed:',
        choices=DAYS_MISSED
    )

    flucon_missed_reason = models.CharField(
        verbose_name='Reason:',
        max_length=25,
        blank=True,
        choices=REASON_DRUG_MISSED)

    flucon_missed_reason_other = OtherCharField()

    class Meta:
        app_label = 'ambition_subject'
        unique_together = ('day_missed', 'flucon_missed_reason')


class AmphotericinMissedDoses(BaseUuidModel):

    week2 = models.ForeignKey(Week2)

    day_missed = models.IntegerField(
        verbose_name='Day:',
        choices=DAYS_MISSED
    )

    ampho_missed_reason = models.CharField(
        verbose_name='Were any drug doses missed?',
        max_length=25,
        choices=REASON_DRUG_MISSED)

    ampho_missed_reason_other = OtherCharField()

    class Meta:
        app_label = 'ambition_subject'
        unique_together = ('day_missed', 'ampho_missed_reason')
