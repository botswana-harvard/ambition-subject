from .form_mixins import SubjectModelFormMixin

from ..models import LumbarPunctureCsf


class LumbarPunctureCSFForm(SubjectModelFormMixin):

    class Meta():
        model = LumbarPunctureCsf
        fields = '__all__'
