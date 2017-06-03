from django.test import TestCase, tag
from model_mommy import mommy

from edc_base.utils import get_utcnow
from edc_visit_tracking.constants import SCHEDULED

from ..forms import BloodResultForm
from ..models import Appointment


class TestBloodResultForm(TestCase):

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

    def test_default_mommy_recipe(self):
        """
        Assert that the form will save
        """
        obj = mommy.prepare_recipe(
            'ambition_subject.bloodresult', subject_visit=self.subject_visit)
        data = obj.__dict__
        del data['subject_visit_id']
        data.update({'subject_visit': self.subject_visit.id})
        form = BloodResultForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())
