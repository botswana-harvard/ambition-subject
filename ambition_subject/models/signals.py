from ambition_rando.randomizer import Randomizer
from ambition_screening.models import SubjectScreening
from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from .subject_consent import SubjectConsent
from .subject_visit import SubjectVisit


@receiver(post_save, weak=False, sender=SubjectConsent,
          dispatch_uid='subject_consent_on_post_save')
def subject_consent_on_post_save(sender, instance, raw, created, **kwargs):
    """Creates an onschedule instance for this consented subject, if
    it does not exist.
    """
    if not raw:
        if not created:
            visit_schedule = site_visit_schedules.get_visit_schedule(
                'visit_schedule')
            schedule = visit_schedule.schedules.get('schedule')
            schedule.refresh_schedule(
                subject_identifier=instance.subject_identifier)
        else:
            subject_screening = SubjectScreening.objects.get(
                screening_identifier=instance.screening_identifier)
            subject_screening.subject_identifier = instance.subject_identifier
            subject_screening.consented = True
            subject_screening.save_base(
                update_fields=['subject_identifier', 'consented'])

            # put subject on schedule
            visit_schedule = site_visit_schedules.get_visit_schedule(
                'visit_schedule')
            schedule = visit_schedule.schedules.get('schedule')
            schedule.put_on_schedule(
                subject_identifier=instance.subject_identifier,
                consent_identifier=instance.consent_identifier,
                onschedule_datetime=instance.consent_datetime)

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
def subject_consent_on_post_delete(sender, instance, using, **kwargs):
    """Updates/Resets subject screening.
    """
    # don't allow if subject visits exist. This should be caught
    # in the ModelAdmin delete view
    if SubjectVisit.objects.filter(subject_identifier=instance.subject_identifier).exists():
        raise ValidationError('Unable to delete consent. Visit data exists.')

    # remove onschedule model
    visit_schedule = site_visit_schedules.get_visit_schedule(
        'visit_schedule')
    schedule = visit_schedule.schedules.get('schedule')
    onschedule_model_cls = django_apps.get_model(schedule.onschedule_model)
    onschedule_model_cls.objects.filter(
        subject_identifier=instance.subject_identifier).delete()

    # update subject screening
    subject_screening = SubjectScreening.objects.get(
        screening_identifier=instance.screening_identifier)
    subject_screening.consented = False
    subject_screening.subject_identifier = subject_screening.subject_screening_as_pk
    subject_screening.save()
