from ambition_rando.randomizer import Randomizer
from ambition_screening.models import SubjectScreening
from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from ..constants import CONSENT_WITHDRAWAL
from .enrollment import Enrollment
from .subject_consent import SubjectConsent
from . import StudyTerminationConclusion, SubjectOffstudy

post_delete.providing_args = set(["instance", "using", "raw"])


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
            subject_screening.subject_identifier = instance.subject_identifier
            subject_screening.consented = True
            subject_screening.save_base(
                update_fields=['subject_identifier', 'consented'])

            # randomize
            randomizer = Randomizer(
                subject_identifier=instance.subject_identifier,
                report_datetime=instance.consent_datetime,
                study_site=instance.study_site,
                user=instance.user_created)

            # create prescription
            prescription_model_cls = django_apps.get_model(
                'edc_pharmacy.prescription')
            prescription_model_cls.objects.create(
                subject_identifier=randomizer.model_obj.subject_identifier,
                rando_sid=randomizer.model_obj.sid,
                rando_arm=randomizer.model_obj.drug_assignment)


@receiver(post_save, weak=False, sender=StudyTerminationConclusion,
          dispatch_uid='study_termination_conclusion_on_post_save')
def study_termination_conclusion_on_post_save(sender, instance, raw, created, **kwargs):
    if instance.termination_reason != CONSENT_WITHDRAWAL:
        try:
            SubjectOffstudy.objects.get(
                subject_identifier=instance.subject_identifier)
        except ObjectDoesNotExist:
            offstudy_obj = SubjectOffstudy(
                subject_identifier=instance.subject_identifier,
                offstudy_datetime=instance.created,
                reason=instance.termination_reason)
            offstudy_obj.save()


# @receiver(post_save, weak=False, sender=PatientHistory,
#           dispatch_uid='patient_history_on_post_save')
# def patient_history_on_post_save(sender, instance, raw, created, **kwargs):
#     if not raw:
#         # subject_randomization must exist
#         subject_randomization = SubjectRandomization.objects.get(
#             subject_identifier=instance.subject_identifier)
#         # update weight on prescription
#         prescription_model_cls = django_apps.get_model(
#             'edc_pharmacy.prescription')
#         prescription = prescription_model_cls.objects.get(
#             subject_identifier=subject_randomization.subject_identifier,
#             rando_sid=subject_randomization.sid)
#         prescription.weight = instance.weight
#         prescription.save()


@receiver(post_delete, weak=False, sender=SubjectConsent,
          dispatch_uid="subject_consent_on_post_delete")
def subject_consent_on_post_delete(sender, instance, raw, using, **kwargs):
    if not raw:
        subject_screening = SubjectScreening.objects.get(
            screening_identifier=instance.screening_identifier)
        subject_screening.consented = False
        subject_screening.subject_identifier = subject_screening.subject_screening_as_pk
        subject_screening.save()
