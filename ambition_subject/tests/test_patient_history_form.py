from ambition_visit_schedule import DAY1
from ambition_rando.import_randomization_list import import_randomization_list
from django.test import TestCase, tag
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_constants.constants import NO
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy
from unittest.case import skip

from ..forms import PatientHistoryForm


class TestPatientHistoryFormValidator(TestCase):

    def setUp(self):
        import_randomization_list(verbose=False)
        subject_screening = mommy.make_recipe(
            'ambition_screening.subjectscreening')

        options = {
            'screening_identifier': subject_screening.screening_identifier,
            'consent_datetime': get_utcnow, }
        consent = mommy.make_recipe(
            'ambition_subject.subjectconsent', **options)
        self.subject_identifier = consent.subject_identifier
        self.subject_visit = mommy.make_recipe(
            'ambition_subject.subjectvisit',
            appointment=Appointment.objects.get(
                subject_identifier=self.subject_identifier, visit_code=DAY1),
            subject_identifier=consent.subject_identifier,
            reason=SCHEDULED,)

    @skip('fix this test')
    def test_tb_history_yes_tb_site_none_invalid(self):
        options = {'care_before_hospital': NO,
                   'subject_visit': self.subject_visit,
                   'report_datetime': get_utcnow()}
        mommy.make_recipe(
            'ambition_subject.patienthistory', **options)
        form = PatientHistoryForm()
        self.assertTrue(form.is_valid())
