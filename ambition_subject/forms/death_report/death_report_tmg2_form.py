from ambition_validators import DeathFormValidator

from ...models import DeathReportTmg2

from ..form_mixins import SubjectModelFormMixin


class DeathReportTmg2Form(SubjectModelFormMixin):

    form_validator_cls = DeathFormValidator

    class Meta:
        model = DeathReportTmg2
        fields = '__all__'
