from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from edc_base.model_managers import HistoricalRecords
from edc_base.model_validators import datetime_not_future
from edc_constants.choices import YES_NO
from edc_reportable import CELLS_PER_MILLIMETER_CUBED_DISPLAY
from edc_reportable import MILLIMOLES_PER_LITER, MILLIGRAMS_PER_DECILITER

from ..choices import FLUCYTOSINE_DOSE_MISSED
from .model_mixins import CrfModelMixin


class PkPdCrf(CrfModelMixin):

    weight = models.IntegerField(
        verbose_name='Patient weight',
        validators=[MinValueValidator(1), MaxValueValidator(9999)],
        null=True,
        help_text='in kg')

    cd4_cell_count = models.IntegerField(
        verbose_name='CD4 cell count',
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        null=True,
        help_text=f'in {CELLS_PER_MILLIMETER_CUBED_DISPLAY}')

    on_art = models.CharField(
        verbose_name='On Antiretroviral treatment?',
        choices=YES_NO,
        max_length=5,
        null=True)

    other_medication = models.CharField(
        verbose_name='Any other medication?',
        choices=YES_NO,
        max_length=5,
        null=True)

    albumin = models.IntegerField(
        verbose_name='Albumin',
        null=True)

    creatine_clearance = models.IntegerField(
        verbose_name='Creatine Clearance',
        null=True)

    potassium = models.IntegerField(
        verbose_name='Potassium',
        null=True,
        help_text=f'in {MILLIMOLES_PER_LITER}')

    magnesium = models.IntegerField(
        verbose_name='Magnesium',
        null=True,
        help_text=f'in {MILLIGRAMS_PER_DECILITER}')

    haemoglobin = models.IntegerField(
        verbose_name='Haemoglobin',
        null=True)

    ambisome_dose = models.IntegerField(
        verbose_name='Ambisome dose given',
        null=True,
        help_text='Units in mg')

    ambisome_dose_time_started = models.TimeField(
        verbose_name='Time Ambisome infusion started?',
        max_length=5,
        null=True)

    ambisome_dose_time_ended = models.TimeField(
        verbose_name='Time Ambisome infusion stopped',
        max_length=5,
        null=True)

    full_ambisome_dose_given = models.CharField(
        verbose_name='Was the entire Ambisome dose given?',
        choices=YES_NO,
        max_length=5,
        null=True)

    flucytosine_dose = models.IntegerField(
        verbose_name='What was  the dose of Flucytosine given?',
        null=True,
        help_text='Units in mg')

    flucytosine_dose_one_time = models.TimeField(
        verbose_name=mark_safe(
            'Time Flucytosine <u>DOSE&nbsp;1</u> was swallowed?'),
        max_length=5,
        null=True)

    flucytosine_dose_two_time = models.TimeField(
        verbose_name=mark_safe(
            'Time Flucytosine <u>DOSE&nbsp;2</u> was swallowed?'),
        null=True)

    flucytosine_dose_three_time = models.TimeField(
        verbose_name=mark_safe(
            'Time Flucytosine <u>DOSE&nbsp;3</u> was swallowed?'),
        null=True)

    flucytosine_dose_four_time = models.TimeField(
        verbose_name=mark_safe(
            'Time Flucytosine <u>DOSE&nbsp;4</u> was swallowed?'),
        null=True)

    flucytosine_doses_missed = models.CharField(
        verbose_name='Were any Flucytosine doses missed?',
        choices=YES_NO,
        max_length=5,
        null=True)

    flucytosine_dose_missed = models.CharField(
        verbose_name='Which dose(s) was/were missed?',
        choices=FLUCYTOSINE_DOSE_MISSED,
        max_length=5,
        null=True)

    reason_flucytosine_dose_missed = models.CharField(
        verbose_name='Why was/were the dose(s) missed?',
        max_length=75,
        blank=True,
        null=True)

    fluconazole_dose_given = models.IntegerField(
        verbose_name='What was the dose of Fluconazole given?',
        blank=True,
        null=True,
        help_text='Units in mg')

    time_fluconazole_dose_given = models.TimeField(
        verbose_name='Time Fluconazole was swallowed?',
        max_length=5,
        blank=True,
        null=True)

    fluconazole_dose_missed = models.CharField(
        verbose_name='Was the Fluconazole dose missed?',
        choices=YES_NO,
        max_length=5,
        null=True)

    reason_fluconazole_dose_missed = models.CharField(
        verbose_name='Was the Fluconazole dose missed?',
        max_length=75,
        blank=True,
        null=True)

    blood_sample_one_day_one = models.TimeField(
        verbose_name=mark_safe('Time blood <u>SAMPLE&nbsp;1</u> taken?'),
        max_length=5,
        blank=True,
        null=True)

    blood_sample_two_day_one = models.TimeField(
        verbose_name=mark_safe('Time blood <u>SAMPLE&nbsp;2</u> taken?'),
        max_length=5,
        blank=True,
        null=True)

    blood_sample_three_day_one = models.TimeField(
        verbose_name=mark_safe('Time blood <u>SAMPLE&nbsp;3</u> taken?'),
        max_length=5,
        blank=True,
        null=True)

    blood_sample_four_day_one = models.TimeField(
        verbose_name=mark_safe('Time blood <u>SAMPLE&nbsp;4</u> taken?'),
        max_length=5,
        blank=True,
        null=True)

    blood_sample_five_day_one = models.TimeField(
        verbose_name=mark_safe('Time blood <u>SAMPLE&nbsp;5</u> taken?'),
        max_length=5,
        blank=True,
        null=True)

    any_day_one_sample_missed = models.CharField(
        verbose_name='Were any blood sample missed?',
        choices=YES_NO,
        max_length=5,
        null=True)

    reason_day_one_missed = models.CharField(
        verbose_name='Why was/were the blood sample(s) missed??',
        max_length=75,
        blank=True,
        null=True)

    blood_sample_one_day_seven = models.TimeField(
        verbose_name=mark_safe('Time blood <u>SAMPLE&nbsp;1</u> taken?'),
        max_length=5,
        null=True)

    blood_sample_two_day_seven = models.TimeField(
        verbose_name=mark_safe('Time blood <u>SAMPLE&nbsp;2</u> taken?'),
        max_length=5,
        null=True)

    blood_sample_three_day_seven = models.TimeField(
        verbose_name=mark_safe('Time blood <u>SAMPLE&nbsp;3</u> taken?'),
        max_length=5,
        null=True)

    blood_sample_four_day_seven = models.TimeField(
        verbose_name=mark_safe('Time blood <u>SAMPLE&nbsp;4</u> taken?'),
        max_length=5,
        null=True)

    blood_sample_five_day_seven = models.TimeField(
        verbose_name=mark_safe('Time blood <u>SAMPLE&nbsp;5</u> taken?'),
        max_length=5,
        null=True)

    blood_sample_six_day_seven = models.TimeField(
        verbose_name=mark_safe('Time blood <u>SAMPLE&nbsp;6</u> taken?'),
        max_length=5,
        null=True)

    any_day_seven_sample_missed = models.CharField(
        verbose_name='Were any blood sample missed?',
        choices=YES_NO,
        max_length=5,
        null=True)

    reason_day_seven_missed = models.CharField(
        verbose_name='Why was/were the blood sample(s) missed?',
        max_length=75,
        null=True,
        blank=True)

    pre_dose_lp = models.CharField(
        verbose_name='Is this a pre-dose LP?',
        choices=YES_NO,
        max_length=5,
        null=True)

    post_dose_lp = models.CharField(
        verbose_name='Is this a post-dose LP?',
        choices=YES_NO,
        max_length=5,
        null=True)

    second_pre_dose_lp = models.CharField(
        verbose_name='Is this a pre-dose LP?',
        choices=YES_NO,
        max_length=5,
        null=True)

    second_post_dose_lp = models.CharField(
        verbose_name='Is this a post-dose LP?',
        choices=YES_NO,
        max_length=5,
        null=True)

    time_csf_sample_taken = models.TimeField(
        verbose_name='What time was the CSF sample taken?',
        choices=YES_NO,
        max_length=5,
        null=True)

    extra_csf_samples_time = models.TimeField(
        verbose_name=('If any further CSF samples were taken, please add '
                      'here the exact time sample was taken'),
        max_length=5,
        null=True)

    extra_csf_samples_date = models.DateField(
        verbose_name=('If any further CSF samples were taken, '
                      'please add here the exact date sample was taken'),
        validators=[datetime_not_future],
        max_length=5,
        null=True)

    extra_blood_samples_time = models.TimeField(
        verbose_name=('If any further blood samples were taken, '
                      'please add here the exact time sample was taken'),
        max_length=5,
        null=True)

    extra_blood_samples_date = models.DateField(
        verbose_name=('If any further blood samples were taken, '
                      'please add here the exact date sample was taken'),
        validators=[datetime_not_future],
        max_length=5,
        null=True)

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        verbose_name = 'PK/PD'
        verbose_name_plural = 'PK/PD'
