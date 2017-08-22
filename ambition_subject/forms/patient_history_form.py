from ambition_validators import PatientHistoryFormValidator
from django import forms

from ..models import PatientHistory
from .form_mixins import SubjectModelFormMixin


class PatientHistoryForm(SubjectModelFormMixin):

    form_validator_cls = PatientHistoryFormValidator

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[
            'ecog_score_value'].initial = self._meta.model.ecog_score
        self.fields[
            'ecog_score_value'].widget = forms.TextInput(attrs={'readonly': 'readonly'})

    class Meta:
        model = PatientHistory
        fields = '__all__'
