from django.test import TestCase, tag
from model_mommy import mommy

from edc_base.utils import get_utcnow
from edc_constants.constants import YES
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.models import CrfMetadata
from edc_visit_tracking.constants import SCHEDULED

from ..models import Appointment


@tag('rg')
class TestSubjectRules(TestCase):

    def setUp(self):
        screening = mommy.make_recipe('ambition_screening.subjectscreening',
                                      report_datetime=get_utcnow())
        self.consent = mommy.make_recipe('ambition_subject.subjectconsent',
                                         consent_datetime=get_utcnow(),
                                         subject_screening=screening)
        self.subject_identifier = self.consent.subject_identifier
        self.subject_visit = mommy.make_recipe(
            'ambition_subject.subjectvisit',
            appointment=Appointment.objects.get(
                subject_identifier=self.subject_identifier, visit_code='1028'),
            subject_identifier=self.consent.subject_identifier,
            reason=SCHEDULED,)

    def test_adverse_event_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseevent',
                subject_identifier=self.subject_identifier).entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            adverse_event=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseevent',
                subject_identifier=self.subject_identifier).entry_status,
            REQUIRED)

    def test_adverse_event_tmg_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseeventtmg',
                subject_identifier=self.subject_identifier).entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            adverse_event_tmg=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseeventtmg',
                subject_identifier=self.subject_identifier).entry_status,
            REQUIRED)

    def test_adverse_event_followup_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseeventfollowup',
                subject_identifier=self.subject_identifier).entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            adverse_event_followup=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseeventfollowup',
                subject_identifier=self.subject_identifier).entry_status,
            REQUIRED)

    def test_microbiology_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.microbiology').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            microbiology=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.microbiology').entry_status,
            REQUIRED)

    def test_radiology_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.radiology').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            radiology=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.radiology').entry_status,
            REQUIRED)

    def test_lumbar_puncture_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.lumbarpuncturecsf').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            lumbar_puncture=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.lumbarpuncturecsf').entry_status,
            REQUIRED)

    def test_recurrence_symptom_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.recurrencesymptom').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            recurrence_symptom=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.recurrencesymptom').entry_status,
            REQUIRED)

    def test_protocol_deviation_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.protocoldeviationviolation').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            protocol_deviation=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.protocoldeviationviolation').entry_status,
            REQUIRED)

    def test_death_report_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreport').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            death_report=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreport').entry_status,
            REQUIRED)

    def test_death_report_required_from_adverse_event(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreport').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            adverse_event=YES)
        mommy.make_recipe(
            'ambition_subject.adverseevent',
            subject_visit=self.subject_visit,
            ae_severity_grade='grade_5')
