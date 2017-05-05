from edc_constants.constants import YES, NO

from .form_mixins import SubjectModelFormMixin
from ..models import FollowUp


class FollowUpForm(SubjectModelFormMixin):

    def clean(self):

            self.required_if(
                YES,
                field='other_significant_new_diagnosis',
                field_required='diagnosis_date')
            self.required_if(
                NO,
                field='fluconazole_dose',
                field_required='other_fluconazole_dose_reason')
            self.required_if(
                YES,
                field='other_fluconazole_dose',
                field_required='other_fluconazole_dose_reason')
            self.required_if(
                YES,
                field='is_rifampicin_started',
                field_required='study_day_rifampicin_started')

    class Meta:
        model = FollowUp
        fields = '__all__'
