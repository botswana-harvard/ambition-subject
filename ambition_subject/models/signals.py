from django.apps import apps as django_apps
from ambition_rando.randomizer import Randomizer
from django.db.models.signals import post_save
from django.dispatch import receiver
from edc_base.utils import get_utcnow

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
            Randomizer(subject_consent=instance,
                       randomization_datetime=get_utcnow())
            subject_screening.subject_identifier = instance.subject_identifier
            subject_screening.save_base(update_fields=['subject_identifier'])


@receiver(post_save, weak=False, dispatch_uid="crf_metadata_update_on_post_save")
def crf_metadata_update_on_post_save(sender, instance, raw, created, using,
                                     update_fields, **kwargs):
    """Update the meta data record on post save of a model.
    """

    if not raw:
        try:
            instance.metadata_update()
            if django_apps.get_app_config('edc_metadata').metadata_rules_enabled:
                instance.run_metadata_rules()
        except AttributeError as e:
            if 'metadata_update' not in str(e):
                raise AttributeError(e) from e
