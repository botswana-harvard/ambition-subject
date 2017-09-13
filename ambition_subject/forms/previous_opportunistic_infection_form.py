# from ambition_validators import FluconazoleMissedDosesFormValidator

from ..models import PreviousOpportunisticInfection
from .form_mixins import SubjectModelFormMixin


class PreviousOpportunisticInfectionForm(SubjectModelFormMixin):

    #     form_validator_cls = FluconazoleMissedDosesFormValidator

    class Meta:
        model = PreviousOpportunisticInfection
        fields = '__all__'
