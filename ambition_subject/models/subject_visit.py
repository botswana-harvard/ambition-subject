from django.db import models
from edc_appointment.models import Appointment
from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentMixin
from edc_metadata.model_mixins.creates import CreatesMetadataModelMixin
from edc_reference.model_mixins import ReferenceModelMixin
from edc_visit_tracking.managers import VisitModelManager
from edc_visit_tracking.model_mixins import VisitModelMixin, PreviousVisitError

from ..choices import INFO_SOURCE, VISIT_UNSCHEDULED_REASON, VISIT_REASON


class SubjectVisit(VisitModelMixin, ReferenceModelMixin, CreatesMetadataModelMixin,
                   RequiresConsentMixin, BaseUuidModel):

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

    info_source = models.CharField(
        verbose_name='What is the main source of this information?',
        max_length=25,
        choices=INFO_SOURCE)

    objects = VisitModelManager()

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.info_source = 'subject'
        super().save(*args, **kwargs)

    @property
    def common_clean_exceptions(self):
        return super().common_clean_exceptions + [PreviousVisitError]

    class Meta(VisitModelMixin.Meta, RequiresConsentMixin.Meta):
        consent_model = 'ambition_subject.subjectconsent'
