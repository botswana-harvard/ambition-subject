from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins.base_uuid_model import BaseUuidModel

from .model_mixins import CrfModelMixin, MedicalExpensesModelMixin


class HealthEconomicsQuestionnaire2Manager(models.Manager):

    def get_by_natural_key(self, location_care, subject_identifier,
                           visit_schedule_name, schedule_name, visit_code):
        return self.get(
            location_care=location_care,
            health_economics_questionnaire__subject_visit__subject_identifier=subject_identifier,
            health_economics_questionnaire__subject_visit__visit_schedule_name=visit_schedule_name,
            health_economics_questionnaire__subject_visit__schedule_name=schedule_name,
            health_economics_questionnaire__subject_visit__visit_code=visit_code
        )


class HealthEconomicsQuestionnaire(CrfModelMixin):

    history = HistoricalRecords()

    class Meta(CrfModelMixin.Meta):
        verbose_name_plural = 'Health Economics Questionnaires'


class HealthEconomicsQuestionnaire2(MedicalExpensesModelMixin, BaseUuidModel):

    health_economics_questionnaire = models.ForeignKey(
        HealthEconomicsQuestionnaire, on_delete=PROTECT)

    objects = HealthEconomicsQuestionnaire2Manager()

    def natural_key(self):
        return ((self.location_care,) + self.health_economics_questionnaire.natural_key())
    natural_key.dependencies = [
        'ambition_subject.healtheconomicsquestionnaire']

    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'Health Economics Questionnaire Inlines'
        unique_together = ('health_economics_questionnaire', 'location_care')
