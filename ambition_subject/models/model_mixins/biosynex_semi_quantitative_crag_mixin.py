from django.db import models

from edc_constants.choices import POS_NEG_ONLY, YES_NO_NA


class BiosynexSemiQuantitativeCragMixin(models.Model):

    bios_crag = models.CharField(
        verbose_name='Biosynex Semi-quantitative CrAg performed?',
        choices=YES_NO_NA,
        help_text='Gaborone and Blantyre only',
        max_length=5,
        blank=True,
        null=True)

    crag_control_result = models.CharField(
        verbose_name='Control result',
        choices=POS_NEG_ONLY,
        help_text='Gaborone and Blantyre only',
        max_length=5,
        blank=True,
        null=True)

    crag_t1_result = models.CharField(
        verbose_name='T1 result',
        choices=POS_NEG_ONLY,
        help_text='Gaborone and Blantyre only',
        max_length=5,
        blank=True,
        null=True)

    crag_t2_result = models.CharField(
        verbose_name='T2 result',
        choices=POS_NEG_ONLY,
        help_text='Gaborone and Blantyre only',
        max_length=5,
        blank=True,
        null=True)

    class Meta:
        abstract = True
