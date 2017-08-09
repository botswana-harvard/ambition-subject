from django import forms

from ambition_subject_validators import BloodResultFormValidator

from ..models import BloodResult
from .form_mixins import SubjectModelFormMixin


class BloodResultForm(SubjectModelFormMixin, forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = BloodResultFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = BloodResult
        fields = '__all__'
