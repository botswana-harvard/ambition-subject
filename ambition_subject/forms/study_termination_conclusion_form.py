from .form_mixins import SubjectModelFormMixin

from ..models import StudyTerminationConclusion


class StudyTerminationConclusionForm(SubjectModelFormMixin):

    class Meta():
        model = StudyTerminationConclusion
        fields = '__all__'
