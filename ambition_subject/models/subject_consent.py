from django.apps import apps as django_apps
from django.db import models

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_consent.field_mixins.bw import IdentityFieldsMixin
from edc_consent.field_mixins import (
    ReviewFieldsMixin, PersonalFieldsMixin, VulnerabilityFieldsMixin,
    SampleCollectionFieldsMixin, CitizenFieldsMixin)
from edc_consent.managers import ConsentManager
from edc_consent.model_mixins import ConsentModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_registration.model_mixins import UpdatesOrCreatesRegistrationModelMixin
from edc_search.model_mixins import SearchSlugManager

from ambition_screening.models import SubjectScreening

from ..managers import SubjectConsentManager
from .model_mixins import SearchSlugModelMixin


class Manager(SubjectConsentManager, SearchSlugManager):
    pass


class SubjectConsent(
        ConsentModelMixin, UpdatesOrCreatesRegistrationModelMixin,
        NonUniqueSubjectIdentifierModelMixin,
        IdentityFieldsMixin, ReviewFieldsMixin, PersonalFieldsMixin,
        SampleCollectionFieldsMixin, CitizenFieldsMixin,
        VulnerabilityFieldsMixin, SearchSlugModelMixin, BaseUuidModel):
    """ A model completed by the user that captures the ICF.
    """

    subject_screening = models.ForeignKey(
        SubjectScreening, on_delete=models.PROTECT)

    is_signed = models.BooleanField(default=False, editable=False)

    objects = Manager()

    consent = ConsentManager()

    history = HistoricalRecords()

    def __str__(self):
        return f'{self.subject_identifier} V{self.version}'

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
