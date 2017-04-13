from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO

from ..choices import RANDOMISATION_NUMBER, REGIMEN


class SubjectRandomization(BaseUuidModel):

    hospital_admission_date = models.DateField(
        validators=[date_not_future],
        verbose_name='Date of hospital admission')

    inclusion_date = models.DateField(
        validators=[date_not_future],
        verbose_name='Date of inclusion')

    abnormal_mental_status = models.CharField(
        choices=YES_NO,
        max_length=5,
        help_text='Abnormal mental status is GCS<15')

    already_on_arvs = models.CharField(
        choices=YES_NO,
        max_length=5)

    arv_start_date = models.DateField(
        blank=True,
        null=True,
        validators=[date_not_future],
        verbose_name='If yes, ARV start date:')

    randomization_number = models.CharField(
        choices=RANDOMISATION_NUMBER,
        max_length=10)

    consent_form_signed = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Consent form signed and copy given to participant')

    regimen = models.CharField(
        choices=REGIMEN,
        max_length=15)

    history = HistoricalRecords()

    class Meta:
        app_label = 'ambition_subject'
        verbose_name = 'Screening and randomization'
