from django.contrib import admin

from edc_appointment.admin import AppointmentAdmin as BaseAppointmentAdmin
from edc_appointment.models import Appointment

from ..admin_site import ambition_subject_admin
from ..forms import AppointmentForm


@admin.register(Appointment, site=ambition_subject_admin)
class AppointmentAdmin(BaseAppointmentAdmin):

    form = AppointmentForm
