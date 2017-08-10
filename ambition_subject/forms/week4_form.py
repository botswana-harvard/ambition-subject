from django import forms

from ambition_validators import (
    SignificantDiagnosesFormValidator)

from ..models import Week4, Week4Diagnoses
from .form_mixins import SubjectModelFormMixin


class Week4Form(SubjectModelFormMixin):

    class Meta:
        model = Week4
        fields = '__all__'


class Week4DiagnosesForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = SignificantDiagnosesFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = Week4Diagnoses
        fields = '__all__'
