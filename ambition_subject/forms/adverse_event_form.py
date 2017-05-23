from edc_constants.constants import YES, NO, UNKNOWN

from ..models import AdverseEvent
from .form_mixins import SubjectModelFormMixin


class AdverseEventForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = self.cleaned_data

        self.required_if(
            YES,
            field='ae_cause',
            field_required='ae_cause_other')

        self.required_if_true(
            condition=(cleaned_data.get(
                'ae_study_relation_possibility') in [NO, UNKNOWN]),
            field_required='possiblity_detail')

        self.required_if(
            YES,
            field='ae_study_relation_possibility',
            field_required='ambisome_relation')

        self.required_if(
            YES,
            field='ae_study_relation_possibility',
            field_required='fluconazole_relation')

        self.required_if(
            YES,
            field='ae_study_relation_possibility',
            field_required='amphotericin_b_relation')

    class Meta:
        model = AdverseEvent
        fields = '__all__'
