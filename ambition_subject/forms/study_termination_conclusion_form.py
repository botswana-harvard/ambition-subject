from django import forms

from edc_constants.constants import NO, YES

from ..constants import CONSENT_WITHDRAWAL
from ..models import StudyTerminationConclusion
from .form_mixins import SubjectModelFormMixin


class StudyTerminationConclusionForm(SubjectModelFormMixin):

    def clean(self):

        self.required_if(
            YES,
            field='discharged_after_initial_admission',
            field_required='initial_discharge_date')

        self.required_if(
            YES,
            field='discharged_after_initial_admission',
            field_required='initial_discharge_study_date')

        self.required_if(
            YES,
            field='readmission_following_initial_discharge',
            field_required='date_admitted')

        self.required_if(
            CONSENT_WITHDRAWAL,
            field='study_termination_reason',
            field_required='withdrawal_of_consent_reason')

        self.required_if(
            YES,
            field='rifampicin_started_since_week4',
            field_required='rifampicin_started_study_day')

        self.required_if(
            YES,
            field='is_naive',
            field_required='date_started_arvs')

        self.required_if(
            NO,
            field='is_naive',
            field_required='date_switched_arvs')

        self.required_if(
            YES,
            field='is_first_line_regimen',
            field_required='efv_or_nvp')

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
