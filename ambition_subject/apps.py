from datetime import datetime
from dateutil.tz import gettz
from django.apps import AppConfig as DjangoApponfig

from edc_base_test.apps import AppConfig as BaseEdcBaseTestAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig, SubjectType, Cap
from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig


class AppConfig(DjangoApponfig):
    name = 'ambition_subject'
    listboard_template_name = 'ambition_subject/listboard.html'
    dashboard_template_name = 'ambition_subject/dashboard.html'
    base_template_name = 'edc_base/base.html'
    listboard_url_name = 'ambition_subject:listboard_url'
    dashboard_url_name = 'ambition_subject:dashboard_url'
    admin_site_name = 'ambition_subject_admin'

    def ready(self):
        from .models.signals import subject_consent_on_post_save


class EdcBaseTestAppConfig(BaseEdcBaseTestAppConfig):
    consent_model = 'ambition_subject.subjectconsent'


class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
    visit_models = {
        'ambition_subject': ('subject_visit', 'ambition_subject.subjectvisit')}


class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
    protocol = 'BHP099'
    protocol_number = '099'
    protocol_name = 'Ambition'
    protocol_title = ''
    subject_types = [
        SubjectType('subject', 'Research Subject',
                    Cap(model_name='ambition_subject.subjectconsent', max_subjects=9999)),
    ]
    study_open_datetime = datetime(2016, 12, 31, 0, 0, 0, tzinfo=gettz('UTC'))
    study_close_datetime = datetime(2019, 12, 31, 0, 0, 0, tzinfo=gettz('UTC'))

    @property
    def site_name(self):
        return 'Gaborone'

    @property
    def site_code(self):
        return '40'
