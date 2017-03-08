from .form_mixins import SubjectModelFormMixin

from ..models import Death


class DeathForm(SubjectModelFormMixin):

    class Meta():
        model = Death
        fields = '__all__'
