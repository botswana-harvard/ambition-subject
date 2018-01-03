from ambition_validators import SubjectVisitFormValidator
from django import forms
from edc_form_validators import FormValidatorMixin


from ..models import SubjectVisit


class SubjectVisitForm (FormValidatorMixin, forms.ModelForm):

    form_validator_cls = SubjectVisitFormValidator

    class Meta:
        model = SubjectVisit
        fields = '__all__'
