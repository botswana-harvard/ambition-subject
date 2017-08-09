from django import forms

from ambition_subject_validators import (
    FollowUpFormValidator, SignificantDiagnosesFormValidator)
from .form_mixins import SubjectModelFormMixin

from ..models import FollowUp, FollowUpDiagnoses


class FollowUpForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = FollowUpFormValidator(cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = FollowUp
        fields = '__all__'


class FollowUpDiagnosesForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = SignificantDiagnosesFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = FollowUpDiagnoses
        fields = '__all__'
