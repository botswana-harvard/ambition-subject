from edc_constants.constants import YES

from ..models import AdverseEvent
from .form_mixins import SubjectModelFormMixin


class AdverseEventForm(SubjectModelFormMixin):

    def clean(self):

        self.required_if(
            YES,
            field='other_ae_event_cause',
            field_required='other_ae_event_cause_specify')
        self.required_if(
            YES,
            field='other_ae_event_cause',
            field_required='recurrence_cm_symptoms')
        self.required_if(
            YES,
            field='is_sae_event',
            field_required='sae_event_reason')
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
