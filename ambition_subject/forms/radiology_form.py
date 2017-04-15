from ..models import Radiology
from .form_mixins import SubjectModelFormMixin


class RadiologyForm(SubjectModelFormMixin):

    class Meta:
        model = Radiology
        fields = '__all__'
