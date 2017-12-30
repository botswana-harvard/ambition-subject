from django.db import models
from edc_appointment.models import Appointment
from edc_base.model_fields import OtherCharField
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentNonCrfModelMixin
from edc_metadata.model_mixins.creates import CreatesMetadataModelMixin
from edc_reference.model_mixins import ReferenceModelMixin
from edc_visit_tracking.managers import VisitModelManager
from edc_visit_tracking.model_mixins import VisitModelMixin

from ..choices import INFO_SOURCE, VISIT_UNSCHEDULED_REASON, VISIT_REASON


class SubjectVisit(VisitModelMixin, ReferenceModelMixin, CreatesMetadataModelMixin,
                   RequiresConsentNonCrfModelMixin, BaseUuidModel):

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
        choices=VISIT_UNSCHEDULED_REASON)

    reason_unscheduled_other = OtherCharField(
        max_length=25,
        blank=True,
        null=True)

    info_source = models.CharField(
        verbose_name='What is the main source of this information?',
        max_length=25,
        choices=INFO_SOURCE)

    objects = VisitModelManager()

    history = HistoricalRecords()

    class Meta(VisitModelMixin.Meta):
        pass
