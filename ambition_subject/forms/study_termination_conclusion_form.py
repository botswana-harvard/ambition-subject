from django.apps import apps as django_apps
from django import forms
from ambition_validators import StudyTerminationConclusionFormValidator

from ..models import PatientHistory, StudyTerminationConclusion
from .form_mixins import SubjectModelFormMixin


class StudyTerminationConclusionForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        try:
            form_validator = StudyTerminationConclusionFormValidator(
                cleaned_data=cleaned_data, instance=self.instance,
                patient_history_cls=django_apps.get_model(PatientHistory._meta.label_lower))
        except TypeError:
            pass
        else:
            cleaned_data = form_validator.validate()
        return cleaned_data

    action_identifier = forms.CharField(
        label='Action Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = StudyTerminationConclusion
        fields = '__all__'
