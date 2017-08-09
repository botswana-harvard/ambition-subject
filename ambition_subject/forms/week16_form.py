from ambition_subject_validators import Week16FormValidator

from ..models import Week16
from .form_mixins import SubjectModelFormMixin


class Week16Form(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = Week16FormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = Week16
        fields = '__all__'
