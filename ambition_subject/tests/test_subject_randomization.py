from django.test import TestCase, tag
from model_mommy import mommy

from edc_base_test.utils import get_utcnow
from edc_constants.constants import YES, NO
from edc_visit_tracking.constants import SCHEDULED

from ..constants import AMS_A4
from ..models import Appointment


@tag('rando')
class TestSubjectRandomization(TestCase):

    def setUp(self):
        screening = mommy.make_recipe(
            'ambition_subject.subject_screening',
            report_datetime=get_utcnow())
        consent = mommy.make_recipe(
            'ambition_subject.subject_consent',
            consent_datetime=get_utcnow(),
            subject_screening=screening)
        appointment = Appointment.objects.get(
            visit_code='1000')
        self.subject_visit = mommy.make_recipe(
            'ambition_subject.subjectvisit',
            appointment=appointment,
            subject_identifier=consent.subject_identifier,
            reason=SCHEDULED)

    def test_subject_on_art_normal_mental_status(self):

        rando = mommy.make_recipe(
            'ambition_subject.subject_randomization',
            subject_visit=self.subject_visit,
            abnormal_mental_status=YES, on_arvs=YES)
        self.assertEqual(rando.rando_category, AMS_A4)
