from django import forms
from edc_appointment.modelform_mixins import AppointmentFormMixin
from edc_appointment.models import Appointment

from ..choices import APPOINTMENT_REASON


class AppointmentForm(AppointmentFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.status_field is not None:
            self.fields['appt_reason'].choices = APPOINTMENT_REASON
            self.fields['appt_reason'].widget.choices = APPOINTMENT_REASON

    # FIXME: This should NOT be overriden!
    def validate_appt_new_or_complete(self, appt_status=None):
        return None

    class Meta:
        model = Appointment
        fields = '__all__'
