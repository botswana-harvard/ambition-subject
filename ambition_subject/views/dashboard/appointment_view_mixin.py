from edc_appointment.models import Appointment
from edc_dashboard.view_mixins.subject_dashboard import (
    AppointmentViewMixin as BaseAppointmentMixin)

from ..wrappers import AppointmentModelWrapper


class AppointmentViewMixin(BaseAppointmentMixin):

    appointment_model_wrapper_cls = AppointmentModelWrapper

    def empty_appointment(self, **kwargs):
        return Appointment()
