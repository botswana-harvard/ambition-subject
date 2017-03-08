from .form_mixins import SubjectModelFormMixin

from ..models import PatientHistory


class PatientHistoryForm(SubjectModelFormMixin):

    class Meta():
        model = PatientHistory
        fields = '__all__'
