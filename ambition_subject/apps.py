from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
from django.apps import AppConfig as DjangoApponfig

from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_appointment.facility import Facility
from edc_base.address import Address
from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_base.utils import get_utcnow
from edc_constants.constants import FAILED_ELIGIBILITY
from edc_device.apps import AppConfig as BaseEdcDeviceAppConfig
from edc_device.constants import CENTRAL_SERVER
from edc_lab.apps import AppConfig as BaseEdcLabAppConfig
from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
from edc_timepoint.apps import AppConfig as BaseEdcTimepointAppConfig
from edc_timepoint.timepoint import Timepoint
from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT


class AppConfig(DjangoApponfig):
    name = 'ambition_subject'
    listboard_template_name = 'ambition_subject/listboard.html'
    dashboard_template_name = 'ambition_subject/dashboard.html'
    base_template_name = 'edc_base/base.html'
    listboard_url_name = 'ambition_subject:listboard_url'
    dashboard_url_name = 'ambition_subject:dashboard_url'
    admin_site_name = 'ambition_subject_admin'

    def ready(self):
        pass


class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
    app_label = 'ambition_subject'
    default_appt_type = 'clinic'
    facilities = {
        'clinic': Facility(
            name='clinic', days=[MO, TU, WE, TH, FR, SA, SU],
            slots=[99999, 99999, 99999, 99999, 99999, 99999, 99999])}


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'AMBITION'
    institution = 'Botswana-Harvard AIDS Institute Partnership'
    copyright = '2017-{}'.format(get_utcnow().year)
    license = 'GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007'
    physical_address = Address(
        company_name='Botswana-Harvard AIDS Institute Partnership',
        address='Plot 1836',
        city='Gaborone',
        country='Botswana',
        tel='+267 3902671',
        fax='+267 3901284')
    postal_address = Address(
        company_name='Botswana-Harvard AIDS Institute Partnership',
        address='Private Bag BO 320',
        city='Bontleng',
        country='Botswana')


class EdcLabAppConfig(BaseEdcLabAppConfig):
    requisition_model = 'ambition_subject.subjectrequisition'


class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
    reason_field = {'ambition_subject.subjectvisit': 'reason'}
    create_on_reasons = [SCHEDULED, UNSCHEDULED]
    delete_on_reasons = [LOST_VISIT, FAILED_ELIGIBILITY]


class EdcTimepointAppConfig(BaseEdcTimepointAppConfig):
    timepoints = [
        Timepoint(
            model='ambition_subject.appointment',
            datetime_field='appt_datetime',
            status_field='appt_status',
            closed_status='DONE'
        ),
        Timepoint(
            model='ambition_subject.historicalappointment',
            datetime_field='appt_datetime',
            status_field='appt_status',
            closed_status='DONE'
        ),
    ]


class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
    visit_models = {
        'ambition_subject': ('subject_visit', 'ambition_subject.subjectvisit')}
