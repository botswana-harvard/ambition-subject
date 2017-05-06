from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from django.urls.base import reverse

from edc_appointment.views import AppointmentModelWrapper
from edc_dashboard.wrappers.model_wrapper import ModelWrapper


class ModelWrapperMixin(ModelWrapper):

    next_url_name = django_apps.get_app_config(
        'ambition_subject').dashboard_url_name
    extra_querystring_attrs = {}
    next_url_attrs = {'edc_appointment.appointment': ['subject_identifier']}
    url_instance_attrs = ['subject_identifier']


class SubjectVisitModelWrapper(ModelWrapperMixin):

    model_name = 'ambition_subject.subjectvisit'
    extra_querystring_attrs = {
        'ambition_subject.subjectvisit': ['household_member']}
    next_url_attrs = {'ambition_subject.subjectvisit': [
        'appointment', 'subject_identifier']}
    url_instance_attrs = ['subject_identifier', 'appointment']


class AppointmentModelWrapper(AppointmentModelWrapper, ModelWrapperMixin):

    model_name = 'ambition_subject.appointment'
    visit_model_wrapper_class = SubjectVisitModelWrapper
    dashboard_url_name = django_apps.get_app_config(
        'ambition_subject').dashboard_url_name

    @property
    def visit(self):
        """Returns a wrapped persistent or non-persistent visit
        instance.
        """
        # FIXME: to much overriden from super class
        # only difference are the options for the visit model
        try:
            return self.visit_model_wrapper_class(self._original_object.subjectvisit)
        except ObjectDoesNotExist:
            visit_model = django_apps.get_model(
                *self.visit_model_wrapper_class.model_name.split('.'))
            return self.visit_model_wrapper_class(
                visit_model(
                    appointment=self._original_object,
                    subject_identifier=self.subject_identifier))

    @property
    def forms_url(self):
        """Returns a reversed URL to show forms for this
        appointment/visit.

        This is standard for edc_dashboard
        """
        # FIXME: to much overriden from super class
        # only difference are the extra kwargs tp reverse
        kwargs = dict(
            subject_identifier=self.subject_identifier,
            appointment=self._original_object.id)
        return reverse(self.dashboard_url_name, kwargs=kwargs)


class CrfModelWrapper(ModelWrapper):

    admin_site_name = django_apps.get_app_config(
        'ambition_subject').admin_site_name
    url_namespace = 'ambition_subject'
    next_url_name = django_apps.get_app_config(
        'ambition_subject').dashboard_url_name
    next_url_attrs = dict(crf=[
        'appointment', 'subject_identifier'])
    extra_querystring_attrs = {
        'crf': ['subject_visit']}
    url_instance_attrs = [
        'appointment', 'subject_identifier', 'subject_visit']

    @property
    def appointment(self):
        return self._original_object.subject_visit.appointment


class SubjectLocatorModelWrapper(ModelWrapper):
    model_name = 'ambition_subject.subjectlocator'
    admin_site_name = django_apps.get_app_config(
        'ambition_subject').admin_site_name
    url_namespace = 'ambition_subject'
    next_url_name = django_apps.get_app_config(
        'ambition_subject').dashboard_url_name
    next_url_attrs = {
        'ambition_subject.subjectlocator': ['subject_identifier']}
    url_instance_attrs = ['subject_identifier']


class RequisitionModelWrapper(ModelWrapper):

    admin_site_name = django_apps.get_app_config(
        'ambition_subject').admin_site_name
    url_namespace = 'ambition_subject'
    next_url_name = django_apps.get_app_config(
        'ambition_subject').dashboard_url_name
    next_url_attrs = dict(requisition=[
        'appointment', 'subject_identifier'])
    extra_querystring_attrs = {
        'requisition': ['subject_visit', 'panel_name']}
    url_instance_attrs = [
        'appointment', 'subject_identifier', 'subject_visit', 'panel_name']

    @property
    def subject_visit(self):
        return self._original_object.subject_visit

    @property
    def appointment(self):
        return self._original_object.subject_visit.appointment


class SubjectConsentModelWrapper(ModelWrapper):

    model_name = 'ambition_subject.subjectconsent'
    next_url_name = django_apps.get_app_config(
        'ambition_subject').dashboard_url_name
    next_url_attrs = {
        'ambition_subject.subjectconsent': ['subject_identifier']}
    extra_querystring_attrs = {
        'ambition_subject.subjectconsent': ['gender', 'first_name', 'initials']}
    url_instance_attrs = [
        'subject_identifier', 'gender', 'first_name', 'initials']


class SubjectScreeningModelWrapper(ModelWrapper):

    model_name = 'ambition_subject.subjectscreening'
    next_url_name = django_apps.get_app_config(
        'ambition_subject').dashboard_url_name
    next_url_attrs = {
        'ambition_subject.subjectscreening': ['screening_identifier']}
    extra_querystring_attrs = {
        'ambition_subject.subjectscreening': ['sex']}
    url_instance_attrs = [
        'screening_identifier', 'sex']
