from ambition_subject_validators import SignificantDiagnosesFormValidator

from ..models import SignificantDiagnoses
from .form_mixins import SubjectModelFormMixin


class SignificantDiagnosesForm(SubjectModelFormMixin):

    form_validator_cls = SignificantDiagnosesFormValidator

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['other_significant_diagnoses'].label = (
            'Other significant diagnosis since enrollment?')

    class Meta:
        model = SignificantDiagnoses
        fields = '__all__'
