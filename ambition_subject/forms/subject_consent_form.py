from dateutil.relativedelta import relativedelta
from django import forms

from ..models import SubjectConsent


class SubjectConsentForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()

        if 'consent_datetime' in cleaned_data:
            if not self.cleaned_data.get('consent_datetime'):
                raise forms.ValidationError(
                    'Please indicate the consent datetime.')
        self.validate_age_with_screening(cleaned_data)
        self.validate_gender_with_screening(cleaned_data)
        return cleaned_data

    def validate_age_with_screening(self, cleaned_data):
        dob = cleaned_data.get('dob')
        subject_screening = cleaned_data.get(
            'subject_screening')
        try:
            dob_age_at_screening = relativedelta(
                subject_screening.report_datetime.date(), dob).years
            if dob_age_at_screening != subject_screening.age_in_years:
                raise forms.ValidationError(
                    'The date of birth entered does not match the age at '
                    'screening.')
        except subject_screening.DoesNotExist:
            raise forms.ValidationError(
                'Complete the Subject screening form before proceeding.')

    def validate_gender_with_screening(self, cleaned_data):
        subject_screening = cleaned_data.get(
            'subject_screening')
        consent_gender = cleaned_data.get('gender')
        try:
            if subject_screening.gender != cleaned_data.get('gender'):
                raise forms.ValidationError(
                    f'Gender mismatch, Screening gender: {subject_screening.gender}, '
                    f'Consent gender: {consent_gender}')
        except subject_screening.DoesNotExist:
            raise forms.ValidationError(
                'Complete the Subject screening form before proceeding.')

    class Meta:
        model = SubjectConsent
        fields = '__all__'
