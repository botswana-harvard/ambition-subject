from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO


class ClinicalAssessment(models.Model):

    physical_symptoms = models.CharField(
        verbose_name='Physical symptoms',
        max_length=5,
        choices=YES_NO)

    headache = models.CharField(
        verbose_name='Headache',
        max_length=5,
        choices=YES_NO)

    visual_acuity_left_eye = models.DecimalField(
        verbose_name='Viscuity Left Eye',
        decimal_places=3,
        max_digits=4)

    visual_acuity_right_eye = models.DecimalField(
        verbose_name='Viscuity Right Eye',
        decimal_places=3,
        max_digits=4,
    )

    glasgow_coma_score = models.IntegerField(
        verbose_name='Glasgow Coma Score',
        validators=[MaxValueValidator(15), MinValueValidator(3)])

    confusion = models.CharField(
        verbose_name='Confusion',
        max_length=5,
        choices=YES_NO,
    )

    recent_seizure_less_72 = models.CharField(
        verbose_name='Recent seizure (<72 hrs)',
        max_length=5,
        choices=YES_NO)

    cn_palsy = models.CharField(
        verbose_name='CN palsy',
        max_length=5,
        choices=YES_NO)

    behaviour_change = models.CharField(
        verbose_name='Behaviour change',
        max_length=5,
        choices=YES_NO)

    focal_neurology = models.CharField(
        verbose_name='Focal neurology',
        max_length=5,
        choices=YES_NO)

    tb_pulmonary_dx = models.CharField(
        verbose_name='Pulmonary TB diagnosis since the last visit?',
        max_length=5,
        choices=YES_NO)

    tb_pulmonary_dx_date = models.DateField(
        verbose_name='Date of pulmonary TB diagnosis',
        validators=[date_not_future],
        null=True,
        blank=True,)

    extra_pulmonary_tb_dx = models.CharField(
        verbose_name='Extra pulmonary TB diagnosis since the last visit?',
        max_length=5,
        choices=YES_NO)

    extra_tb_pulmonary_dx_date = models.DateField(
        verbose_name='Date of Extra Pulmonary TB diagnosis',
        validators=[date_not_future],
        null=True,
        blank=True,)

    kaposi_sarcoma_dx = models.CharField(
        verbose_name='Kaposi\'s sarcoma diagnosis since the last visit?',
        max_length=5,
        choices=YES_NO)

    kaposi_sarcoma_dx_date = models.DateField(
        verbose_name='Date of Kaposi\'s sarcoma diagnosis ',
        validators=[date_not_future],
        null=True,
        blank=True,)

    malaria_dx = models.CharField(
        verbose_name='Malaria diagnosis since the last visit?',
        max_length=5,
        choices=YES_NO)

    malaria_dx_date = models.DateField(
        verbose_name='Date of malaria diagnosis',
        validators=[date_not_future],
        null=True,
        blank=True,)

    bacteraemia_dx = models.CharField(
        verbose_name='Bacteraemia diagnosis since the last visit?',
        max_length=5,
        choices=YES_NO)

    bacteraemia_dx_date = models.DateField(
        verbose_name='Date of bacteraemia diagnosis',
        validators=[date_not_future],
        null=True,
        blank=True,)

    pneumonia_dx = models.CharField(
        verbose_name='Bacterial pneumonia diagnosis since the last visit?',
        max_length=5,
        choices=YES_NO)

    pneumonia_dx_date = models.DateField(
        verbose_name='Date of bacterial pneumonia diagnosis',
        validators=[date_not_future],
        null=True,
        blank=True,)

    diarrhoeal_wasting_dx = models.CharField(
        verbose_name='Diarrhoeal wasting diagnosis since the last visit?',
        max_length=5,
        choices=YES_NO)

    diarrhoeal_wasting_dx_date = models.DateField(
        verbose_name='Date of diarrhoeal wasting diagnosis',
        validators=[date_not_future],
        null=True,
        blank=True,)

    other_dx = models.CharField(
        verbose_name='Other diagnosis',
        max_length=50)

    class Meta():
        abstract = True
