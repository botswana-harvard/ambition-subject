from ..models import HealthEconomicsQuestionnaire
from .form_mixins import SubjectModelFormMixin
from ambition_validators import HealthEconomicsQuestionnaireFormValidator
from django.forms import forms
from edc_base.modelform_validators.base_form_validator import NOT_REQUIRED_ERROR
from edc_constants.constants import NOT_APPLICABLE, YES


class HealthEconomicsQuestionnaireForm(SubjectModelFormMixin):

    def clean(self):
        HealthEconomicsQuestionnaireFormValidator(
            cleaned_data=self.cleaned_data).clean()

        if (self.data.get('care_before_hospital') == YES
                and self.data.get(
                    'medicalexpenses_set-0-location_care') == NOT_APPLICABLE):

            message = 'The medical expenses inline is required.'
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)

        if self.data.get('medicalexpenses_set-3-location_care'):
            message = 'Exceeded maximum number of medical expenses inlines.'
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)

        if (self.data.get('medicalexpenses_set-0-other_place_visited') == YES
                and self.data.get(
                    'medicalexpenses_set-1-location_care') == NOT_APPLICABLE):

            message = 'Please fill in the second medical expenses inline.'
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)

        if (self.data.get('medicalexpenses_set-1-other_place_visited') == YES
                and self.data.get(
                    'medicalexpenses_set-2-location_care') == NOT_APPLICABLE):

            message = 'Please fill in the third medical expenses inline.'
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)

    class Meta:
        model = HealthEconomicsQuestionnaire
        fields = '__all__'
