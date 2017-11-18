from ambition_validators import EducationFormValidator

from ..models import EducationHoh
from .form_mixins import SubjectModelFormMixin


class EducationHohForm(SubjectModelFormMixin):

    form_validator_cls = EducationFormValidator

    class Meta:
        model = EducationHoh
        fields = '__all__'
