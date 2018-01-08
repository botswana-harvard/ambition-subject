from django.db import models
from django.utils.safestring import mark_safe
from edc_base.model_managers import HistoricalRecords
from edc_constants.choices import YES_NO

from .model_mixins import CrfModelMixin
from .list_models import MissedDoses


class PkPdCrf(CrfModelMixin):

    albumin = models.IntegerField(
        verbose_name='Albumin',
        null=True,
        blank=True,
        help_text='Units in g/L')

    ambisome_dose = models.IntegerField(
        verbose_name='Ambisome dose given',
        null=True,
        blank=True,
        help_text='Units in mg')

    ambisome_started_datetime = models.DateTimeField(
        verbose_name='Date and time Ambisome infusion started?',
        null=True,
        blank=True)

    ambisome_ended_datetime = models.DateTimeField(
        verbose_name='Date and time Ambisome infusion stopped',
        null=True,
        blank=True)

    full_ambisome_dose_given = models.CharField(
        verbose_name='Was the entire Ambisome dose given?',
        choices=YES_NO,
        max_length=5,
        null=True,
        blank=True)

    flucytosine_dose = models.IntegerField(
        verbose_name='What was the dose of Flucytosine given?',
        null=True,
        blank=True,
        help_text='Units in mg')

    flucytosine_dose_one_datetime = models.DateTimeField(
        verbose_name=mark_safe(
            'Date and time Flucytosine <u>DOSE&nbsp;1</u> was swallowed?'),
        null=True,
        blank=True)

    flucytosine_dose_two_datetime = models.DateTimeField(
        verbose_name=mark_safe(
            'Date and time Flucytosine <u>DOSE&nbsp;2</u> was swallowed?'),
        null=True,
        blank=True)

    flucytosine_dose_three_datetime = models.DateTimeField(
        verbose_name=mark_safe(
            'Date and time Flucytosine <u>DOSE&nbsp;3</u> was swallowed?'),
        null=True,
        blank=True)

    flucytosine_dose_four_datetime = models.DateTimeField(
        verbose_name=mark_safe(
            'Date and time Flucytosine <u>DOSE&nbsp;4</u> was swallowed?'),
        null=True,
        blank=True)

    flucytosine_missed = models.CharField(
        verbose_name='Were any Flucytosine doses missed?',
        choices=YES_NO,
        max_length=5,
        null=True,
        blank=True)

    flucytosine_dose_missed = models.ManyToManyField(
        MissedDoses,
        verbose_name='Which dose(s) was/were missed?',
        blank=True)

    reason_flucytosine_dose_missed = models.CharField(
        verbose_name='Why was/were the dose(s) missed?',
        max_length=75,
        null=True,
        blank=True)

    fluconazole_dose_given = models.IntegerField(
        verbose_name='What was the dose of Fluconazole given?',
        null=True,
        blank=True,
        help_text='Units in mg')

    fluconazole_dose_datetime = models.DateTimeField(
        verbose_name='Date and time Fluconazole was swallowed?',
        null=True,
        blank=True)

    fluconazole_dose_missed = models.CharField(
        verbose_name='Was the Fluconazole dose missed?',
        choices=YES_NO,
        max_length=5,
        null=True,
        blank=True)

    reason_fluconazole_dose_missed = models.CharField(
        verbose_name='Why was the Fluconazole dose missed?',
        max_length=75,
        null=True,
        blank=True)

    blood_sample_one_datetime = models.DateTimeField(
        verbose_name=mark_safe(
            'Date and time blood <u>SAMPLE&nbsp;1</u> taken?'),
        null=True,
        blank=True)

    blood_sample_two_datetime = models.DateTimeField(
        verbose_name=mark_safe(
            'Date and time blood <u>SAMPLE&nbsp;2</u> taken?'),
        null=True,
        blank=True)

    blood_sample_three_datetime = models.DateTimeField(
        verbose_name=mark_safe(
            'Date and time blood <u>SAMPLE&nbsp;3</u> taken?'),
        null=True,
        blank=True)

    blood_sample_four_datetime = models.DateTimeField(
        verbose_name=mark_safe(
            'Date and time blood <u>SAMPLE&nbsp;4</u> taken?'),
        null=True,
        blank=True)

    blood_sample_five_datetime = models.DateTimeField(
        verbose_name=mark_safe(
            'Date and time blood <u>SAMPLE&nbsp;5</u> taken?'),
        null=True,
        blank=True)

    blood_sample_six_datetime = models.DateTimeField(
        verbose_name=mark_safe(
            'Date and time blood <u>SAMPLE&nbsp;6</u> taken?'),
        null=True,
        blank=True)

    blood_sample_missed = models.CharField(
        verbose_name='Were any blood samples missed?',
        choices=YES_NO,
        max_length=5,
        null=True,
        blank=True)

    reason_blood_sample_missed = models.CharField(
        verbose_name='Why was/were the blood sample(s) missed??',
        max_length=75,
        null=True,
        blank=True)

    pre_dose_lp = models.CharField(
        verbose_name='Is this a pre-dose LP?',
        choices=YES_NO,
        max_length=5,
        null=True,
        blank=True)

    post_dose_lp = models.CharField(
        verbose_name='Is this a post-dose LP?',
        choices=YES_NO,
        max_length=5,
        null=True,
        blank=True)

    time_csf_sample_taken = models.DateTimeField(
        verbose_name='What date and time was the CSF sample taken?',
        null=True,
        blank=True)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        verbose_name = 'PK/PD'
        verbose_name_plural = 'PK/PD'
