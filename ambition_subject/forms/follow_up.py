from ambition_subject_validations.form_validators import FollowUpFormValidator
from .form_mixins import SubjectModelFormMixin
from ..models import FollowUp


class FollowUpForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data = FollowUpFormValidator(cleaned_data=cleaned_data).clean()
        return cleaned_data

    class Meta:
        model = FollowUp
        fields = '__all__'
