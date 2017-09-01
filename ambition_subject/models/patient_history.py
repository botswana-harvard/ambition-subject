from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from edc_base.model_fields import OtherCharField, IsDateEstimatedField
from edc_base.model_validators import date_not_future
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE

from ..choices import (FIRST_LINE_REGIMEN, FIRST_ARV_REGIMEN,
                       TB_SITE, ECOG_SCORE, ACTIVITIES_MISSED,
                       SECOND_ARV_REGIMEN, LOCATION_CARE,
                       TRANSPORT, CARE_PROVIDER)
from ..validators import bp_validator
from .list_models import Medication, Neurological
from .list_models import PreviousOpportunisticInfection, Symptom
from .model_mixins import CrfModelMixin


class PatientHistory(CrfModelMixin):

    symptom = models.ManyToManyField(
        Symptom,
        blank=True,
        related_name='symptoms',
        verbose_name='What are your current symptoms?')

    headache_duration = models.IntegerField(
        verbose_name='If headache, how many days did it last?',
        validators=[MinValueValidator(1)],
        null=True,
        blank=True)

    visual_loss_duration = models.IntegerField(
        verbose_name='If visual loss, how many days did it last?',
        validators=[MinValueValidator(1)],
        null=True,
        blank=True)

    tb_history = models.CharField(
        verbose_name='Previous medical history of Tuberculosis?',
        max_length=5,
        choices=YES_NO)

    tb_site = models.CharField(
        verbose_name='If Yes, site of TB?',
        max_length=15,
        choices=TB_SITE,
        default=NOT_APPLICABLE)

    tb_treatment = models.CharField(
        verbose_name='Are you currently taking TB treatment?',
        max_length=5,
        choices=YES_NO)

    taking_rifampicin = models.CharField(
        verbose_name='If yes, are you currently also taking Rifampicin?',
        max_length=5,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE)

    rifampicin_started_date = models.DateField(
        verbose_name='If yes, when did you first start taking Rifampicin?',
        validators=[date_not_future],
        null=True,
        blank=True)

    previous_non_tb_oi = models.ManyToManyField(
        PreviousOpportunisticInfection,
        blank=True,
        related_name='previousopportunisticinfection',
        verbose_name='Previous opportunistic infection other than TB?',)

    previous_non_tb_oi_other = models.CharField(
        verbose_name='If other, please specify',
        null=True,
        blank=True,
        max_length=50)

    previous_non_tb_oi_date = models.DateField(
        verbose_name='If yes, what was the date of infection?',
        validators=[date_not_future],
        null=True,
        blank=True)

    new_hiv_diagnosis = models.CharField(
        verbose_name='Is this a new HIV diagnosis?',
        max_length=5,
        choices=YES_NO)

    taking_arv = models.CharField(
        verbose_name='If No, Already taking ARVs?',
        max_length=5,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE)

    arv_date = models.DateField(
        verbose_name='If yes, date ARVs were started.',
        validators=[date_not_future],
        null=True,
        blank=True)

    first_arv_regimen = models.CharField(
        verbose_name='Drug used in first line arv regimen',
        max_length=50,
        choices=FIRST_ARV_REGIMEN,
        default=NOT_APPLICABLE)

    first_arv_regimen_other = OtherCharField()

    second_arv_regimen = models.CharField(
        verbose_name='Second line arv regimen',
        max_length=50,
        choices=SECOND_ARV_REGIMEN,
        default=NOT_APPLICABLE)

    second_arv_regimen_other = OtherCharField()

    first_line_choice = models.CharField(
        verbose_name='If first line:',
        max_length=5,
        choices=FIRST_LINE_REGIMEN,
        default=NOT_APPLICABLE)

    patient_adherence = models.CharField(
        verbose_name='Is the patient reportedly adherent?',
        max_length=5,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE)

    last_dose = models.IntegerField(
        verbose_name='If no, how many months since the last dose '
        'was taken?',
        validators=[MinValueValidator(1)],
        null=True,
        blank=True)

    last_viral_load = models.DecimalField(
        verbose_name='Last Viral Load, if known?',
        decimal_places=3,
        max_digits=10,
        null=True,
        blank=True,
        help_text='copies/mL')

    viral_load_date = models.DateField(
        verbose_name='Viral load date',
        validators=[date_not_future],
        null=True,
        blank=True
    )

    vl_date_estimated = IsDateEstimatedField(
        blank=True,
        null=True,
        verbose_name=("Is the subject's viral load date estimated?"))

    last_cd4 = models.IntegerField(
        verbose_name='Last CD4, if known?',
        validators=[MinValueValidator(1), MaxValueValidator(2500)],
        null=True,
        blank=True)

    cd4_date = models.DateField(
        verbose_name='CD4 date',
        validators=[date_not_future],
        null=True,
        blank=True
    )

    cd4_date_estimated = IsDateEstimatedField(
        verbose_name=("Is the subject's CD4 date estimated?"),
        blank=True,
        null=True)

    temp = models.DecimalField(
        verbose_name='Temperature:',
        validators=[MinValueValidator(30), MaxValueValidator(45)],
        decimal_places=1,
        max_digits=3,
        help_text='in degrees Celcius')

    heart_rate = models.IntegerField(
        verbose_name='Heart Rate:',
        validators=[MinValueValidator(30), MaxValueValidator(200)],
        help_text='bpm')

    sys_blood_pressure = models.CharField(
        verbose_name='Blood Pressure: systolic',
        validators=[bp_validator],
        max_length=6,
        help_text='in mmHg. format SYS/DIA, e.g. 120/80')

    dia_blood_pressure = models.CharField(
        verbose_name='Blood Pressure: diastolic',
        validators=[bp_validator],
        max_length=6,
        help_text='in mmHg. format SYS/DIA, e.g. 120/80')

    respiratory_rate = models.IntegerField(
        verbose_name='Respiratory Rate:',
        validators=[MinValueValidator(6), MaxValueValidator(50)],
        help_text='breaths/min')

    weight = models.DecimalField(
        verbose_name='Weight:',
        validators=[MinValueValidator(20), MaxValueValidator(150)],
        decimal_places=1,
        max_digits=4,
        help_text='Kg')

    glasgow_coma_score = models.IntegerField(
        verbose_name='Glasgow Coma Score:',
        validators=[MinValueValidator(3), MaxValueValidator(15)],
        help_text='/15')

    neurological = models.ManyToManyField(
        Neurological,
        blank=True)

    neurological_other = OtherCharField(
        verbose_name='If other CN palsy, specify',
        max_length=250,
        blank=True,
        null=True)

    focal_neurologic_deficit = models.TextField(
        verbose_name='If focal neurologic deficit chosen, please '
        'specify details:',
        null=True,
        blank=True)

    visual_acuity_day = models.DateField(
        verbose_name='Study day visual acuity recorded?',
        validators=[date_not_future],
        null=True,
        blank=True)

    left_acuity = models.DecimalField(
        verbose_name='Visual acuity Left eye:',
        decimal_places=3,
        max_digits=4,
        null=True,
        blank=True)

    right_acuity = models.DecimalField(
        verbose_name='Visual Acuity Right eye',
        decimal_places=3,
        max_digits=4,
        null=True,
        blank=True)

    ecog_score = models.CharField(
        verbose_name='ECOG Disability score',
        max_length=15,
        choices=ECOG_SCORE)

    ecog_score_value = models.CharField(
        verbose_name='ECOG Score',
        max_length=15,
        choices=ECOG_SCORE)

    lung_exam = models.CharField(
        verbose_name='Abnormal lung exam:',
        max_length=5,
        choices=YES_NO)

    cryptococcal_lesions = models.CharField(
        verbose_name='Cryptococcal related skin lesions:',
        max_length=5,
        choices=YES_NO)

    specify_medications = models.ManyToManyField(
        Medication,
        blank=True)

    specify_medications_other = models.TextField(
        verbose_name='...if "Other", specify',
        max_length=150,
        blank=True,
        null=True)

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
        decimal_places=2,
        max_digits=4,
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

    location_care_other = OtherCharField(
        verbose_name='If Other Specify:',
        max_length=25,
        blank=True,
        null=True)

    transport_form = models.CharField(
        verbose_name='Which form of transport did you take to reach '
        'there?',
        max_length=5,
        choices=TRANSPORT)

    transport_cost = models.DecimalField(
        verbose_name='How much did you spend on the transport?',
        decimal_places=2,
        max_digits=4,
        null=True,
        blank=True)

    transport_duration = models.CharField(
        verbose_name='How long did it take you to reach there?',
        max_length=25,
        null=True,
        blank=True)

    care_provider = models.CharField(
        verbose_name='Who provided treatment or care for your'
        ' present condition, before coming to the hospital?',
        max_length=35,
        choices=CARE_PROVIDER)

    care_provider_other = OtherCharField(
        verbose_name='If Other Specify:',
        max_length=25,
        blank=True,
        null=True)

    paid_treatment = models.CharField(
        verbose_name='Did you pay for treatment of your present '
        'condition?',
        max_length=5,
        choices=YES_NO)

    paid_treatment_amount = models.DecimalField(
        verbose_name=(
            'How much did you pay for the treatment of your present '
            'condition?'),
        decimal_places=2,
        max_digits=4,
        null=True,
        blank=True)

    medication_bought = models.CharField(
        verbose_name='Did you buy other medication '
        'for the treatment of your present condition?',
        max_length=5,
        choices=YES_NO)

    medication_payment = models.DecimalField(
        verbose_name=(
            'How much did you pay?'),
        decimal_places=2,
        max_digits=4,
        null=True,
        blank=True)

    other_place_visited = models.CharField(
        verbose_name='Before this, did you go to another place '
        'for the treatment of the present situation?',
        max_length=5,
        choices=YES_NO)

    duration_present_condition = models.CharField(
        verbose_name='How long have you been sick with your current '
        'condition?',
        max_length=25,
        blank=True,
        null=True)

    activities_missed = models.CharField(
        verbose_name='What would you have been doing '
        'if you were not sick with your present condition',
        max_length=15,
        choices=ACTIVITIES_MISSED)

    activities_missed_other = OtherCharField(
        verbose_name='If Other, Specify',
        max_length=25,
        blank=True,
        null=True)

    time_off_work = models.CharField(
        verbose_name='How much time did you take off work?',
        max_length=25,
        blank=True,
        null=True)

    carer_time_off = models.CharField(
        verbose_name='How much time did a caring family member take '
        'off work to accompany you to the hospital?',
        max_length=25,
        blank=True,
        null=True)

    loss_of_earnings = models.CharField(
        verbose_name='Did you lose earnings as a result?',
        max_length=5,
        choices=YES_NO,
        blank=True,
        null=True)

    earnings_lost_amount = models.DecimalField(
        verbose_name='How much did you lose?',
        decimal_places=2,
        max_digits=4,
        blank=True,
        null=True)

    household_head = models.CharField(
        verbose_name='Are you head of the household?',
        max_length=5,
        choices=YES_NO)

    profession = models.CharField(
        verbose_name='What is your profession?',
        max_length=25,
        blank=True,
        null=True)

    education_years = models.IntegerField(
        verbose_name='How many years of education did you complete?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    education_certificate = models.CharField(
        verbose_name='What is your highest education certificate?',
        max_length=25,
        blank=True,
        null=True)

    elementary_school = models.CharField(
        verbose_name='Did you go to elementary school?',
        max_length=5,
        choices=YES_NO)

    elementary_attendance_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    secondary_school = models.CharField(
        verbose_name='Did you go to secondary school?',
        max_length=5,
        choices=YES_NO)

    secondary_attendance_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    higher_education = models.CharField(
        verbose_name='Did you go to higher education?',
        max_length=5,
        choices=YES_NO)

    higher_attendance_years = models.IntegerField(
        verbose_name='If YES, for how many years?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    head_profession = models.CharField(
        verbose_name='What is the head of household profession?',
        max_length=25,
        blank=True,
        null=True)

    head_education_years = models.IntegerField(
        verbose_name='How many years of education did '
        'head of houesehold complete?',
        validators=[MinValueValidator(1)],
        blank=True,
        null=True)

    head_education_certificate = models.CharField(
        verbose_name='What is the head of household highest education '
        'certificate?',
        max_length=25,
        blank=True,
        null=True)

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

    class Meta(CrfModelMixin.Meta):
        verbose_name_plural = 'Patients History'
