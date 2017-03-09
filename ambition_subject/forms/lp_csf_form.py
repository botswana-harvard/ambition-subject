from .form_mixins import SubjectModelFormMixin

from ..models import LpCsf


class LpCsfForm(SubjectModelFormMixin):

    class Meta():
        model = LpCsf
        fields = '__all__'
