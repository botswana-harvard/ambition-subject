from django import forms

from edc_appointment.modelform_mixins import AppointmentFormMixin

from ..models import Appointment
from ..choices import APPOINTMENT_REASON, AMB_APPT_TYPE


class AppointmentForm(AppointmentFormMixin, forms.ModelForm):

    appt_reason = forms.ChoiceField(
        label='Reason for appointment:',
        choices=APPOINTMENT_REASON,
        widget=forms.RadioSelect)

    class Meta:
        model = Appointment
        fields = '__all__'
