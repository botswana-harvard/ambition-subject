from ambition_validators import DeathReportFormValidator

from ...models import DeathReportTmg2

from ..form_mixins import SubjectModelFormMixin


class DeathReportTmg2Form(SubjectModelFormMixin):

    form_validator_cls = DeathReportFormValidator

    class Meta:
        model = DeathReportTmg2
        fields = '__all__'
