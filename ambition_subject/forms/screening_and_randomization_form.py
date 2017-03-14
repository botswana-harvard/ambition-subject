from .form_mixins import SubjectModelFormMixin

from ..models import ScreeningRandomization


class ScreeningRandomizationForm(SubjectModelFormMixin):

    class Meta():
        model = ScreeningRandomization
        fields = '__all__'
