from ..models import BloodResult
from .form_mixins import SubjectModelFormMixin


class BloodResultForm(SubjectModelFormMixin):

    class Meta:
        model = BloodResult
        fields = '__all__'
