from ambition_validators import PatientHistoryFormValidator
from django import forms

from ..models import PatientHistory
from .form_mixins import SubjectModelFormMixin


class PatientHistoryForm(SubjectModelFormMixin):

    form_validator_cls = PatientHistoryFormValidator

    class Meta:
        model = PatientHistory
        fields = '__all__'
