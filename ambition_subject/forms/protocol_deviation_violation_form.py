from ambition_subject_validations.form_validators import ProtocolDeviationViolationFormValidator

from .form_mixins import SubjectModelFormMixin
from ..models import ProtocolDeviationViolation


class ProtocolDeviationViolationForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = ProtocolDeviationViolationFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = ProtocolDeviationViolation
        fields = '__all__'
