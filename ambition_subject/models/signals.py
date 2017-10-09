from ambition_rando.randomizer import Randomizer
from edc_base.utils import get_utcnow
from edc_pharma.scheduler import DispensePlanScheduler

from django.db.models.signals import post_save
from django.dispatch import receiver

from .enrollment import Enrollment
from .subject_consent import SubjectConsent
from .subject_screening import SubjectScreening


@receiver(post_save, weak=False, sender=SubjectConsent,
          dispatch_uid='subject_consent_on_post_save')
def subject_consent_on_post_save(sender, instance, raw, created, **kwargs):
    """Creates an enrollment instance for this consented subject, if
    it does not exist.
    """
    if not raw:
        if created:
            subject_screening = SubjectScreening.objects.get(
                screening_identifier=instance.screening_identifier)
            try:
                Enrollment.objects.get(
                    subject_identifier=instance.subject_identifier,
                    visit_schedule_name=Enrollment._meta.visit_schedule_name)
            except Enrollment.DoesNotExist:
                Enrollment.objects.create(
                    subject_identifier=instance.subject_identifier,
                    consent_identifier=instance.consent_identifier,
                    is_eligible=subject_screening.eligible)
            obj = Randomizer(subject_consent=instance,
                             randomization_datetime=get_utcnow())
            subject_screening.subject_identifier = instance.subject_identifier
            subject_screening.save_base(update_fields=['subject_identifier'])
            DispensePlanScheduler(
                obj.history_obj, arm=obj.history_obj.rx).create_schedules()
