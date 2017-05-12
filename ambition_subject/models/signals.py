from django.db.models.signals import post_save
from django.dispatch import receiver

from ambition_screening.models import SubjectScreening

from .subject_consent import SubjectConsent
from .enrollment import Enrollment


@receiver(post_save, weak=False, sender=SubjectConsent, dispatch_uid='subject_consent_on_post_save')
def subject_consent_on_post_save(sender, instance, raw, created, using, **kwargs):
    if not raw:
        if created:
            try:
                Enrollment.objects.create(
                    subject_identifier=instance.subject_identifier,
                    consent_identifier=instance.id,
                    is_eligible=instance.subject_screening.eligible)
            except SubjectScreening.DoesNotExist:
                raise('Valid subject screening id not found')
