from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_constants.choices import GENDER, YES_NO, YES_NO_NA

from ..choices import RANDOMISATION_NUMBER, REGIMEN


class ScreeningRandomization(BaseUuidModel):

##Could be obtained from Consent Data
    sex = models.CharField(
        choices=GENDER,
        max_length=10)

##Could be obtained from Consent Data
    age = models.IntegerField()

    is_of_age = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Age ≥18 years')

    meningitis_diagoses_by_csf_or_crag = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='First episode cryptococcal meningitis diag- nosed by '
                     'either: CSF India Ink or CSF cryptococcal antigen '
                     '(CRAG)')

    consent_to_hiv_test = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Willing to consent to HIV test')

    willing_to_give_informed_consent = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Participant or legal guardian/representative able and '
                     'willing to give informed consent.')

    pregrancy_or_lactation = models.CharField(
        choices=YES_NO_NA,
        max_length=15,
        verbose_name='Pregnancy or lactation (Urine βhCG)')

    previous_adverse_drug_reaction = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Previous Adverse Drug Reaction (ADR) to study drug '
                     '(e.g. rash, drug induced blood abnormality)')

    medication_contraindicated_with_study_drug = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Taking concomitant medication that is contra-indicated '
                     'with any study drug')

    two_days_amphotericin_b = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Has received >48 hours of Amphotericin B (AmB) therapy '
                     'prior to screening.')

    two_days_fluconazole = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Has received >48 hours of fluconazole treatment (> '
                     '400mg daily dose) prior to screening.')

    patient_eligible = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Is the patient eligible for the study?')

    consent_given = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='If yes, has consent been given?')

    hospital_admission_date = models.DateField(
        validators=[date_not_future],
        verbose_name='Date of hospital admission')

    inclusion_date = models.DateField(
        validators=[date_not_future],
        verbose_name='Date of inclusion')

    abnormal_mental_status = models.CharField(
        choices=YES_NO,
        max_length=5,
        help_text='Abnormal mental status is GCS<15')

    already_on_arvs = models.CharField(
        choices=YES_NO,
        max_length=5)

    arv_start_date = models.DateField(
        blank=True,
        null=True,
        validators=[date_not_future],
        verbose_name='If yes, ARV start date:')

    randomization_number = models.CharField(
        choices=RANDOMISATION_NUMBER,
        max_length=10)

    consent_form_signed = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='Consent form signed and copy given to participant')

    regimen = models.CharField(
        choices=REGIMEN,
        max_length=15)

    history = HistoricalRecords()

    class Meta:
        app_label = 'ambition_subject'
        verbose_name = 'Screening and randomization'
