from django.db import models
from django.db.models.deletion import PROTECT

from edc_base.model_mixins import BaseUuidModel
from edc_base.model_managers import HistoricalRecords
from edc_lab.model_mixins.result import ResultModelMixin

from ..subject_requisition import SubjectRequisition


class ResultManager(models.Manager):

    def get_by_natural_key(self, report_datetime, requisition_identifier):
        return self.get(
            report_datetime=report_datetime,
            requisition__requisition_identifier=requisition_identifier,)


class Result(ResultModelMixin, BaseUuidModel):

    requisition = models.ForeignKey(SubjectRequisition, on_delete=PROTECT)

    objects = ResultManager()

    history = HistoricalRecords()

    def natural_key(self):
        return (
            self.report_datetime, self.requisition.requisition_identifier,)

    class Meta:
        app_label = 'edc_lab'
