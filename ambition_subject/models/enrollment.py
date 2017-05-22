from django.db import models
from django.utils import timezone

from edc_appointment.model_mixins import CreateAppointmentsMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_visit_schedule.model_mixins import EnrollmentModelMixin

from ..managers import EnrollmentManager as BaseEnrollmentManager


class EnrollmentManager(BaseEnrollmentManager):

    def get_enrollment_model_class(self, survey_object):
        """Returns the proxy model class for the given survey name.
        """
        return Enrollment


class EnrollmentProxyModelManager(BaseEnrollmentManager):

    def get_queryset(self):
        qs = super().get_queryset()
        visit_schedule_name = qs.model._meta.visit_schedule_name.split('.')[0]
        schedule_name = qs.model._meta.visit_schedule_name.split('.')[1]
        return qs.filter(
            visit_schedule_name=visit_schedule_name,
            schedule_name=schedule_name,
        )


class Enrollment(EnrollmentModelMixin, CreateAppointmentsMixin, BaseUuidModel):

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

    def save(self, *args, **kwargs):
        self.facility_name = 'clinic'
        super().save(*args, **kwargs)

    class Meta(EnrollmentModelMixin.Meta):
        app_label = 'ambition_subject'
        consent_model = 'ambition_subject.subjectconsent'
        verbose_name = 'Enrollment'
        visit_schedule_name = 'visit_schedule1.schedule1'
