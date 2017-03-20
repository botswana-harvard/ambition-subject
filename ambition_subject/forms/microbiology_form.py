from .form_mixins import SubjectModelFormMixin

from ..models import Microbiology


class MicrobiologyForm(SubjectModelFormMixin):

    class Meta():

        model = Microbiology
        fields = '__all__'
