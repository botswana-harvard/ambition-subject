from ambition_rando.import_randomization_list import import_randomization_list
from django.test import TestCase, tag
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_constants.constants import YES
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy

from ..forms import MicrobiologyForm


class TestMicrobiologyForm(TestCase):

    def setUp(self):
        import_randomization_list(verbose=False)
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening')
        options = {
            'screening_identifier': subject_screening.screening_identifier,
            'consent_datetime': get_utcnow, }
        consent = mommy.make_recipe(
            'ambition_subject.subjectconsent', **options)
        self.subject_identifier = consent.subject_identifier
        self.subject_visit = mommy.make_recipe(
            'ambition_subject.subjectvisit',
            appointment=Appointment.objects.get(
                subject_identifier=self.subject_identifier, visit_code='1000'),
            subject_identifier=consent.subject_identifier,
            reason=SCHEDULED)

    def test_yes_blood_culture_performed_with_blood_culture_results(self):

        self.subject_visit.appointment.subject_identifier = '11111111'

        cleaned_data = {'subject_visit': self.subject_visit,
                        'blood_culture_performed': YES,
                        'blood_taken_date': get_utcnow().date(),
                        'blood_culture_results': 'no_growth'}
        form = MicrobiologyForm(data=cleaned_data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())
