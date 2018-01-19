from django import forms
from ambition_validators import PkPdCrfFormValidator

from ..models import PkPdCrf


class PkPdCrfForm(forms.ModelForm):

    form_validator_cls = PkPdCrfFormValidator

    class Meta:
        model = PkPdCrf
        fields = '__all__'
