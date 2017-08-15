from ambition_validators import SubjectVisitFormValidator
from django import forms
from edc_base.modelform_mixins import CommonCleanModelFormMixin
from edc_base.modelform_validators import FormValidatorMixin
from edc_consent.modelform_mixins import RequiresConsentModelFormMixin

from ..choices import VISIT_REASON
from ..models import SubjectVisit


class SubjectVisitForm (FormValidatorMixin, RequiresConsentModelFormMixin,
                        CommonCleanModelFormMixin, forms.ModelForm):

    form_validator_cls = SubjectVisitFormValidator

    reason = forms.ChoiceField(
        label='What is the reason for this visit?',
        choices=VISIT_REASON,
        widget=forms.RadioSelect)

    class Meta:
        model = SubjectVisit
        fields = '__all__'
