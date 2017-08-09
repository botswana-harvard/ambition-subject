from ambition_subject_validators import DeathFormValidator

from ..models import DeathReportTMG2

from .form_mixins import SubjectModelFormMixin


class DeathReportTMG2Form(SubjectModelFormMixin):

    form_validator_cls = DeathFormValidator

    class Meta:
        model = DeathReportTMG2
        fields = '__all__'
