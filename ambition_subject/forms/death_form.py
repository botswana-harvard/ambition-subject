from edc_constants.constants import YES, OTHER

from ..models import Death

from .form_mixins import SubjectModelFormMixin


class DeathForm (SubjectModelFormMixin):

    def clean(self):
        cleaned_data = self.cleaned_data
        self.validate_other_specify(
            'cause_of_death_study_doctor_opinion',
            'cause_other_study_doctor_opinion')
        return cleaned_data

    class Meta:
        model = Death
        fields = '__all__'
