from ambition_validators import MedicalExpensesTwoDetailFormValidator

from ..models import MedicalExpensesTwoDetail
from .form_mixins import SubjectModelFormMixin


class MedicalExpensesTwoDetailForm(SubjectModelFormMixin):

    form_validator_cls = MedicalExpensesTwoDetailFormValidator

    class Meta:
        model = MedicalExpensesTwoDetail
        fields = '__all__'
