from ambition_subject.choices import YES_NO, ACTIVITIES_MISSED, CURRENCY
from django.core.validators import MinValueValidator
from django.db import models
from edc_base.model_fields.custom_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import YES_NO_NA

from .model_mixins import CrfModelMixin


class MedicalExpenses(CrfModelMixin):

    currency = models.CharField(
        verbose_name='Which currency do you use?',
        max_length=20,
        choices=CURRENCY)

    personal_he_spend = models.DecimalField(
        verbose_name='Over that last 4 weeks, how much have you '
        'spent on activities relating to your health?',
        decimal_places=2,
        max_digits=15,
        null=True,
        validators=[MinValueValidator(0)])

    proxy_he_spend = models.DecimalField(
        verbose_name='Over that last 4 weeks, how much'
        ' has someone else spent on activities relating to your health?',
        decimal_places=2,
        max_digits=15,
        null=True,
        validators=[MinValueValidator(0)])

    he_spend_last_4weeks = models.DecimalField(
        verbose_name='How much in total has been spent'
        ' on your healthcare in the last 4 weeks?',
        decimal_places=2,
        max_digits=16,
        null=True,
        validators=[MinValueValidator(0)])

    care_before_hospital = models.CharField(
        verbose_name='Have you received any treatment or care '
        'for your present condition, before coming to the hospital?',
        max_length=5,
        choices=YES_NO,
        help_text="If Yes, please complete medical expenses part 2")

    duration_present_condition = models.IntegerField(
        verbose_name='How long have you been sick with your current '
        'condition?',
        validators=[MinValueValidator(1)],
        null=True,
        help_text='in days')

    activities_missed = models.CharField(
        verbose_name='What would you have been doing '
        'if you were not sick with your present condition',
        max_length=25,
        null=True,
        choices=ACTIVITIES_MISSED)

    activities_missed_other = OtherCharField(
        verbose_name='If Other, Specify',
        max_length=25,
        blank=True,
        null=True)

    time_off_work = models.DecimalField(
        verbose_name='How much time did you take off work?',
        max_digits=4,
        decimal_places=1,
        validators=[MinValueValidator(0.5)],
        blank=True,
        null=True,
        help_text='in days')

    carer_time_off = models.IntegerField(
        verbose_name='How much time did a caring family member take '
        'off work to accompany you to the hospital?',
        validators=[MinValueValidator(0.5)],
        null=True,
        help_text='in days')

    loss_of_earnings = models.CharField(
        verbose_name='Did you lose earnings as a result?',
        max_length=5,
        choices=YES_NO_NA)

    earnings_lost_amount = models.DecimalField(
        verbose_name='How much did you lose?',
        decimal_places=2,
        max_digits=15,
        validators=[MinValueValidator(0)],
        null=True,
        blank=True)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        verbose_name = 'Health Economics: Medical Expenses'
        verbose_name_plural = 'Health Economics: Medical Expenses'
