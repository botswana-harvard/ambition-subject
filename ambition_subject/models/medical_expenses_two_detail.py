from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins.base_uuid_model import BaseUuidModel

from .model_mixins import MedicalExpensesModelMixin
from .medical_expenses_two import MedicalExpensesTwo


class ModelManager(models.Manager):

    def get_by_natural_key(self, location_care, subject_identifier,
                           visit_schedule_name, schedule_name, visit_code):
        return self.get(
            location_care=location_care,
            medical_expenses_two__subject_visit__subject_identifier=subject_identifier,
            medical_expenses_two__subject_visit__visit_schedule_name=visit_schedule_name,
            medical_expenses_two__subject_visit__schedule_name=schedule_name,
            medical_expenses_two__subject_visit__visit_code=visit_code
        )


class MedicalExpensesTwoDetail(MedicalExpensesModelMixin, BaseUuidModel):

    medical_expenses_two = models.ForeignKey(
        MedicalExpensesTwo, on_delete=PROTECT)

    objects = ModelManager()

    def natural_key(self):
        return ((self.location_care,) + self.medical_expenses_two.natural_key())
    natural_key.dependencies = ['ambition_subject.medicalexpensestwo']

    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Medical Expenses Part 2: Detail'
        verbose_name_plural = 'Medical Expenses Part 2: Detail'
        unique_together = ('medical_expenses_two', 'location_care')
