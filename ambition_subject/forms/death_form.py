from edc_constants.constants import YES, NO

from ..models import Death

from .form_mixins import SubjectModelFormMixin


class DeathForm (SubjectModelFormMixin):
    def clean(self):

        self.required_if(
            YES,
            field='cause_of_death_agreed',
            field_required='narrative_summary')
        self.required_if(
            NO,
            field='cause_of_death_study_doctor_opinion',
            field_required='cause_other_study_doctor_opinion')

    class Meta:
        model = Death
        fields = '__all__'
