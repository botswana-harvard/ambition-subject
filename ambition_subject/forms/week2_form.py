from ..models import Week2
from .form_mixins import SubjectModelFormMixin


class Week2Form(SubjectModelFormMixin):

    class Meta:
        model = Week2
        fields = '__all__'
