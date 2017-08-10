from ambition_validators import DeathFormValidator

from ..models import DeathReport

from .form_mixins import SubjectModelFormMixin


class DeathReportForm(SubjectModelFormMixin):

    form_validator_cls = DeathFormValidator

    class Meta:
        model = DeathReport
        fields = '__all__'
