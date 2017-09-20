from django import forms

from ..models import PkPdCrf


class PkPdCrfForm(forms.ModelForm):

    class Meta:
        model = PkPdCrf
        fields = '__all__'
