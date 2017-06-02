from django.apps import apps as django_apps
from django.db import models
from django.db.models.deletion import PROTECT

from edc_base.model_mixins import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentMixin
from edc_lab.model_mixins.requisition import (
    RequisitionModelMixin, RequisitionStatusMixin, RequisitionIdentifierMixin)
from edc_metadata.model_mixins.updates import UpdatesRequisitionMetadataModelMixin
from edc_offstudy.model_mixins import OffstudyMixin
from edc_search.model_mixins import SearchSlugManager
from edc_visit_tracking.managers import (
    CrfModelManager as VisitTrackingCrfModelManager)
from edc_visit_tracking.model_mixins import (
    CrfModelMixin as VisitTrackingCrfModelMixin, PreviousVisitModelMixin)

from .model_mixins import SearchSlugModelMixin
from .subject_visit import SubjectVisit


class Manager(VisitTrackingCrfModelManager, SearchSlugManager):
    pass


class SubjectRequisition(
        RequisitionModelMixin, RequisitionStatusMixin, RequisitionIdentifierMixin,
        VisitTrackingCrfModelMixin, OffstudyMixin,
        RequiresConsentMixin, PreviousVisitModelMixin,
        UpdatesRequisitionMetadataModelMixin, SearchSlugModelMixin,
        BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)

    objects = Manager()

    def save(self, *args, **kwargs):
        if not self.id:
            edc_protocol_app_config = django_apps.get_app_config(
                'edc_protocol')
            self.study_site = edc_protocol_app_config.site_code
            self.study_site_name = edc_protocol_app_config.site_name
        super().save(*args, **kwargs)

    def get_slugs(self):
        return ([self.subject_visit.subject_identifier,
                 self.requisition_identifier,
                 self.human_readable_identifier,
                 self.identifier_prefix])

    class Meta(VisitTrackingCrfModelMixin.Meta, RequiresConsentMixin.Meta):
        consent_model = 'ambition_subject.subjectconsent'
        app_label = 'ambition_subject'
