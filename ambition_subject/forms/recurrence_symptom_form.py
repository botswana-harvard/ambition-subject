from ..models import RecurrenceSymptom
from .form_mixins import SubjectModelFormMixin


class RecurrenceSymptomForm(SubjectModelFormMixin):

    class Meta:
        model = RecurrenceSymptom
        fields = '__all__'
