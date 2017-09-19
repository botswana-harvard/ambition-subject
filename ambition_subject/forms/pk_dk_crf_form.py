from django import forms

from ..models import PkDkCrf


class PkDkCrfForm(forms.ModelForm):

    class Meta:
        model = PkDkCrf
        fields = '__all__'
