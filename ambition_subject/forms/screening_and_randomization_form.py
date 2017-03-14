from edc_constants.constants import YES

from ..models import ScreeningRandomization
from .form_mixins import SubjectModelFormMixin


class ScreeningRandomizationForm(SubjectModelFormMixin):

    def clean(self):

        self.required_if(
            YES,
            field='already_on_arvs',
            field_required='arv_start_date')

    class Meta():
        model = ScreeningRandomization
        fields = '__all__'
