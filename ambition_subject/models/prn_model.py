from django.db import models
from edc_constants.choices import YES_NO

from .model_mixins import CrfModelMixin


class PrnModel(CrfModelMixin):

    adverse_event = models.CharField(
        verbose_name='Adverse event?',
        max_length=5,
        choices=YES_NO
    )

    microbiology = models.CharField(
        verbose_name='Microbiology?',
        max_length=5,
        choices=YES_NO
    )

    radiology = models.CharField(
        verbose_name='Radiology?',
        max_length=5,
        choices=YES_NO
    )

    recurrence_symptom = models.CharField(
        verbose_name='Recurrence of symptoms?',
        max_length=5,
        choices=YES_NO
    )

    protocol_deviation = models.CharField(
        verbose_name='Protocol Deviation?',
        max_length=5,
        choices=YES_NO
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'ambition_subject'
        verbose_name = 'PRN Forms'
