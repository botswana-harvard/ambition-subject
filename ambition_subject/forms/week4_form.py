from edc_base.modelform_validators import FormValidatorMixin
from ambition_validators import SignificantDiagnosesFormValidator, Week4FormValidator

from ..models import Week4, Week4Diagnoses
from .form_mixins import SubjectModelFormMixin


class Week4Form(SubjectModelFormMixin):

    form_validator_cls = Week4FormValidator

    class Meta:
        model = Week4
        fields = '__all__'


class Week4DiagnosesForm(FormValidatorMixin):

    form_validator_cls = SignificantDiagnosesFormValidator

    class Meta:
        model = Week4Diagnoses
        fields = '__all__'
