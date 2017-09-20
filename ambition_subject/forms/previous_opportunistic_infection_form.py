from ambition_validators import PreviousOpportunisticInfectionFormValidator

from ..models import PreviousOpportunisticInfection
from .form_mixins import SubjectModelFormMixin


class PreviousOpportunisticInfectionForm(SubjectModelFormMixin):

    form_validator_cls = PreviousOpportunisticInfectionFormValidator

    class Meta:
        model = PreviousOpportunisticInfection
        fields = '__all__'
