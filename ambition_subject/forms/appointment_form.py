from django import forms

from edc_appointment.modelform_mixins import AppointmentFormMixin
from edc_appointment.models import Appointment

from ..choices import APPOINTMENT_REASON, AMB_APPT_TYPE


class AppointmentForm(AppointmentFormMixin, forms.ModelForm):

    appt_type = forms.ChoiceField(
        label='Appointment type:',
        choices=AMB_APPT_TYPE,
        widget=forms.RadioSelect)

    appt_reason = forms.ChoiceField(
        label='Reason for appointment:',
        choices=APPOINTMENT_REASON,
        widget=forms.RadioSelect)

    def validate_appt_new_or_complete(self, appt_status=None):
        return None

    class Meta:
        model = Appointment
        fields = '__all__'
