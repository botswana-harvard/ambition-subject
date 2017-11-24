from django.db import models
from django.utils import timezone
from edc_appointment.model_mixins import CreateAppointmentsMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_visit_schedule.model_mixins import EnrollmentModelMixin


class EnrollmentManager(models.Manager):

    def get_by_natural_key(self, subject_identifier,
                           visit_schedule_name, schedule_name):
        return self.get(
            subject_identifier=subject_identifier,
            visit_schedule_name=visit_schedule_name,
            schedule_name=schedule_name)


class Enrollment(EnrollmentModelMixin, CreateAppointmentsMixin,
                 BaseUuidModel):

    """A model used by the system. Auto-completed by subject_consent.
    """

    ADMIN_SITE_NAME = 'ambition_subject_admin'

    subject_identifier = models.CharField(
        verbose_name="Subject Identifier",
        max_length=50)

    consent_identifier = models.UUIDField()

    report_datetime = models.DateTimeField(
        default=timezone.now,
        editable=False)

    objects = EnrollmentManager()

    history = HistoricalRecords()

    class Meta(EnrollmentModelMixin.Meta):
        consent_model = 'ambition_subject.subjectconsent'
        visit_schedule_name = 'visit_schedule.schedule'
