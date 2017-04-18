from .form_mixins import SubjectModelFormMixin
from ..models import ClinicNote


class ClinicNoteForm(SubjectModelFormMixin):

    class Meta:
        model = ClinicNote
        fields = '__all__'
