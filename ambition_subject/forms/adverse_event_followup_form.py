from .form_mixins import SubjectModelFormMixin
from ..models import AdverseEventFollowUp


class AdverseEventFollowUpForm(SubjectModelFormMixin):

    class Meta:
        model = AdverseEventFollowUp
        fields = '__all__'
