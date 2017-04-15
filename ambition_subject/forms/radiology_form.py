from .form_mixins import SubjectModelFormMixin

from ..models import Radiology


class RadiologyForm(SubjectModelFormMixin):

    class Meta():
        model = Radiology
        fields = '__all__'
