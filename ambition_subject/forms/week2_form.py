from django import forms

from ambition_subject_validators import (
    Week2FormValidator, SignificantDiagnosesFormValidator,
    FluconazoleMissedDosesFormValidator)

from ..models import (
    Week2, AmphotericinMissedDoses, FluconazoleMissedDoses,
    FlucytosineMissedDoses, SignificantDiagnoses)
from .form_mixins import SubjectModelFormMixin


class Week2Form(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = Week2FormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = Week2
        fields = '__all__'


class SignificantDiagnosesForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['other_significant_diagnoses'].label = (
            'Other significant diagnosis since enrollment?')

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = SignificantDiagnosesFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = SignificantDiagnoses
        fields = '__all__'


class FluconazoleMissedDosesForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = FluconazoleMissedDosesFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = FluconazoleMissedDoses
        fields = '__all__'


class AmphotericinMissedDosesForm(forms.ModelForm):

    class Meta:
        model = AmphotericinMissedDoses
        fields = '__all__'


class FlucytosineMissedDosesForm(forms.ModelForm):

    class Meta:
        model = FlucytosineMissedDoses
        fields = '__all__'
