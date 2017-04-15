from ..models import SubjectScreening
from .form_mixins import SubjectModelFormMixin


class SubjectScreeningForm(SubjectModelFormMixin):

    class Meta:
        model = SubjectScreening
        fields = '__all__'
