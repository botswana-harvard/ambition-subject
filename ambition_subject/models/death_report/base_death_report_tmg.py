from django.db import models

from edc_constants.choices import YES_NO

from ...choices import CAUSE_OF_DEATH, TB_SITE_DEATH


class BaseDeathReportTmg(models.Model):

    cause_of_death = models.CharField(
        verbose_name='Main cause of death (opinion of TMG member)',
        max_length=50,
        choices=CAUSE_OF_DEATH,
        help_text='Tick only 1:(NB. Fill in AE CRF)')

    cause_of_death_agreed = models.CharField(
        verbose_name='Cause of death agreed between Study dr and TMG member?',
        max_length=5,
        choices=YES_NO,
        help_text='If No, complete Q10 below')

    cause_of_death_other = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='If other, please specify:')

    tb_site = models.CharField(
        verbose_name='If cause of death is TB, specify site of TB disease',
        max_length=25,
        choices=TB_SITE_DEATH,
        blank=True,
        null=True)

    death_narrative = models.TextField(
        verbose_name='Narrative')

    class Meta:
        abstract = True
