from ..models import LumbarPunctureCsf
from .form_mixins import SubjectModelFormMixin


class LumbarPunctureCSFForm(SubjectModelFormMixin):

    class Meta:
        model = LumbarPunctureCsf
        fields = '__all__'
