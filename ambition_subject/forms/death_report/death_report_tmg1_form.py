from ambition_validators import DeathFormValidator

from ...models import DeathReportTmg1

from ..form_mixins import SubjectModelFormMixin


class DeathReportTmg1Form(SubjectModelFormMixin):

    form_validator_cls = DeathFormValidator

    class Meta:
        model = DeathReportTmg1
        fields = '__all__'
