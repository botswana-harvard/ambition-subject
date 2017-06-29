from ..models import SubjectRandomization
from .form_mixins import SubjectModelFormMixin


class SubjectRandomizationForm(SubjectModelFormMixin):

    class Meta:
        model = SubjectRandomization
        fields = '__all__'
