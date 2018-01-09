from django import forms
from edc_form_validators import FormValidatorMixin
from edc_visit_tracking.form_validators import VisitFormValidator

from ..models import SubjectVisit


class SubjectVisitForm (FormValidatorMixin, forms.ModelForm):

    form_validator_cls = VisitFormValidator

    class Meta:
        model = SubjectVisit
        fields = '__all__'
