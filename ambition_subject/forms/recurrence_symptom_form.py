from ambition_validators import RecurrenceSymptomFormValidator

from ..models import RecurrenceSymptom
from .form_mixins import SubjectModelFormMixin


class RecurrenceSymptomForm(SubjectModelFormMixin):

    form_validator_cls = RecurrenceSymptomFormValidator

    class Meta:
        model = RecurrenceSymptom
        fields = '__all__'
