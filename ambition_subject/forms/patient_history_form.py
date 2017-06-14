from ambition_subject_validations.form_validators import PatientHistoryFormValidator

from ..models import PatientHistory
from .form_mixins import SubjectModelFormMixin


class PatientHistoryForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = PatientHistoryFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = PatientHistory
        fields = '__all__'
