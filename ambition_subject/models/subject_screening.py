import re

from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.utils import get_utcnow
from edc_constants.choices import GENDER, YES_NO, YES_NO_NA, NO, YES, NORMAL_ABNORMAL
from edc_constants.constants import UUID_PATTERN
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_search.model_mixins import SearchSlugManager, SearchSlugModelMixin
from uuid import uuid4

from ..eligibility import Eligibility
from ..screening_identifier import ScreeningIdentifier
from ..choices import PREG_YES_NO_NA, WITHDRAWAL_CRITERIA_YES_NO_UNKNOWN


class SubjectScreeningManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, screening_identifier):
        return self.get(screening_identifier=screening_identifier)


class SubjectIdentifierModelMixin(NonUniqueSubjectIdentifierModelMixin,
                                  SearchSlugModelMixin, models.Model):

    def update_subject_identifier_on_save(self):
        """Overridden to not set the subject identifier on save.
        """
        if not self.subject_identifier:
            self.subject_identifier = self.subject_identifier_as_pk.hex
        elif re.match(UUID_PATTERN, self.subject_identifier):
            pass
        return self.subject_identifier

    def make_new_identifier(self):
        return self.subject_identifier_as_pk.hex

    class Meta:
        abstract = True


class SubjectScreening(SubjectIdentifierModelMixin, BaseUuidModel):

    reference = models.UUIDField(
        verbose_name="Reference",
        unique=True,
        default=uuid4,
        editable=False)

    screening_identifier = models.CharField(
        verbose_name='Screening Id',
        max_length=50,
        blank=True,
        unique=True,
        editable=False)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date and Time",
        default=get_utcnow,
        help_text='Date and time of report.')

    gender = models.CharField(
        choices=GENDER,
        max_length=10)

    age_in_years = models.IntegerField()

    meningitis_dx = models.CharField(
        verbose_name='First episode cryptococcal meningitis diagnosed by '
                     'either: CSF India Ink or CSF cryptococcal antigen '
                     '(CRAG)',
        choices=YES_NO,
        max_length=5)

    will_hiv_test = models.CharField(
        verbose_name='Known HIV positive/willing to consent to an HIV test.',
        max_length=5,
        choices=YES_NO)

    mental_status = models.CharField(
        verbose_name='Mental Status',
        max_length=10,
        choices=NORMAL_ABNORMAL)

    consent_ability = models.CharField(
        verbose_name='Participant or legal guardian/representative able and '
                     'willing to give informed consent.',
        max_length=5,
        choices=YES_NO)

    pregnancy = models.CharField(
        verbose_name='Is the patient pregnant?',
        max_length=15,
        choices=PREG_YES_NO_NA)

    preg_test_date = models.DateTimeField(
        verbose_name="Pregnancy test (Urine or serum βhCG) date",
        blank=True,
        null=True)

    breast_feeding = models.CharField(
        verbose_name='Is the patient breasfeeding?',
        max_length=15,
        choices=YES_NO_NA)

    previous_drug_reaction = models.CharField(
        verbose_name='Previous Adverse Drug Reaction (ADR) to study drug '
                     '(e.g. rash, drug induced blood abnormality)',
        max_length=5,
        choices=YES_NO)

    contraindicated_meds = models.CharField(
        verbose_name='Taking concomitant medication that is contra-indicated '
                     'with any study drug',
        max_length=5,
        choices=YES_NO,
        help_text='Contraindicated Meds: Cisapride, Pimozide,'
        'Terfenadine, Quinidine, Astemizole, Erythromycin')

    received_amphotericin = models.CharField(
        verbose_name='Has received >48 hours of Amphotericin B '
        '(>0.7mg/kg/day) prior to screening.',
        max_length=5,
        choices=YES_NO,

    )

    received_fluconazole = models.CharField(
        verbose_name='Has received >48 hours of fluconazole treatment (> '
                     '400mg/day) prior to screening.',
        max_length=5,
        choices=YES_NO,
    )

    eligible = models.BooleanField(
        default=False,
        editable=False)

    reasons_ineligible = models.TextField(
        verbose_name="Reason not eligible",
        max_length=150,
        null=True,
        editable=False)

    withdrawal_criteria = models.CharField(
        verbose_name='Does the patient meet an early withdrawal criteria?',
        max_length=150,
        choices=WITHDRAWAL_CRITERIA_YES_NO_UNKNOWN,
        help_text='ALT>200 IU/mL, PMNs<500x106/L, Platelets<50,000x106/L'
    )

    objects = SubjectScreeningManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.screening_identifier,)

    def save(self, *args, **kwargs):
        self.verify_eligibility()
        if not self.id:
            self.screening_identifier = ScreeningIdentifier().identifier
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.screening_identifier} {self.gender} {self.age_in_years}'

    def get_search_slug_fields(self):
        return ['screening_identifier', 'subject_identifier', 'reference']

    def verify_eligibility(self):
        """Verifies eligibility criteria and sets model attrs.
        """
        def if_yes(value):
            return value == YES

        def if_no(value):
            return value == NO

        eligibility = Eligibility(
            age=self.age_in_years,
            gender=self.gender,
            will_hiv_test=if_yes(self.will_hiv_test),
            consent_ability=if_yes(self.consent_ability),
            mental_status=self.mental_status,
            meningitis_dx=if_yes(self.meningitis_dx),
            pregnant=if_yes(self.pregnancy),
            breast_feeding=if_yes(self.breast_feeding),
            no_drug_reaction=if_no(self.previous_drug_reaction),
            no_concomitant_meds=if_no(self.contraindicated_meds),
            no_amphotericin=if_no(self.received_amphotericin),
            no_fluconazole=if_no(self.received_fluconazole),
            withdrawal_criteria=if_yes(self.withdrawal_criteria))
        self.reasons_ineligible = ','.join(eligibility.reasons)
        self.eligible = eligibility.eligible
