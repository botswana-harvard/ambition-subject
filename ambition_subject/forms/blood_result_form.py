from django import forms
from ..models import BloodResult
from .form_mixins import SubjectModelFormMixin


class BloodResultForm(SubjectModelFormMixin, forms.ModelForm):

    class Meta:
        model = BloodResult
        fields = '__all__'
