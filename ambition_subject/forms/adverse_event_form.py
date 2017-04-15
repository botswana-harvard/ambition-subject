from .form_mixins import SubjectModelFormMixin

from ..models import AdverseEvent


class AdverseEventForm(SubjectModelFormMixin):

    class Meta():
        model = AdverseEvent
        fields = '__all__'
