from ..models import AdverseEventTMG
from .form_mixins import SubjectModelFormMixin


class AdverseEventTMGForm(SubjectModelFormMixin):

    class Meta:
        model = AdverseEventTMG
        fields = '__all__'
