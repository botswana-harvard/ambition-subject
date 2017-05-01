from django import forms

from edc_constants.constants import OTHER, YES

from ..models import RecurrenceSymptom
from .form_mixins import SubjectModelFormMixin


class RecurrenceSymptomForm(SubjectModelFormMixin):

    def clean(self):

        self.required_if(
            YES,
            field='amb_administered',
            field_required='amb_duration')

        self.required_if(
            YES,
            field='steroids_administered',
            field_required='steroids_duration')

        self.required_if(
            YES,
            field='steroids_administered',
            field_required='steroids_choices')

        self.required_if(
            OTHER,
            field='steroids_choices',
            field_required='steroids_choices_other')

        self.required_if(
            OTHER,
            field='antibiotic_treatment',
            field_required='antibiotic_treatment_other')

        self.required_if(
            YES,
            field='on_arvs',
            field_required='arv_date')

        self.required_if(
            OTHER,
            field='dr_opinion',
            field_required='dr_opinion_other')

        self.validate_employed_reason()
        self.validate_neurological_symptom()
        self.validate_focal_neurologic_deficit()

    def validate_meningitis_symptom(self):
        cleaned_data = self.cleaned_data
        if OTHER in cleaned_data.get('meningitis_symptom'):
            if not cleaned_data('meningitis_symptom_other'):
                raise forms.ValidationError({
                    'meningitis_symptom_other': [
                        'If other symptom is selected then this field is '
                        'required.']})

    def validate_focal_neurologic_deficit(self):
        cleaned_data = self.cleaned_data
        if OTHER in cleaned_data.get('neurological'):
            if not cleaned_data('focal_neurologic_deficit'):
                raise forms.ValidationError({
                    'focal_neurologic_deficit': [
                        'If focal neurologic deficit is selected then this '
                        ' field is required.']})

    def validate_neurological_symptom(self):
        cleaned_data = self.cleaned_data
        if OTHER in cleaned_data.get('neurological'):
            if not cleaned_data('neurological_other'):
                raise forms.ValidationError({
                    'neurological_other': [
                        'If other neurological symptom is selected then this '
                        ' field is required.']})

    class Meta:
        model = RecurrenceSymptom
        fields = '__all__'
