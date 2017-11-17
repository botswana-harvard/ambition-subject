import re

from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.utils import get_utcnow
from edc_constants.choices import GENDER, YES_NO, YES_NO_NA, NORMAL_ABNORMAL
from edc_constants.constants import UUID_PATTERN
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_search.model_mixins import SearchSlugManager, SearchSlugModelMixin
from uuid import uuid4

from ..choices import PREG_YES_NO_NA
from ..eligibility import SubjectScreeningEligibility
from ..screening_identifier import ScreeningIdentifier


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

    eligibility_cls = SubjectScreeningEligibility

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
        choices=YES_NO)

    received_fluconazole = models.CharField(
        verbose_name=(
            'Has received >48 hours of fluconazole treatment (> '
            '400mg/day) prior to screening.'),
        max_length=5,
        choices=YES_NO)

    alt_result = models.IntegerField(
        verbose_name='ALT result?',
        null=True,
        blank=True,
        help_text=('Leave blank if unknown. Units: "IU/mL". '
                   'Ineligible if > 200 IU/mL'))

    pmn_result = models.IntegerField(
        verbose_name='PMNs result?',
        null=True,
        blank=True,
        help_text=('Leave blank if unknown. Units: " x 10e6/L". '
                   'Ineligible if < 500 x 10e6/L'))

    platelets_result = models.IntegerField(
        null=True,
        blank=True,
        help_text=('Leave blank if unknown. Units: " x 10e9/L". '
                   'Ineligible if < 50 x 10e9/L'))

    eligible = models.BooleanField(
        default=False,
        editable=False)

    reasons_ineligible = models.TextField(
        verbose_name="Reason not eligible",
        max_length=150,
        null=True,
        editable=False)

    objects = SubjectScreeningManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (self.screening_identifier,)

    def save(self, *args, **kwargs):
        eligibility_obj = self.eligibility_cls(model_obj=self, allow_none=True)
        self.eligible = eligibility_obj.eligible
        if not self.eligible:
            reasons_ineligible = [
                v for v in eligibility_obj.reasons_ineligible.values() if v]
            reasons_ineligible.sort()
            self.reasons_ineligible = ','.join(reasons_ineligible)
        else:
            self.reasons_ineligible = None
        if not self.id:
            self.screening_identifier = ScreeningIdentifier().identifier
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.screening_identifier} {self.gender} {self.age_in_years}'

    def get_search_slug_fields(self):
        return ['screening_identifier', 'subject_identifier', 'reference']
