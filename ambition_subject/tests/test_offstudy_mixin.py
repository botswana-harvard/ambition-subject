from ambition_rando.import_randomization_list import import_randomization_list
from ambition_subject.models.subject_visit import SubjectVisit
from django.test import TestCase
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy


class TestOffStudyMixin(TestCase):

    def setUp(self):
        import_randomization_list(verbose=False)
        screening = mommy.make_recipe('ambition_subject.subjectscreening',
                                      report_datetime=get_utcnow())
        self.consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            consent_datetime=get_utcnow(),
            screening_identifier=screening.screening_identifier)

        self.appointment = Appointment.objects.get(
            visit_code='1000', subject_identifier=self.consent.subject_identifier)
        self.subject_visit = mommy.make_recipe(
            'ambition_subject.subjectvisit',
            appointment=self.appointment,
            reason=SCHEDULED)

    def test_is_eligible_after_blood_result(self):
        self.subject_visit = SubjectVisit.objects.get(
            subject_identifier=self.consent.subject_identifier,
            visit_code='1000')
        obj = mommy.make_recipe(
            'ambition_subject.bloodresult',
            subject_visit=self.subject_visit)
        self.assertTrue(obj)
        self.assertTrue(obj.is_eligible_after_blood_result())

    def test_is_eligible_after_blood_result_1(self):
        self.subject_visit = SubjectVisit.objects.get(
            subject_identifier=self.consent.subject_identifier,
            visit_code='1000')
        obj = mommy.make_recipe(
            'ambition_subject.bloodresult',
            subject_visit=self.subject_visit,
            absolute_neutrophil=55,
            alt=199,
            platelets=5451)
        self.assertFalse(obj.neutrophils_result(obj=obj))
        self.assertFalse(obj.platelets_result(obj=obj))
        self.assertFalse(obj.alt_result(obj=obj))

    def test_is_eligible_after_blood_result_neutrophils(self):
        self.subject_visit = SubjectVisit.objects.get(
            subject_identifier=self.consent.subject_identifier,
            visit_code='1000')
        obj = mommy.make_recipe(
            'ambition_subject.bloodresult',
            subject_visit=self.subject_visit,
            absolute_neutrophil=50,
            alt=201,
            platelets=5000)
        self.assertTrue(obj.neutrophils_result(obj=obj))
        self.assertTrue(obj.platelets_result(obj=obj))
        self.assertTrue(obj.alt_result(obj=obj))
