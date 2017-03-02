from django import forms

from ..models import SubjectConsent


class SubjectConsentForm(forms.ModelForm):

    def clean(self):
        if 'consent_datetime' in self.cleaned_data:
            if not self.cleaned_data.get('consent_datetime'):
                raise forms.ValidationError(
                    'Please indicate the consent datetime.')
        cleaned_data = super().clean()
        self.validate_with_enrollment_checklist()
        return cleaned_data

    def validate_with_enrollment_checklist(self):
        pass

    class Meta:
        model = SubjectConsent
        fields = '__all__'
