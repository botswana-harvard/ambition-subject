from django.apps import apps as django_apps
from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from ..managers import CurrentSiteManager
from edc_consent.field_mixins import ReviewFieldsMixin, PersonalFieldsMixin
from edc_consent.field_mixins import SampleCollectionFieldsMixin, CitizenFieldsMixin
from edc_consent.field_mixins import VulnerabilityFieldsMixin
from edc_consent.field_mixins import IdentityFieldsMixin
from edc_consent.managers import ConsentManager
from edc_consent.model_mixins import ConsentModelMixin
from edc_constants.constants import NOT_APPLICABLE, ABNORMAL, NO, YES
from edc_constants.choices import YES_NO
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_search.model_mixins import SearchSlugManager

from .model_mixins import SearchSlugModelMixin
from edc_base.sites.site_model_mixin import SiteModelMixin


class SubjectConsentManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)


class SubjectConsent(
        ConsentModelMixin, SiteModelMixin, UpdatesOrCreatesRegistrationModelMixin,
        NonUniqueSubjectIdentifierModelMixin, IdentityFieldsMixin,
        ReviewFieldsMixin, PersonalFieldsMixin,
        SampleCollectionFieldsMixin, CitizenFieldsMixin,
        VulnerabilityFieldsMixin, SearchSlugModelMixin, BaseUuidModel):

    """ A model completed by the user that captures the ICF.
    """

    subject_screening_model = 'ambition_screening.subjectscreening'

    screening_identifier = models.CharField(
        verbose_name='Screening identifier',
        max_length=50)

    completed_by_next_of_kin = models.CharField(
        max_length=10,
        default=NO,
        choices=YES_NO,
        editable=False)

    on_site = CurrentSiteManager()

    objects = SubjectConsentManager()

    consent = ConsentManager()

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.subject_identifier} V{self.version}'

    def save(self, *args, **kwargs):
        subject_screening = self.get_subject_screening()
        self.completed_by_next_of_kin = (
            YES if subject_screening.mental_status == ABNORMAL else NO)
        self.gender = subject_screening.gender
        self.subject_type = 'subject'
        self.citizen = NOT_APPLICABLE
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.subject_identifier, self.version)

    def get_subject_screening(self):
        """Returns the subject screening model instance.

        Instance must exist since SubjectScreening is completed
        before consent.
        """
        model_cls = django_apps.get_model(self.subject_screening_model)
        return model_cls.objects.get(
            screening_identifier=self.screening_identifier)

    @property
    def registration_unique_field(self):
        """Required for UpdatesOrCreatesRegistrationModelMixin.
        """
        return 'subject_identifier'

    class Meta(ConsentModelMixin.Meta):
        unique_together = (
            ('subject_identifier', 'version'),
            ('subject_identifier', 'screening_identifier'),
            ('first_name', 'dob', 'initials', 'version'))
