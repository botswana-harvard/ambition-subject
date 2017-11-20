from ambition_validators import SubjectVisitFormValidator
from django import forms
from edc_base.modelform_mixins import CommonCleanModelFormMixin
from edc_consent.modelform_mixins import RequiresConsentModelFormMixin
from edc_form_validators import FormValidatorMixin


from ..models import SubjectVisit


class SubjectVisitForm (FormValidatorMixin, RequiresConsentModelFormMixin,
                        CommonCleanModelFormMixin, forms.ModelForm):

    form_validator_cls = SubjectVisitFormValidator

    class Meta:
        model = SubjectVisit
        fields = '__all__'
