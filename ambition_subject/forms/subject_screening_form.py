from ambition_validators import SubjectScreeningFormValidator
from django import forms

from ..models.subject_screening import SubjectScreening


class SubjectScreeningForm(forms.ModelForm):

    form_validator_cls = SubjectScreeningFormValidator

    class Meta:
        model = SubjectScreening
        fields = '__all__'
