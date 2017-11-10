from ambition_subject.choices import AMB_APPT_TYPE, APPOINTMENT_REASON
from django.db import models
from edc_appointment.managers import AppointmentManager
from edc_appointment.model_mixins import AppointmentModelMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_visit_schedule.site_visit_schedules import site_visit_schedules


class Appointment(AppointmentModelMixin, BaseUuidModel):

    appt_type = models.CharField(
        verbose_name='Appointment type',
        choices=AMB_APPT_TYPE,
        default='clinic',
        max_length=20,
        help_text=(
            'Default for subject may be edited Subject Configuration.'))

    appt_reason = models.CharField(
        verbose_name='Reason for appointment:',
        max_length=25,
        choices=APPOINTMENT_REASON,
        default='routine')

    objects = AppointmentManager()

    history = HistoricalRecords()

    @property
    def title(self):
        schedule = site_visit_schedules.get_schedule(
            schedule_name=self.schedule_name)
        if self.visit_code_sequence > 0:
            return schedule.visits.get(self.visit_code).title + ' Unscheduled'
        else:
            return schedule.visits.get(self.visit_code).title
