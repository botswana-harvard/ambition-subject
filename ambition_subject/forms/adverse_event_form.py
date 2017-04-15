from ..models import AdverseEvent
from .form_mixins import SubjectModelFormMixin


class AdverseEventForm(SubjectModelFormMixin):

    class Meta:
        model = AdverseEvent
        fields = '__all__'
