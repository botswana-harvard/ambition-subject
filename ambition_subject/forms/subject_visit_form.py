from ambition_validators import SubjectVisitFormValidator
from django import forms
from edc_base.modelform_mixins import CommonCleanModelFormMixin
from edc_base.modelform_validators import FormValidatorMixin
from edc_consent.modelform_mixins import RequiresConsentModelFormMixin

from ..models import SubjectVisit
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED


class SubjectVisitForm (FormValidatorMixin, RequiresConsentModelFormMixin,
                        CommonCleanModelFormMixin, forms.ModelForm):

    form_validator_cls = SubjectVisitFormValidator

    reason = forms.ChoiceField(
        label='What is the reason for this visit?',
        choices=((SCHEDULED, 'Scheduled'), (UNSCHEDULED, 'Not scheduled')),
        widget=forms.RadioSelect)

    class Meta:
        model = SubjectVisit
        fields = '__all__'
