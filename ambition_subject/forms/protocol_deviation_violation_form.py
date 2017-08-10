from ambition_validators import ProtocolDeviationViolationFormValidator

from .form_mixins import SubjectModelFormMixin
from ..models import ProtocolDeviationViolation


class ProtocolDeviationViolationForm(SubjectModelFormMixin):

    form_validator_cls = ProtocolDeviationViolationFormValidator

    class Meta:
        model = ProtocolDeviationViolation
        fields = '__all__'
