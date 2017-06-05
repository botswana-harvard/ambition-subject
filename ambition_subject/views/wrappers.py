from django.apps import apps as django_apps

from edc_appointment.views import AppointmentModelWrapper as BaseAppointmentModelWrapper
from edc_model_wrapper import ModelWrapper

from ..models import SubjectVisit


class SubjectVisitModelWrapper(ModelWrapper):

    model = SubjectVisit
    url_namespace = 'ambition_subject'
    next_url_attrs = ['appointment']
    querystring_attrs = ['subject_identifier']

    @property
    def appointment(self):
        return self.object.subject_visit.appointment


class AppointmentModelWrapper(BaseAppointmentModelWrapper):

    visit_model_wrapper_cls = SubjectVisitModelWrapper

    next_url_name = django_apps.get_app_config(
        'ambition_subject').dashboard_url_name
    next_url_attrs = ['subject_identifier']
    querystring_attrs = ['subject_identifier']
    dashboard_url_name = django_apps.get_app_config(
        'ambition_subject').dashboard_url_name


class CrfModelWrapper(ModelWrapper):

    admin_site_name = django_apps.get_app_config(
        'ambition_subject').admin_site_name
    next_url_name = django_apps.get_app_config(
        'ambition_subject').dashboard_url_name
    next_url_attrs = ['appointment', 'subject_identifier']
    querystring_attrs = ['subject_visit']

    @property
    def subject_visit(self):
        return self.object.subject_visit

    @property
    def appointment(self):
        return self.object.subject_visit.appointment


class RequisitionModelWrapper(ModelWrapper):

    admin_site_name = django_apps.get_app_config(
        'ambition_subject').admin_site_name
    next_url_name = django_apps.get_app_config(
        'ambition_subject').dashboard_url_name
    next_url_attrs = ['appointment', 'subject_identifier']
    querystring_attrs = ['subject_visit', 'panel_name']

    @property
    def subject_visit(self):
        return self.object.subject_visit

    @property
    def appointment(self):
        return self.object.subject_visit.appointment


class SubjectConsentModelWrapper(ModelWrapper):

    model = 'ambition_subject.subjectconsent'
    next_url_name = django_apps.get_app_config(
        'ambition_subject').dashboard_url_name
    next_url_attrs = ['subject_identifier', ]
    querystring_attrs = [
        'gender', 'subject_screening', 'first_name', 'initials', 'modified']

    @property
    def subject_screening(self):
        return str(self.object.subject_screening.id)

    @property
    def subject_identifier(self):
        return str(self.object.subject_identifier)
