from django import forms

from ambition_subject_validations.form_validators import Week2FormValidator

from ..models import Week2, AmphotericinMissedDoses, FluconazoleMissedDoses
from .form_mixins import SubjectModelFormMixin


class Week2Form(SubjectModelFormMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tb_pulmonary_dx'].label = (
            'Pulmonary TB diagnosis since enrollment?')

        self.fields['extra_pulmonary_tb_dx'].label = (
            'Extra pulmonary TB diagnosis since the enrollment?')

        self.fields['kaposi_sarcoma_dx'].label = (
            'Kaposi\'s sarcoma diagnosis since enrollment?')

        self.fields['malaria_dx'].label = (
            'Malaria diagnosis since enrollment?')

        self.fields['bacteraemia_dx'].label = (
            'Bacteraemia diagnosis since enrollment?')

        self.fields['pneumonia_dx'].label = (
            'Bacterial pneumonia diagnosis since enrollment?')

        self.fields['diarrhoeal_wasting_dx'].label = (
            'Diarrhoeal wasting diagnosis since enrollment?')

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = Week2FormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = Week2
        fields = '__all__'


class FluconazoleMissedDosesForm(forms.ModelForm):

    class Meta:
        model = FluconazoleMissedDoses
        fields = '__all__'


class AmphotericinMissedDosesForm(forms.ModelForm):

    class Meta:
        model = AmphotericinMissedDoses
        fields = '__all__'
