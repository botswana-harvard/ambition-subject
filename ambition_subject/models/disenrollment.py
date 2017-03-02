from edc_base.model.models import BaseUuidModel
from edc_visit_schedule.model_mixins import DisenrollmentModelMixin

from ..managers import DisenrollmentManager

from edc_consent.model_mixins import RequiresConsentMixin


class Disenrollment(DisenrollmentModelMixin, RequiresConsentMixin, BaseUuidModel):

    ADMIN_SITE_NAME = 'ambition_subject_admin'

    objects = DisenrollmentManager()

    class Meta(DisenrollmentModelMixin.Meta):
        visit_schedule_name = 'visit_schedule'
        consent_model = 'ambition_subject.subjectconsent'
        app_label = 'ambition_subject'
