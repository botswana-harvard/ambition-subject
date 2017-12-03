from django import forms
from ambition_validators import ProtocolDeviationViolationFormValidator

from .form_mixins import SubjectModelFormMixin
from ..models import ProtocolDeviationViolation


class ProtocolDeviationViolationForm(SubjectModelFormMixin):

    form_validator_cls = ProtocolDeviationViolationFormValidator

    action_identifier = forms.CharField(
        label='Action Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = ProtocolDeviationViolation
        fields = '__all__'
