from ambition_subject_validators import DeathFormValidator

from ..models import DeathReportTMG1

from .form_mixins import SubjectModelFormMixin


class DeathReportTMG1Form(SubjectModelFormMixin):

    form_validator_cls = DeathFormValidator

    class Meta:
        model = DeathReportTMG1
        fields = '__all__'
