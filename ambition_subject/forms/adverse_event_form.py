from edc_constants.constants import YES

from ..models import AdverseEvent
from .form_mixins import SubjectModelFormMixin


class AdverseEventForm(SubjectModelFormMixin):

    def clean(self):
        cleaned_data = self.cleaned_data

        self.required_if(
            YES,
            field='ae_cause_other',
            field_required='ae_cause_other_specify')
        self.required_if(
            YES,
            field='ae_cause_other',
            field_required='recurrence_cm_symptoms')
        self.required_if(
            YES,
            field='is_sa_event',
            field_required='sa_event_reason')
        self.required_if(
            YES,
            field='is_susar',
            field_required='susar_reported')
        self.required_if(
            YES,
            field='susar_reported',
            field_required='susar_reported_datetime')

    class Meta:
        model = AdverseEvent
        fields = '__all__'
