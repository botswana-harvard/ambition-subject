from ..models import PatientHistory
from .form_mixins import SubjectModelFormMixin
from ambition_validators import PatientHistoryFormValidator
from django.forms import forms
from edc_base.modelform_validators.base_form_validator import NOT_REQUIRED_ERROR
from edc_constants.constants import NOT_APPLICABLE, YES


class PatientHistoryForm(SubjectModelFormMixin):

    form_validator_cls = PatientHistoryFormValidator

    def clean(self):
        if (self.data.get('care_before_hospital') == YES
                and self.data.get('medicalexpenses_set-0-location_care') is NOT_APPLICABLE):

            message = 'This field is applicable.'
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)

        if self.data.get('medicalexpenses_set-3-location_care'):
            message = 'Exceeded maximum number of medical expenses inlines.'
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)

    class Meta:
        model = PatientHistory
        fields = '__all__'
