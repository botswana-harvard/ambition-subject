from ..models import EducationalBackground
from .form_mixins import SubjectModelFormMixin
from ambition_validators import EducationalBackgroundFormValidator


class EducationalBackgroundForm(SubjectModelFormMixin):

    form_validator_cls = EducationalBackgroundFormValidator

    class Meta:
        model = EducationalBackground
        fields = '__all__'
