from .form_mixins import SubjectModelFormMixin

from ..models import BloodResults


class BloodResultsForm(SubjectModelFormMixin):

    class Meta():
        model = BloodResults
        fields = '__all__'
