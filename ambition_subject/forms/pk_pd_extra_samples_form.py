from ..models import PkPdExtraSamples
from .form_mixins import SubjectModelFormMixin


class PkPdExtraSamplesForm(SubjectModelFormMixin):

    class Meta:
        model = PkPdExtraSamples
        fields = '__all__'
