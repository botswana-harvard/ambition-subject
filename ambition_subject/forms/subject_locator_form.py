from django import forms

from edc_constants.constants import YES, NO

from ..models import SubjectLocator
from .form_mixins import SubjectModelFormMixin


class SubjectLocatorForm (SubjectModelFormMixin):

    subject_identifier = forms.CharField(
        label='Subject identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def clean(self):
        cleaned_data = super().clean()

        self.validate_has_contacts_for_hic()

        self.required_if(
            YES, field='home_visit_permission', field_required='physical_address')
        self.required_if(
            YES, field='may_follow_up', field_required='subject_cell')
        self.not_required_if(
            NO, field='may_follow_up', field_required='subject_cell_alt', inverse=False)
        self.not_required_if(
            NO, field='may_follow_up', field_required='subject_phone', inverse=False)
        self.not_required_if(
            NO, field='may_follow_up', field_required='subject_phone_alt', inverse=False)

        return cleaned_data

    class Meta:
        model = SubjectLocator
        fields = '__all__'
