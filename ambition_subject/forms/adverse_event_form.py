from ambition_validators import AdverseEventFormValidator

from ..models import AdverseEvent
from .form_mixins import SubjectModelFormMixin


class AdverseEventForm(SubjectModelFormMixin):

    form_validator_cls = AdverseEventFormValidator

    class Meta:
        model = AdverseEvent
        fields = '__all__'
