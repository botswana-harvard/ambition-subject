from edc_consent.modelform_mixins import ConsentModelFormMixin
from ambition_validators import SubjectConsentFormValidator
from django import forms
from edc_base.modelform_validators import FormValidatorMixin

from ..models import SubjectConsent


class SubjectConsentForm(FormValidatorMixin, ConsentModelFormMixin, forms.ModelForm):

    form_validator_cls = SubjectConsentFormValidator

    def clean_gender_of_consent(self):
        return None

    def clean_guardian_and_dob(self):
        return None

    def clean_identity_with_unique_fields(self):
        return None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['guardian_name'].label = (
            'Guardian\'s Last and first name (for patients with Abnormal mental status)')
        self.fields['guardian_name'].help_text = (
            'Required only if participant is unconscious or has an abnormal mental '
            'status. Format is \'LASTNAME, FIRSTNAME\'. All uppercase separated '
            'by a comma then followed by a space.')
        self.fields['identity'].label = (
            'Identity number (Country ID Number, etc)')
        self.fields['identity'].help_text = (
            'Use Country ID Number, Passport number, driver\'s license '
            'number or Country ID receipt number')
        self.fields['witness_name'].help_text = (
            'Required only if participant is illiterate. '
            'Format is \'LASTNAME, FIRSTNAME\'. '
            'All uppercase separated by a comma.'),

    screening_identifier = forms.CharField(
        label='Screening identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = SubjectConsent
        fields = '__all__'
