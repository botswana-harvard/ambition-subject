from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel, FormAsJSONModelMixin
from edc_base.model_validators import datetime_not_future
from edc_base.utils import get_utcnow
from edc_consent.model_mixins import RequiresConsentMixin
from edc_metadata.model_mixins.updates import UpdatesCrfMetadataModelMixin
from edc_protocol.validators import datetime_not_before_study_start
from edc_reference.model_mixins import ReferenceModelMixin
from edc_visit_tracking.managers import CrfModelManager as VisitTrackingCrfModelManager
from edc_visit_tracking.model_mixins import CrfModelMixin as BaseCrfModelMixin
from edc_visit_tracking.model_mixins import PreviousVisitModelMixin

from ..subject_visit import SubjectVisit
from .off_study_model_mixin import OffstudyModelMixin


class CrfModelManager(VisitTrackingCrfModelManager):

    def get_by_natural_key(self, subject_identifier, visit_schedule_name,
                           schedule_name, visit_code):
        return self.get(
            subject_visit__subject_identifier=subject_identifier,
            subject_visit__visit_schedule_name=visit_schedule_name,
            subject_visit__schedule_name=schedule_name,
            subject_visit__visit_code=visit_code
        )


class CrfModelMixin(BaseCrfModelMixin, OffstudyModelMixin,
                    RequiresConsentMixin, PreviousVisitModelMixin,
                    UpdatesCrfMetadataModelMixin,
                    FormAsJSONModelMixin, ReferenceModelMixin, BaseUuidModel):

    """ Base model for all scheduled models (adds key to :class:`SubjectVisit`).
    """

    subject_visit = models.OneToOneField(SubjectVisit, on_delete=PROTECT)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_future, datetime_not_before_study_start],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    objects = CrfModelManager()

    history = HistoricalRecords()

    def natural_key(self):
        return self.subject_visit.natural_key()
    natural_key.dependencies = ['ambition_subject.subjectvisit']

    class Meta(BaseCrfModelMixin.Meta, RequiresConsentMixin.Meta):
        consent_model = 'ambition_subject.subjectconsent'
        abstract = True
