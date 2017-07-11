from django.test import TestCase, tag
from model_mommy import mommy

from edc_base.utils import get_utcnow
from edc_sync.tests import SyncTestHelper
from edc_visit_tracking.constants import SCHEDULED

from ambition_subject.models.appointment import Appointment


@tag('TestNaturalKey')
class TestNaturalKey(TestCase):

    sync_test_helper = SyncTestHelper()

    @tag('natural_key')
    def test_natural_key_attrs(self):
        self.sync_test_helper.sync_test_natural_key_attr(
            'ambition_subject')

    @tag('natural_key')
    def test_get_by_natural_key_attr(self):
        self.sync_test_helper.sync_test_get_by_natural_key_attr(
            'ambition_subject')

    def complete_subject_visit(self):
        screening = mommy.make_recipe('ambition_screening.subjectscreening',
                                      report_datetime=get_utcnow())
        consent = mommy.make_recipe('ambition_subject.subjectconsent',
                                    consent_datetime=get_utcnow(),
                                    subject_screening=screening)
        self.subject_identifier = consent.subject_identifier
        self.subject_visit = mommy.make_recipe(
            'ambition_subject.subjectvisit',
            appointment=Appointment.objects.get(
                subject_identifier=self.subject_identifier, visit_code='1000'),
            subject_identifier=consent.subject_identifier,
            reason=SCHEDULED,)
        return self.subject_visit

    def test_sync_test_natural_keys_by_schedule(self):
        self.sync_test_helper.sync_test_natural_keys_by_schedule(
            visits=[self.complete_subject_visit()])
