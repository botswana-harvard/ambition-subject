from ..models import Week16
from .form_mixins import SubjectModelFormMixin


class Week16Form(SubjectModelFormMixin):

    class Meta:
        model = Week16
        fields = '__all__'
