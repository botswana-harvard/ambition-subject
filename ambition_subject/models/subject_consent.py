from django.apps import apps as django_apps
from django.db import models

from edc_base.model_mixins import BaseUuidModel
from edc_base.model_managers import HistoricalRecords
from edc_consent.field_mixins.bw import IdentityFieldsMixin
from edc_consent.field_mixins import (
    ReviewFieldsMixin, PersonalFieldsMixin, VulnerabilityFieldsMixin,
    SampleCollectionFieldsMixin, CitizenFieldsMixin)
from edc_consent.managers import ConsentManager
from edc_consent.model_mixins import ConsentModelMixin
from edc_dashboard.model_mixins import SearchSlugManager
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_registration.exceptions import RegisteredSubjectError
from edc_registration.model_mixins import (
    UpdatesOrCreatesRegistrationModelMixin
    as BaseUpdatesOrCreatesRegistrationModelMixin)

from ..managers import SubjectConsentManager
from .model_mixins import SearchSlugModelMixin


class Manager(SubjectConsentManager, SearchSlugManager):
    pass


class UpdatesOrCreatesRegistrationModelMixin(BaseUpdatesOrCreatesRegistrationModelMixin):

    @property
    def registration_options(self):
        """Insert internal_identifier to be updated on
        RegisteredSubject.
        """
        registration_options = super().registration_options
        registration_options.update(
            registration_identifier=self.household_member.internal_identifier)
        return registration_options

    def registration_raise_on_illegal_value_change(self, registered_subject):
        """Raises an exception if a value changes between
        updates.
        """
        if registered_subject.identity != self.identity:
            raise RegisteredSubjectError(
                'Identity may not be changed. Expected {}. Got {}'.format(
                    registered_subject.identity,
                    self.identity))
        if (registered_subject.registration_identifier
            and registered_subject.registration_identifier !=
                self.household_member.internal_identifier):
            raise RegisteredSubjectError(
                'Internal Identifier may not be changed. Expected {}. '
                'Got {}'.format(
                    registered_subject.registration_identifier,
                    self.household_member.internal_identifier))
        if registered_subject.dob != self.dob:
            raise RegisteredSubjectError(
                'DoB may not be changed. Expected {}. Got {}'.format(
                    registered_subject.dob,
                    self.dob))

    class Meta:
        abstract = True


class SubjectConsent(
        ConsentModelMixin, UpdatesOrCreatesRegistrationModelMixin,
        NonUniqueSubjectIdentifierModelMixin,
        IdentityFieldsMixin, ReviewFieldsMixin, PersonalFieldsMixin,
        SampleCollectionFieldsMixin, CitizenFieldsMixin,
        VulnerabilityFieldsMixin, SearchSlugModelMixin, BaseUuidModel):
    """ A model completed by the user that captures the ICF.
    """

    is_signed = models.BooleanField(default=False, editable=False)

    objects = Manager()

    consent = ConsentManager()

    history = HistoricalRecords()

    def __str__(self):
        return '{0} ({1}) V{2}'.format(
            self.subject_identifier,
            self.survey_schedule_object.name,
            self.version)

    def save(self, *args, **kwargs):
        if not self.id:
            edc_protocol_app_config = django_apps.get_app_config(
                'edc_protocol')
            self.study_site = edc_protocol_app_config.site_code
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.subject_identifier, self.version, )

    class Meta(ConsentModelMixin.Meta):
        app_label = 'ambition_subject'
        get_latest_by = 'consent_datetime'
        unique_together = (('subject_identifier', 'version'),
                           ('first_name', 'dob', 'initials', 'version'))
        ordering = ('-created', )
