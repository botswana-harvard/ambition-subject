from ambition_subject_validators import LumbarPunctureCSFFormValidator

from ..models import LumbarPunctureCsf
from .form_mixins import SubjectModelFormMixin


class LumbarPunctureCSFForm(SubjectModelFormMixin):

    form_validator_cls = LumbarPunctureCSFFormValidator

    class Meta:
        model = LumbarPunctureCsf
        fields = '__all__'
