from ambition_validators import AmphotericinMissedDosesFormValidator

from ..models import AmphotericinMissedDoses
from .form_mixins import SubjectModelFormMixin


class AmphotericinMissedDosesForm(SubjectModelFormMixin):

    form_validator_cls = AmphotericinMissedDosesFormValidator

    class Meta:
        model = AmphotericinMissedDoses
        fields = '__all__'
