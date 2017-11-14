from django.core.validators import MinValueValidator
from django.db import models
from edc_constants.choices import YES_NO

from .model_mixins import CrfModelMixin


class EducationalBackground(CrfModelMixin):

    household_head = models.CharField(
        verbose_name='Are you head of the household?',
        max_length=5,
        choices=YES_NO)

    head_profession = models.CharField(
        verbose_name=('What is the head of household profession?'),
        max_length=25)

    head_education_years = models.IntegerField(
        verbose_name='How many years of education did '
        'head of houesehold complete?',
        validators=[MinValueValidator(1)])

    head_education_certificate = models.CharField(
        verbose_name='What is the head of household highest education '
        'certificate?',
        max_length=25)

    head_elementary = models.CharField(
        verbose_name='Did the head of household go to elementary '
        'school?',
        max_length=5,
        choices=YES_NO)

    head_attendance_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    head_secondary = models.CharField(
        verbose_name='Did head of household go to secondary school?',
        max_length=5,
        choices=YES_NO)

    head_secondary_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    head_higher_education = models.CharField(
        verbose_name='Did head of household go to higher education?',
        max_length=5,
        choices=YES_NO)

    head_higher_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)
