# from ambition_validators import PreviousOpportunisticInfectionFormValidator

from ..models import MedicalExpenses
from .form_mixins import SubjectModelFormMixin


class MedicalExpensesForm(SubjectModelFormMixin):

    #     form_validator_cls = PreviousOpportunisticInfectionFormValidator

    class Meta:
        model = MedicalExpenses
        fields = '__all__'
