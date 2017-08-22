from django.db import models
from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentMixin
from edc_metadata.model_mixins.creates import CreatesMetadataModelMixin
from edc_metadata_rules.model_mixins import MetadataRulesModelMixin
from edc_reference.model_mixins import ReferenceModelMixin
from edc_visit_tracking.managers import VisitModelManager
from edc_visit_tracking.model_mixins import VisitModelMixin, PreviousVisitError

from ..choices import VISIT_UNSCHEDULED_REASON, VISIT_REASON
from .appointment import Appointment


class SubjectVisit(VisitModelMixin, ReferenceModelMixin, CreatesMetadataModelMixin,
                   MetadataRulesModelMixin, RequiresConsentMixin, BaseUuidModel):

    """A model completed by the user that captures the covering
    information for the data collected for this timepoint/appointment,
    e.g.report_datetime.
    """

    appointment = models.OneToOneField(Appointment, on_delete=models.PROTECT)

    reason = models.CharField(
        verbose_name='What is the reason for this visit?',
        max_length=25,
        choices=VISIT_REASON)

    reason_unscheduled = models.CharField(
        verbose_name=(
            'If \'Unscheduled\' above, provide reason for '
            'the unscheduled visit'),
        max_length=25,
        blank=True,
        null=True,
        choices=VISIT_UNSCHEDULED_REASON,
    )

    reason_unscheduled_other = OtherCharField(
        verbose_name='If Other, Specify',
        max_length=25,
        blank=True,
        null=True,
    )

    objects = VisitModelManager()

    history = HistoricalRecords()

#     def run_metadata_rules(self):
#         """Runs the rule groups for this .
#         Gets called in the signal.
#         """
#         for rule_group in site_metadata_rules.registry.get(self._meta.app_label, []):
#             if rule_group._meta.source_model == self._meta.label_lower:
#                 rule_group.evaluate_rules(visit=self)

    def save(self, *args, **kwargs):
        self.info_source = 'subject'
        super().save(*args, **kwargs)

    @property
    def common_clean_exceptions(self):
        return super().common_clean_exceptions + [PreviousVisitError]

    class Meta(VisitModelMixin.Meta, RequiresConsentMixin.Meta):
        consent_model = 'ambition_subject.subjectconsent'
        # rulegroup_app_label = 'ambition_metadata_rules'
