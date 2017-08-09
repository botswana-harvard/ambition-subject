from ambition_subject_validators import RadiologyFormValidator

from ..models import Radiology
from .form_mixins import SubjectModelFormMixin


class RadiologyForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = RadiologyFormValidator(cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = Radiology
        fields = '__all__'
