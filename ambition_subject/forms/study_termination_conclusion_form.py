from django import forms
from ambition_validators import StudyTerminationConclusionFormValidator

from ..models import StudyTerminationConclusion
from .form_mixins import SubjectModelFormMixin


class StudyTerminationConclusionForm(SubjectModelFormMixin):

    form_validator_cls = StudyTerminationConclusionFormValidator

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
