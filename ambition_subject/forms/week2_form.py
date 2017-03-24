from .form_mixins import SubjectModelFormMixin

from ..models import Week2


class Week2Form(SubjectModelFormMixin):

    class Meta():
        model = Week2
        fields = '__all__'
