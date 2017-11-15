from django.forms import forms

from edc_base.modelform_validators.base_form_validator import NOT_REQUIRED_ERROR
from edc_constants.constants import NOT_APPLICABLE, YES
from ..models import HealthEconomicsQuestionnaire
from .form_mixins import SubjectModelFormMixin


class HealthEconomicsQuestionnaireForm(SubjectModelFormMixin):

    def clean(self):

        if self.data.get('healtheconomicsquestionnaire2_set-3-location_care'):
            message = 'Exceeded maximum number of medical expenses inlines.'
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)

        if (self.data.get('healtheconomicsquestionnaire2_set-0-other_place_visited') == YES
                and self.data.get(
                    'healtheconomicsquestionnaire2_set-1-location_care') == NOT_APPLICABLE):

            message = 'Please fill in the second medical expenses inline.'
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)

        if (self.data.get('healtheconomicsquestionnaire2_set-1-other_place_visited') == YES
                and self.data.get(
                    'mhealtheconomicsquestionnaire2_set-2-location_care') == NOT_APPLICABLE):

            message = 'Please fill in the third medical expenses inline.'
            raise forms.ValidationError(message, code=NOT_REQUIRED_ERROR)

    class Meta:
        model = HealthEconomicsQuestionnaire
        fields = '__all__'
