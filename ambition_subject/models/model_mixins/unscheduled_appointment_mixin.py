from decimal import Decimal

from ambition_visit_schedule.visit_schedules.schedule import visit_unscheduled
from edc_appointment.model_mixins import CreateAppointmentsMixin
from edc_base.utils import get_utcnow
from edc_visit_schedule import site_visit_schedules


class WrongAppointmentError(Exception):
    pass


class UnscheduledAppointment(CreateAppointmentsMixin):

    def __init__(self, appointment):
        appointment = appointment
        self.validate_timepoint(appointment)
        self.subject_identifier = appointment.subject_identifier
        self.visit_schedule = site_visit_schedules.get_visit_schedule(
            appointment.visit_schedule_name)
        self.schedule = site_visit_schedules.get_schedule(
            schedule_name=appointment.schedule_name)
        self.facility_name = appointment.facility_name

        self.visit_code_sequence = self.current_visit_code_sequence(
            appointment.visit_code) + 1

        self.visit_code = (appointment.visit_code + '.' +
                           str(self.visit_code_sequence))

        visit_unscheduled.code = self.visit_code
        visit_unscheduled.timepoint = round(
            appointment.timepoint + Decimal(self.visit_code_sequence / 10), 1)

        self.schedule.add_visit(visit=visit_unscheduled)

        self.update_or_create_appointment(
            visit=visit_unscheduled, available_datetime=get_utcnow(),
            timepoint_datetime=get_utcnow())

    @property
    def extra_create_appointment_options(self):
        return dict(
            subject_identifier=self.subject_identifier,
            visit_code=self.visit_code,
            visit_code_sequence=self.visit_code_sequence + 1,
            facility_name=self.facility_name)

    def current_visit_code_sequence(self, visit_code):
        visit_code_sequence = 0
        appointments = self.appointment_model.objects.filter(
            visit_code__contains=visit_code).order_by('-visit_code_sequence')

        if appointments:
            visit_code_sequence = appointments[0].visit_code_sequence
        return visit_code_sequence

    def validate_timepoint(self, appointment):
        if appointment.timepoint < 6:
            raise WrongAppointmentError(
                f'Unscheduled appointment cannot be added at '
                f'{appointment.visit_code}, unscheduled appointment can '
                f'only be added at or after appointment 1014')
