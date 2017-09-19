from ambition_validators import SignificantDiagnosesFormValidator

from ..models import SignificantDiagnoses
from .form_mixins import SubjectModelFormMixin


class SignificantDiagnosesForm(SubjectModelFormMixin):

    form_validator_cls = SignificantDiagnosesFormValidator

    class Meta:
        model = SignificantDiagnoses
        fields = '__all__'
