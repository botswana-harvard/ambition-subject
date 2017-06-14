from ambition_subject_validations.form_validators import AdverseEventFormValidator

from ..models import AdverseEvent
from .form_mixins import SubjectModelFormMixin


class AdverseEventForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        adverse_event_validator = AdverseEventFormValidator(
            cleaned_data=cleaned_data)
        return adverse_event_validator.clean()

    class Meta:
        model = AdverseEvent
        fields = '__all__'
