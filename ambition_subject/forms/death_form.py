from .form_mixins import SubjectModelFormMixin

from ..models import DeathReport


class DeathForm(SubjectModelFormMixin):

    class Meta():
        model = DeathReport
        fields = '__all__'
