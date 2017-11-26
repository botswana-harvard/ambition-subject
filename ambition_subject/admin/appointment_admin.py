from django.conf import settings
from django.contrib.admin.sites import NotRegistered
from edc_appointment.admin import AppointmentAdmin as BaseAppointmentAdmin
from edc_appointment.admin_site import edc_appointment_admin
from edc_appointment.models import Appointment


class AppointmentAdmin(BaseAppointmentAdmin):

    post_url_on_delete_name = settings.DASHBOARD_URL_NAMES.get(
        'subject_dashboard_url')


try:
    edc_appointment_admin.unregister(Appointment)
except NotRegistered:
    pass
edc_appointment_admin.register(Appointment, AppointmentAdmin)
