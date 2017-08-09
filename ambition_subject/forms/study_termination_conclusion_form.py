from ambition_subject_validators import (
    StudyTerminationConclusionFormValidator)

from ..models import StudyTerminationConclusion
from .form_mixins import SubjectModelFormMixin


class StudyTerminationConclusionForm(SubjectModelFormMixin):

    form_validator_cls = StudyTerminationConclusionFormValidator

    class Meta:
        model = StudyTerminationConclusion
        fields = '__all__'
