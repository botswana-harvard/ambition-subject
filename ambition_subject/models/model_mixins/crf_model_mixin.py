from decimal import Decimal
from edc_base.model_mixins import BaseUuidModel, FormAsJSONModelMixin
from edc_base.model_validators import datetime_not_future
from edc_base.utils import get_utcnow
from edc_consent.model_mixins import RequiresConsentMixin
from edc_metadata.model_mixins.updates import UpdatesCrfMetadataModelMixin
from edc_reference.model_mixins import ReferenceModelMixin

from django.apps import apps as django_apps
from django.db import models
from django.db.models.deletion import PROTECT
from edc_base.model_managers import HistoricalRecords
from edc_offstudy.model_mixins import (
    OffstudyMixin as BaseOffstudyMixin, OffstudyError)
from edc_protocol.validators import datetime_not_before_study_start
from edc_visit_tracking.managers import CrfModelManager as VisitTrackingCrfModelManager
from edc_visit_tracking.model_mixins import (
    CrfModelMixin as VisitTrackingCrfModelMixin, PreviousVisitModelMixin)

from ..subject_visit import SubjectVisit


class OffstudyMixin(BaseOffstudyMixin):

    def neutrophils_result(self, obj=None):
        """ if absolute_neutrophil < (0.5 x 109/L ) eq 54.5 then participant is 
        ineligible, take offstudy."""
        neutrophils_allowed_limit = 0.5 * 109
        return (Decimal(obj.absolute_neutrophil or 0) <
                Decimal(neutrophils_allowed_limit))

    def platelets_result(self, obj=None):
        """ if  platelets < (50 x 109/L) then participant is ineligible. 
        take offstudy."""
        platelets_allowed_limit = 50 * 109
        return (Decimal(obj.platelets or 0) <
                Decimal(platelets_allowed_limit))

    def alt_result(self, obj=None):
        """ if  ALT > 200 IU/mL then participant is ineligible. 
        take offstudy."""
        return Decimal(obj.alt or 0) > Decimal('200')

    def is_eligible_after_blood_result(self):
        try:
            if not (self._meta.model_name == 'bloodresult' and
                    self.subject_visit.visit_code == '1000'):
                BloodResult = django_apps.get_app_config(
                    'ambition_subject').get_model('bloodresult')
                obj = BloodResult.objects.get(
                    subject_visit=self.subject_visit,
                    subject_visit__visit_code='1000')
                if any((self.neutrophils_result(obj=obj), self.platelets_result(obj=obj),
                        self.alt_result(obj=obj))):
                    return False
        except BloodResult.DoesNotExist or TypeError:
            return True
        return True

    def save(self, *args, **kwargs):
        super(OffstudyMixin, self).save(*args, **kwargs)
        if not self.is_eligible_after_blood_result():
            raise OffstudyError(
                'Participant is ineligible based on blood result. '
                'Data reported cannot be captured.')

    class Meta:
        abstract = True
        consent_model = None


class CrfModelManager(VisitTrackingCrfModelManager):

    def get_by_natural_key(self, subject_identifier, visit_schedule_name,
                           schedule_name, visit_code):
        return self.get(
            subject_visit__subject_identifier=subject_identifier,
            subject_visit__visit_schedule_name=visit_schedule_name,
            subject_visit__schedule_name=schedule_name,
            subject_visit__visit_code=visit_code
        )


class CrfModelMixin(VisitTrackingCrfModelMixin, OffstudyMixin,
                    RequiresConsentMixin, PreviousVisitModelMixin,
                    UpdatesCrfMetadataModelMixin,
                    FormAsJSONModelMixin, ReferenceModelMixin, BaseUuidModel):

    """ Base model for all scheduled models (adds key to :class:`SubjectVisit`).
    """

    subject_visit = models.OneToOneField(SubjectVisit, on_delete=PROTECT)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_future, datetime_not_before_study_start],
        default=get_utcnow,
        help_text=('If reporting today, use today\'s date/time, otherwise use '
                   'the date/time this information was reported.'))

    objects = CrfModelManager()

    history = HistoricalRecords()

    def natural_key(self):
        return self.subject_visit.natural_key()
    natural_key.dependencies = ['ambition_subject.subjectvisit']

    class Meta(VisitTrackingCrfModelMixin.Meta, RequiresConsentMixin.Meta):
        consent_model = 'ambition_subject.subjectconsent'
        abstract = True
