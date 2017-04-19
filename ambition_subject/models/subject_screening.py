from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.utils import get_utcnow
from edc_consent.site_consents import site_consents
from edc_constants.choices import GENDER, YES_NO, YES_NO_NA, NO, YES, FEMALE


class SubjectScreening(BaseUuidModel):

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text='Date and time of report.')

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

    pregnancy_or_lactation = models.CharField(
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
        error_message = []
        # consent_config = site_consents.get_consent(
        #    consent_model='ambition_subject.subjectconsent')
        if (self.age < 18 and
           self.willing_to_give_informed_consent == NO):
            error_message.append(
                'Participant is under 18')

        if self.sex == FEMALE and self.pregnancy_or_lactation == YES:
            error_message.append('Participant is pregnant')

        if self.previous_adverse_drug_reaction == YES:
            error_message.append('Previous adverse drug reaction reported')

        if self.medication_contraindicated_with_study_drug == YES:
            error_message.append(
                'Participant taking concomitant medication that is contra-'
                'indicated with any study drug')

        if self.two_days_amphotericin_b == YES:
            error_message.append('Has received >48 hours of Amphotericin B')

        if self.two_days_fluconazole == YES:
            error_message.append(
                'Has received >48 hours of fluconazole '
                'treatment (> 400mg daily dose) prior to screening.')
        is_eligible = False if error_message else True
        return (is_eligible, ','.join(error_message))

    class Meta:
        app_label = 'ambition_subject'
        verbose_name = 'Subject Screening'
