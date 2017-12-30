from ambition_labs.labs import cd4_panel, viral_load_panel, fbc_panel
from ambition_subject.models.subject_visit import SubjectVisit
from ambition_visit_schedule import DAY1, DAY5, WEEK10
from django.test import TestCase, tag
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_constants.constants import YES
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.models import CrfMetadata, RequisitionMetadata
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy
from ambition_rando.tests.site_test_case_mixin import SiteTestCaseMixin


class TestSubjectRules(SiteTestCaseMixin, TestCase):

    def setUp(self):
        screening = mommy.make_recipe(
            'ambition_screening.subjectscreening',
            report_datetime=get_utcnow())
        self.consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            consent_datetime=get_utcnow(),
            screening_identifier=screening.screening_identifier)

        self.visit_code = WEEK10

        for appointment in Appointment.objects.all().order_by('timepoint'):
            self.subject_visit = mommy.make_recipe(
                'ambition_subject.subjectvisit',
                appointment=appointment,
                reason=SCHEDULED)
            if appointment.visit_code == self.visit_code:
                break

    def test_blood_result_required_prn_form(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.bloodresult',
                subject_identifier=self.consent.subject_identifier,
                visit_code=WEEK10).entry_status,
            NOT_REQUIRED)

        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            blood_result=YES)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.bloodresult',
                subject_identifier=self.consent.subject_identifier,
                visit_code=WEEK10).entry_status,
            REQUIRED)

    def test_microbiology_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.microbiology',
                subject_identifier=self.consent.subject_identifier,
                visit_code=WEEK10).entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            microbiology=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.microbiology',
                subject_identifier=self.consent.subject_identifier,
                visit_code=WEEK10).entry_status,
            REQUIRED)

    def test_radiology_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.radiology',
                subject_identifier=self.consent.subject_identifier,
                visit_code=WEEK10).entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            radiology=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.radiology',
                subject_identifier=self.consent.subject_identifier,
                visit_code=WEEK10).entry_status,
            REQUIRED)

    def test_lumbar_puncture_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.lumbarpuncturecsf',
                subject_identifier=self.consent.subject_identifier,
                visit_code=WEEK10).entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            lumbar_puncture=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.lumbarpuncturecsf',
                subject_identifier=self.consent.subject_identifier,
                visit_code=WEEK10).entry_status,
            REQUIRED)

    def test_medical_expenses_two_required(self):
        appointment = Appointment.objects.get(
            subject_identifier=self.consent.subject_identifier,
            visit_code=DAY1)
        self.subject_visit = SubjectVisit.objects.get(
            appointment=appointment)

        mommy.make_recipe(
            'ambition_subject.medicalexpenses',
            subject_visit=self.subject_visit,
            care_before_hospital=YES)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.medicalexpensestwo',
                subject_identifier=self.consent.subject_identifier,
                visit_code=DAY1).entry_status,
            REQUIRED)

    def test_viral_load_required(self):
        appointment = Appointment.objects.get(
            subject_identifier=self.consent.subject_identifier,
            visit_code=DAY5)
        self.subject_visit = SubjectVisit.objects.get(
            appointment=appointment)

        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            viral_load=YES)

        self.assertEqual(
            RequisitionMetadata.objects.get(
                model='ambition_subject.subjectrequisition',
                subject_identifier=self.consent.subject_identifier,
                panel_name=viral_load_panel.name,
                visit_code=DAY5).entry_status, REQUIRED)

    def test_cd4_required(self):
        appointment = Appointment.objects.get(
            subject_identifier=self.consent.subject_identifier,
            visit_code=DAY5)
        self.subject_visit = SubjectVisit.objects.get(
            appointment=appointment)

        self.assertEqual(
            RequisitionMetadata.objects.get(
                model='ambition_subject.subjectrequisition',
                subject_identifier=self.consent.subject_identifier,
                panel_name=cd4_panel.name,
                visit_code=DAY5).entry_status, NOT_REQUIRED)

        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            cd4=YES)

        self.assertEqual(
            RequisitionMetadata.objects.get(
                model='ambition_subject.subjectrequisition',
                subject_identifier=self.consent.subject_identifier,
                panel_name=cd4_panel.name,
                visit_code=DAY5).entry_status, REQUIRED)

    def test_cd4_rule_d1(self):
        appointment = Appointment.objects.get(
            subject_identifier=self.consent.subject_identifier,
            visit_code=DAY1)
        self.subject_visit = SubjectVisit.objects.get(
            appointment=appointment)

        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            cd4=YES)

        self.assertEqual(
            RequisitionMetadata.objects.get(
                model='ambition_subject.subjectrequisition',
                subject_identifier=self.consent.subject_identifier,
                panel_name=cd4_panel.name,
                visit_code=DAY1).entry_status, REQUIRED)

    def test_vl_required_d1(self):
        appointment = Appointment.objects.get(
            subject_identifier=self.consent.subject_identifier,
            visit_code=DAY1)
        self.subject_visit = SubjectVisit.objects.get(
            appointment=appointment)

        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            viral_load=YES)

        self.assertEqual(
            RequisitionMetadata.objects.get(
                model='ambition_subject.subjectrequisition',
                subject_identifier=self.consent.subject_identifier,
                panel_name=viral_load_panel.name,
                visit_code=DAY1).entry_status,
            REQUIRED)

    def test_fbc_required_d5(self):
        appointment = Appointment.objects.get(
            subject_identifier=self.consent.subject_identifier,
            visit_code=DAY5)
        self.subject_visit = SubjectVisit.objects.get(
            appointment=appointment)

        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            fbc=YES)

        self.assertEqual(
            RequisitionMetadata.objects.get(
                model='ambition_subject.subjectrequisition',
                subject_identifier=self.consent.subject_identifier,
                panel_name=fbc_panel.name,
                visit_code=DAY5).entry_status,
            REQUIRED)
