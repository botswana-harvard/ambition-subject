from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import YES_NO

from ..choices import ABNORMAL_RESULTS_REASON, BRAIN_IMAGINING_REASON, CXR_TYPE
from .crf_metadata import CrfMetadata


class Radiology(CrfMetadata):

    is_cxr_done = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Is CXR done')

    cxr_type = models.CharField(
        choices=CXR_TYPE,
        max_length=75,
        verbose_name='')

    cxr_description = models.TextField(
        verbose_name='Description/Comments:')

    is_ct_performed = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='CT/MRI brain scan performed?:')

    is_scanned_with_contrast = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='CT/MRI brain scan performed with contrast?:')

    brain_imaging_reason = models.CharField(
        choices=BRAIN_IMAGINING_REASON,
        max_length=25,
        verbose_name='Reason for brain imaging:')

    brain_imaging_reason_other = models.CharField(
        blank=True,
        max_length=50,
        null=True,
        verbose='If other, please specify:')

    are_results_abnormal = models.CharField(
        choices=YES_NO,
        max_length=5)

    abnormal_results_reason = models.CharField(
        blank=True,
        choices=ABNORMAL_RESULTS_REASON,
        max_length=50,
        null=True,
        verbose_name='If results are abnormal, what is the reason?:')

    abnormal_results_reason_other = models.CharField(
        blank=True,
        max_length=50,
        null=True,
        verbose_name='If other, please specify reason:')

    if_infarcts_location = models.CharField(
        blank=True,
        max_length=50,
        null=True,
        verbose_name='If results are abnormal because of Infarcts, what is '
                     'the location?')

    history = HistoricalRecords()

    class Meta():
        app_label = 'ambition_subject'
        verbose_name_plural = 'Radiology'
