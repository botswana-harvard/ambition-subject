from ambition_validators import SubjectConsentFormValidator
from django import forms
from edc_base.modelform_validators import FormValidatorMixin
from edc_constants.choices import YES_NO

from ..choices import ID_TYPE
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

    identity_type = forms.ChoiceField(
        label='What type of identity number is this?',
        choices=ID_TYPE,
        widget=forms.RadioSelect)

    may_store_samples = forms.ChoiceField(
        label=('Does the subject agree that a portion of the blood sample '
               'that is taken be stored for genetic analysis?'),
        choices=YES_NO,
        widget=forms.RadioSelect)

    class Meta:
        model = SubjectConsent
        fields = '__all__'
