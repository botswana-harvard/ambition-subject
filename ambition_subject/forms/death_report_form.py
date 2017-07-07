from ambition_subject_validations.form_validators import DeathFormValidator

from ..models import DeathReport

from .form_mixins import SubjectModelFormMixin


class DeathReportForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = DeathFormValidator(
            cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = DeathReport
        fields = '__all__'
