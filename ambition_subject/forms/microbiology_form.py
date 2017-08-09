from ambition_subject_validators import MicrobiologyFormValidator

from ..models import Microbiology

from .form_mixins import SubjectModelFormMixin


class MicrobiologyForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = MicrobiologyFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = Microbiology
        fields = '__all__'
