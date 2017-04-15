from .form_mixins import SubjectModelFormMixin

from ..models import SubjectScreening


class SubjectScreeningForm(SubjectModelFormMixin):

    class Meta():
        model = SubjectScreening
        fields = '__all__'
