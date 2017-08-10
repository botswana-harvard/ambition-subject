from ambition_subject.models.subject_screening import SubjectScreening
from ambition_validators import SubjectScreeningFormValidator
from django import forms


class SubjectScreeningForm(forms.ModelForm):

    form_validator_cls = SubjectScreeningFormValidator

    class Meta:
        model = SubjectScreening
        fields = '__all__'
