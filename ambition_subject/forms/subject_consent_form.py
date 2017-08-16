from ambition_validators import SubjectConsentFormValidator
from django import forms
from edc_base.modelform_validators import FormValidatorMixin

from ..models import SubjectConsent


class SubjectConsentForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = SubjectConsentFormValidator

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['guardian_name'].label = (
            'Guardian\'s Last and first name (for patients with Abnormal mental status)')
        self.fields['guardian_name'].help_text = (
            'Required only if subject is unconscious or has an abnormal mental '
            'status. Format is \'LASTNAME, FIRSTNAME\'. All uppercase separated '
            'by a comma then followed by a space.')

    screening_identifier = forms.CharField(
        label='Screening identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = SubjectConsent
        fields = '__all__'
