from ambition_subject_validations.form_validators import DeathFormValidator

from ..models import DeathReportTMG2

from .form_mixins import SubjectModelFormMixin


class DeathReportTMG2Form(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = DeathFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = DeathReportTMG2
        fields = '__all__'
