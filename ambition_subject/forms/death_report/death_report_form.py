from ambition_validators import DeathReportFormValidator

from ...models import DeathReport

from ..form_mixins import SubjectModelFormMixin


class DeathReportForm(SubjectModelFormMixin):

    form_validator_cls = DeathReportFormValidator

    class Meta:
        model = DeathReport
        fields = '__all__'
