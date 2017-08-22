from ambition_validators import DeathReportFormValidator

from ...models import DeathReportTmg1

from ..form_mixins import SubjectModelFormMixin


class DeathReportTmg1Form(SubjectModelFormMixin):

    form_validator_cls = DeathReportFormValidator

    class Meta:
        model = DeathReportTmg1
        fields = '__all__'
