from edc_lab.forms import RequisitionFormMixin

from ..models import SubjectRequisition
from .form_mixins import SubjectModelFormMixin


class SubjectRequisitionForm(RequisitionFormMixin, SubjectModelFormMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['panel_name'].initial = self._meta.model.panel_name[0:21]

    class Meta:
        model = SubjectRequisition
        fields = '__all__'
