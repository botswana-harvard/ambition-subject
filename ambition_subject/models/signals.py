from ambition_rando.models import SubjectRandomization
from ambition_rando.randomizer import Randomizer
from ambition_subject.constants import CONTROL, SINGLE_DOSE
from ambition_subject.models.patient_history import PatientHistory
from edc_base.utils import get_utcnow
from edc_pharma import AppointmentDescriber
from edc_pharma.dispense import PrescriptionCreator
from edc_pharma.models.worklist import WorkList
from edc_pharma.scheduler import Scheduler
from edc_registration.models import RegisteredSubject

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
            Randomizer(subject_consent=instance,
                       randomization_datetime=get_utcnow())
            subject_screening.subject_identifier = instance.subject_identifier
            subject_screening.save_base(update_fields=['subject_identifier'])


@receiver(post_save, weak=False, sender=PatientHistory,
          dispatch_uid='patient_history_on_post_save')
def patient_history_on_post_save(sender, instance, raw, created, **kwargs):
    """Creates an enrollment instance for this consented subject, if
    it does not exist.
    """
    if not raw:
        if created:
            subject_randomization = SubjectRandomization.objects.get(
                subject_identifier=instance.subject_identifier)
            if subject_randomization.rx in [CONTROL, SINGLE_DOSE]:
                scheduler = Scheduler(
                    subject_identifier=subject_randomization.subject_identifier,
                    randomization_datetime=subject_randomization.randomization_datetime,
                    arm=subject_randomization.rx
                )
                appt = scheduler.dispense_appointments[0]
                try:
                    WorkList.objects.get(
                        subject_identifier=subject_randomization.subject_identifier)
                except WorkList.DoesNotExist:
                    WorkList.objects.create(
                        subject_identifier=subject_randomization.subject_identifier,
                        report_datetime=instance.created,
                        next_dispensing_datetime=appt.appt_datetime,
                        enrollment_datetime=subject_randomization.created,
                    )
                reg = RegisteredSubject.objects.get(
                    subject_identifier=subject_randomization.subject_identifier)
                options = dict(weight=instance.weight,
                               initials=reg.initials,
                               clinician_initials=appt.user_created[0:2].upper())
                for appointment in scheduler.dispense_appointments:
                    describer = AppointmentDescriber(
                        dispense_appointment=appointment)
                    options.update({'duration': describer.duration})
                    PrescriptionCreator(
                        dispense_appointment=appointment, options=options)
