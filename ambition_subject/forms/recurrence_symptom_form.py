from ambition_subject_validations.form_validators import RecurrenceSymptomFormValidator

from ..models import RecurrenceSymptom
from .form_mixins import SubjectModelFormMixin


class RecurrenceSymptomForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = RecurrenceSymptomFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = RecurrenceSymptom
        fields = '__all__'
