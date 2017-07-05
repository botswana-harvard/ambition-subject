from dateutil.relativedelta import relativedelta
from django.test import TestCase, tag
from model_mommy import mommy

from edc_base.utils import get_utcnow
from edc_constants.constants import YES
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.models import CrfMetadata
from edc_visit_tracking.constants import SCHEDULED

from ..models import Appointment


class TestSubjectRules(TestCase):

    def setUp(self):
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

    @tag('s')
    def test_adverse_event_required(self):
        print('>>>>>>>>>>>>>>>>', CrfMetadata.objects.all())
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseevent',
                subject_identifier=self.subject_identifier).entry_status,
            NOT_REQUIRED)
        prnmodel = mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            adverse_event=YES)
        print(prnmodel.__dict__)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseevent',
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
