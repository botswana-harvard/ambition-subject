from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_constants.choices import GENDER, YES_NO, YES_NO_NA


class SubjectScreening(BaseUuidModel):

    sex = models.CharField(
        choices=GENDER,
        max_length=10)

    age = models.IntegerField()

    meningitis_diagoses_by_csf_or_crag = models.CharField(
        choices=YES_NO,
        max_length=5,
        verbose_name='First episode cryptococcal meningitis diagnosed by '
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

    is_eligible = models.BooleanField(
        default=False,
        editable=False)

    ineligibility = models.TextField(
        verbose_name="Reason not eligible",
        max_length=150,
        null=True,
        editable=False)

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.is_eligible, self.ineligibility = self.get_is_eligible()
        super().save(*args, **kwargs)

    def get_is_eligible(self):
        raise TypeError('Eligibility criteria not evaluated')

    class Meta:
        app_label = 'ambition_subject'
        verbose_name = 'Subject Screening'
