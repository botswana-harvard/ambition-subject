from ambition_validators import HealthEconomicsQuestionnaire2FormValidator
from ..models import HealthEconomicsQuestionnaire2
from .form_mixins import SubjectModelFormMixin


class HealthEconomicsQuestionnaire2Form(SubjectModelFormMixin):

    form_validator_cls = HealthEconomicsQuestionnaire2FormValidator

    class Meta:
        model = HealthEconomicsQuestionnaire2
        fields = '__all__'
