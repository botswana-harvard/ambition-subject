from .form_mixins import SubjectModelFormMixin

from ..models import RecurrenceSymptoms


class RecurrenceSymptomsForm(SubjectModelFormMixin):

    class Meta():
        model = RecurrenceSymptoms
        fields = '__all__'
