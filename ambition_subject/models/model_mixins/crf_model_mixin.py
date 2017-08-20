from django.db import models
from django.db.models.deletion import PROTECT

from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel, FormAsJSONModelMixin
from edc_base.model_validators import datetime_not_future
from edc_base.utils import get_utcnow
from edc_consent.model_mixins import RequiresConsentMixin
from edc_metadata.model_mixins.updates import UpdatesCrfMetadataModelMixin
from edc_offstudy.model_mixins import OffstudyMixin
from edc_protocol.validators import datetime_not_before_study_start
from edc_reference.model_mixins import ReferenceModelMixin
from edc_visit_tracking.managers import CrfModelManager as VisitTrackingCrfModelManager
from edc_visit_tracking.model_mixins import (
    CrfModelMixin as VisitTrackingCrfModelMixin, PreviousVisitModelMixin)
from edc_metadata.rules.site import site_metadata_rules
from edc_metadata.model_mixins.rules.metadata_rules_model_mixin import MetadataRulesModelMixin

from ..subject_visit import SubjectVisit


class CrfModelManager(VisitTrackingCrfModelManager):

    def get_by_natural_key(self, subject_identifier, visit_schedule_name,
                           schedule_name, visit_code):
        return self.get(
            subject_visit__subject_identifier=subject_identifier,
            subject_visit__visit_schedule_name=visit_schedule_name,
            subject_visit__schedule_name=schedule_name,
            subject_visit__visit_code=visit_code
        )


class CrfModelMixin(VisitTrackingCrfModelMixin, OffstudyMixin,
                    RequiresConsentMixin, PreviousVisitModelMixin,
                    UpdatesCrfMetadataModelMixin, MetadataRulesModelMixin,
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

    def run_metadata_rules(self):
        """Runs the rule groups for this .
        Gets called in the signal.
        """
        for rule_group in site_metadata_rules.registry.get(self._meta.rulegroup_app_label, []):
            if rule_group._meta.source_model == self._meta.label_lower:
                rule_group.evaluate_rules(visit=self)

    def natural_key(self):
        return self.subject_visit.natural_key()
    natural_key.dependencies = ['ambition_subject.subjectvisit']

    class Meta(VisitTrackingCrfModelMixin.Meta, RequiresConsentMixin.Meta):
        consent_model = 'ambition_subject.subjectconsent'
        rulegroup_app_label = 'ambition_metadata_rules'
        abstract = True
