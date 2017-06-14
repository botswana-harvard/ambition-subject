from django.db import models
from django.utils import timezone


from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO, YES_NO_NA_SPECIFY

from ..choices import (ABNORMAL_RESULTS_REASON, BRAIN_IMAGINING_REASON,
                       CXR_TYPE, INFILTRATE_LOCATION)
from edc_base.model_mixins import BaseUuidModel


class Radiology(BaseUuidModel):

    is_cxr_done = models.CharField(
        verbose_name='Is CXR done',
        choices=YES_NO,
        max_length=5)

    cxr_date = models.DateField(
        verbose_name='If yes, when was CXR done',
        validators=[date_not_future],
        blank=True,
        null=True)

    cxr_type = models.CharField(
        verbose_name='If yes, specify CXR type:',
        blank=False,
        choices=CXR_TYPE,
        max_length=75,
        null=True)

    infiltrate_location = models.CharField(
        verbose_name='If CXR type is Infiltrate, please specify location:',
        blank=False,
        choices=INFILTRATE_LOCATION,
        max_length=10,
        null=True)

    cxr_description = models.TextField(
        verbose_name='Description/Comments:',
        blank=True,
        null=True)

    is_ct_performed = models.CharField(
        verbose_name='CT/MRI brain scan performed?:',
        choices=YES_NO,
        max_length=5)

    date_ct_performed = models.DateTimeField(
        default=timezone.now,
        editable=True)

    is_scanned_with_contrast = models.CharField(
        verbose_name='CT/MRI brain scan performed with contrast?:',
        blank=False,
        choices=YES_NO_NA_SPECIFY,
        max_length=5,
        null=False)

    brain_imaging_reason = models.CharField(
        verbose_name='Reason for brain imaging:',
        blank=False,
        choices=BRAIN_IMAGINING_REASON,
        max_length=25,
        null=True)

    brain_imaging_reason_other = models.CharField(
        verbose_name='If other, please specify:',
        blank=True,
        max_length=50,
        null=True)

    are_results_abnormal = models.CharField(
        blank=False,
        choices=YES_NO_NA_SPECIFY,
        null=False,
        max_length=5)

    abnormal_results_reason = models.CharField(
        verbose_name='If results are abnormal, what is the reason?:',
        blank=False,
        choices=ABNORMAL_RESULTS_REASON,
        max_length=50,
        null=True)

    abnormal_results_reason_other = models.CharField(
        verbose_name='If other, please specify reason:',
        blank=True,
        max_length=50,
        null=True)

    if_infarcts_location = models.CharField(
        verbose_name='If results are abnormal because of Infarcts, what is '
                     'the location?',
        blank=True,
        max_length=50,
        null=True)

    history = HistoricalRecords()

    class Meta(BaseUuidModel.Meta):
        app_label = 'ambition_subject'
        verbose_name_plural = 'Radiology'
