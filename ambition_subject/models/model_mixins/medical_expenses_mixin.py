from django.core.validators import MinValueValidator
from django.db import models
from ambition_subject.choices import LOCATION_CARE, CURRENCY
from ambition_subject.choices import YES_NO, ACTIVITIES_MISSED, CARE_PROVIDER, TRANSPORT
from ambition_subject.validators import hm_validator, span_validator
from edc_base.model_fields.custom_fields import OtherCharField
from edc_constants.choices import YES_NO_NA


class MedicalExpensesMixin(models.Model):

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
        blank=True)

    proxy_he_spend = models.DecimalField(
        verbose_name='Over that last 4 weeks, how much'
        ' has someone else spent on activities relating to your health?',
        decimal_places=2,
        max_digits=15,
        null=True,
        blank=True)

    he_spend_last_4weeks = models.DecimalField(
        verbose_name='How much in total has been spent'
        ' on your healthcare in the last 4 weeks?',
        decimal_places=4,
        max_digits=8,
        null=True,
        blank=True)

    care_before_hospital = models.CharField(
        verbose_name='Have you received any treatment or care '
        'for your present condition, before coming to the hospital?',
        max_length=5,
        choices=YES_NO)

    location_care = models.CharField(
        verbose_name='If Yes, where did you receive treatment or care?',
        max_length=35,
        choices=LOCATION_CARE)

    location_care_other = OtherCharField()

    transport_form = models.CharField(
        verbose_name='Which form of transport did you take to reach '
        'there?',
        max_length=20,
        choices=TRANSPORT)

    transport_cost = models.DecimalField(
        verbose_name='How much did you spend on the transport (each way)?',
        decimal_places=2,
        max_digits=8,
        null=True,
        blank=True)

    transport_duration = models.CharField(
        verbose_name='How long did it take you to reach there?',
        max_length=25,
        null=True,
        blank=True)

    care_provider = models.CharField(
        verbose_name='Who provided treatment or care during that visit?',
        max_length=35,
        choices=CARE_PROVIDER)

    care_provider_other = OtherCharField(
        verbose_name='If Other Specify:',
        max_length=25,
        blank=True,
        null=True)

    paid_treatment = models.CharField(
        verbose_name=(
            'Did you pay for the treatment '
            'you received during that visit'),
        max_length=15,
        choices=YES_NO_NA)

    paid_treatment_amount = models.DecimalField(
        verbose_name=(
            'How much did you pay for this visit?'),
        decimal_places=2,
        max_digits=8,
        null=True,
        blank=True)

    medication_bought = models.CharField(
        verbose_name='Did you buy other medication for relief?',
        max_length=15,
        choices=YES_NO_NA)

    medication_payment = models.DecimalField(
        verbose_name=(
            'How much did you pay?'),
        decimal_places=2,
        max_digits=8,
        null=True,
        blank=True)

    other_place_visited = models.CharField(
        verbose_name='Before this, did you go to another place '
        'for the treatment of the present situation?',
        max_length=15,
        choices=YES_NO_NA)

#     duration_present_condition = models.CharField(
#         verbose_name='How long have you been sick with your current '
#         'condition?',
#         validators=[span_validator],
#         max_length=8,
#         null=True,
#         blank=True,
#         help_text='in days/weeks/months')

    duration_present_condition = models.IntegerField(
        verbose_name='How long have you been sick with your current '
        'condition?',
        validators=[MinValueValidator(0.5)],
        null=True,
        blank=True,
        help_text='in days')

    activities_missed = models.CharField(
        verbose_name='What would you have been doing '
        'if you were not sick with your present condition',
        max_length=25,
        choices=ACTIVITIES_MISSED)

    activities_missed_other = OtherCharField(
        verbose_name='If Other, Specify',
        max_length=25,
        blank=True,
        null=True)

    time_off_work = models.CharField(
        verbose_name='How much time did you take off work?',
        validators=[hm_validator],
        max_length=5,
        blank=True,
        null=True,
        help_text='in hours:minutes format')

    carer_time_off = models.CharField(
        verbose_name='How much time did a caring family member take '
        'off work to accompany you to the hospital?',
        validators=[hm_validator],
        max_length=5,
        blank=True,
        null=True,
        help_text='in hours:minutes format')

    loss_of_earnings = models.CharField(
        verbose_name='Did you lose earnings as a result?',
        max_length=5,
        choices=YES_NO,
        blank=True,
        null=True)

    earnings_lost_amount = models.DecimalField(
        verbose_name='How much did you lose?',
        decimal_places=2,
        max_digits=8,
        blank=True,
        null=True)

    class Meta:
        abstract = True
