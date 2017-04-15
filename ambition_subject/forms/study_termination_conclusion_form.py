from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import StudyTerminationConclusion


class StudyTerminationConclusionForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        self.validate_last_research_termination_date(cleaned_data)

    def validate_last_research_termination_date(self, cleaned_data):
        if (cleaned_data.get('last_research_termination_date') == cleaned_data.get(
                'date_patient_terminated_study')):
            raise forms.ValidationError({
                'last_research_termination_date':
                'This field is not applicable as'})

    def validate_last_research_termination_study_day(self, cleaned_data):
        if (cleaned_data.get('termination_study_day')
                == cleaned_data.get('last_research_termination_study_day')):
            raise forms.ValidationError({
                'last_research_termination_study_day':
                'This field is not applicable as'})

    class Meta:
        model = StudyTerminationConclusion
        fields = '__all__'
