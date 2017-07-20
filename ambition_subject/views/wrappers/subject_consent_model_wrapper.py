from django.apps import apps as django_apps

from edc_model_wrapper import ModelWrapper

from ...models import SubjectRandomization


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

    @property
    def randomization_arm(self):
        try:
            subject_rando_arm = SubjectRandomization.objects.get(
                subject_identifier=self.object.subject_identifier).rx
            subject_rando_arm = ' '.join(subject_rando_arm.split('_')).title()
        except SubjectRandomization.DoesNotExist:
            subject_rando_arm = None
        return subject_rando_arm
