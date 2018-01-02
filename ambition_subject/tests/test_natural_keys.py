from ambition_rando.tests import AmbitionTestCaseMixin
from ambition_visit_schedule import DAY1
from django.test import TestCase, tag
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_metadata.tests import CrfTestHelper
from edc_sync.tests import SyncTestHelper
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy
from unittest.case import skip


@skip
class TestNaturalKey(AmbitionTestCaseMixin, TestCase):

    sync_test_helper = SyncTestHelper()
    crf_test_helper = CrfTestHelper()

    def test_natural_key_attrs(self):
        self.sync_test_helper.sync_test_natural_key_attr(
            'ambition_subject')

    def test_get_by_natural_key_attr(self):
        self.sync_test_helper.sync_test_get_by_natural_key_attr(
            'ambition_subject')

    def complete_subject_visit(self):
        screening = mommy.make_recipe('ambition_screening.subjectscreening',
                                      report_datetime=get_utcnow())
        consent = mommy.make_recipe('ambition_subject.subjectconsent',
                                    consent_datetime=get_utcnow(),
                                    screening_identifier=screening.screening_identifier)
        self.subject_identifier = consent.subject_identifier
        self.subject_visit = mommy.make_recipe(
            'ambition_subject.subjectvisit',
            appointment=Appointment.objects.get(
                subject_identifier=self.subject_identifier, visit_code=DAY1),
            subject_identifier=consent.subject_identifier,
            reason=SCHEDULED,)
        return self.subject_visit

    def test_sync_test_natural_keys(self):
        complete_required_crfs = {}
        visit = self.complete_subject_visit()
        complete_required_crfs.update({
            visit.visit_code: self.crf_test_helper.complete_required_crfs(
                visit_code=visit.visit_code,
                visit=visit,
                subject_identifier=visit.subject_identifier)
        })
        self.sync_test_helper.sync_test_natural_keys(
            complete_required_crfs, verbose=True)
