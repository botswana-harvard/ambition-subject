from django import forms

from ..models import PrnModel


class PrnModelForm(forms.ModelForm):

    class Meta:
        model = PrnModel
        fields = '__all__'
