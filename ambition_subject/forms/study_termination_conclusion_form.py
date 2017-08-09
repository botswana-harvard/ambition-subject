from ambition_subject_validators import (
    StudyTerminationConclusionFormValidator)

from ..models import StudyTerminationConclusion
from .form_mixins import SubjectModelFormMixin


class StudyTerminationConclusionForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = StudyTerminationConclusionFormValidator(
            cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = StudyTerminationConclusion
        fields = '__all__'
