from .form_mixins import SubjectModelFormMixin

from ..models import ProtocolDeviationViolation


class ProtocolDeviationViolationForm(SubjectModelFormMixin):

    class Meta():
        model = ProtocolDeviationViolation
        fields = '__all__'
