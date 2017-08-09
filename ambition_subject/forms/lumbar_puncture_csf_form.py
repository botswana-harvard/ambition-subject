from ambition_subject_validators import LumbarPunctureCSFFormValidator

from ..models import LumbarPunctureCsf
from .form_mixins import SubjectModelFormMixin


class LumbarPunctureCSFForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = LumbarPunctureCSFFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = LumbarPunctureCsf
        fields = '__all__'
