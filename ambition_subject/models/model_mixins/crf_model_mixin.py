from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel, FormAsJSONModelMixin
from edc_consent.model_mixins import RequiresConsentMixin
from edc_metadata.model_mixins.updates import UpdatesCrfMetadataModelMixin
from edc_offstudy.model_mixins import OffstudyCrfModelMixin
from edc_reference.model_mixins import ReferenceModelMixin
from edc_visit_tracking.managers import CrfModelManager  # as BaseCrfModelManager
from edc_visit_tracking.model_mixins import CrfModelMixin as BaseCrfModelMixin
from edc_visit_tracking.model_mixins import PreviousVisitModelMixin

from ..subject_visit import SubjectVisit


class CrfModelMixin(BaseCrfModelMixin, OffstudyCrfModelMixin,
                    RequiresConsentMixin, PreviousVisitModelMixin,
                    UpdatesCrfMetadataModelMixin,
                    FormAsJSONModelMixin, ReferenceModelMixin, BaseUuidModel):

    """ Base model for all scheduled models
    """

    subject_visit = models.OneToOneField(SubjectVisit, on_delete=PROTECT)

    objects = CrfModelManager()

    history = HistoricalRecords()

    def natural_key(self):
        return self.subject_visit.natural_key()
    natural_key.dependencies = ['ambition_subject.subjectvisit']

    class Meta(BaseCrfModelMixin.Meta, RequiresConsentMixin.Meta):
        consent_model = 'ambition_subject.subjectconsent'
        abstract = True
