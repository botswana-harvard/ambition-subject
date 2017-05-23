from django.test import TestCase, tag
from model_mommy import mommy

from edc_base.utils import get_utcnow
from edc_visit_tracking.constants import SCHEDULED

from ..forms import Week2Form
from ..models import Week2, Appointment


class TestWeek2Form(TestCase):

    def setUp(self):
        screening = mommy.make_recipe(
            'ambition_screening.subjectscreening',
            report_datetime=get_utcnow())
        consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            consent_datetime=get_utcnow(),
            subject_screening=screening)
        appointment = Appointment.objects.get(
            visit_code='1000')
        self.subject_visit = mommy.make_recipe(
            'ambition_subject.subjectvisit',
            appointment=appointment,
            subject_identifier=consent.subject_identifier,
            reason=SCHEDULED,)

    @tag('w2')
    def test_default_mommy_recipe(self):
        obj = mommy.prepare_recipe(
            'ambition_subject.week2', subject_visit=self.subject_visit)
        form = Week2Form(data=obj.__dict__)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())
