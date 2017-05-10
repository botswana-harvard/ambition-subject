from django.test import tag, TestCase
from django.utils import timezone
from model_mommy import mommy

from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO, MALE
from edc_visit_tracking.constants import SCHEDULED

from ..constants import AMS_N3, SINGLE_DOSE
from ..forms import SubjectRandomizationForm

from ..models import Appointment


@tag('randomization')
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
        subject_visit = mommy.make_recipe(
            'ambition_subject.subjectvisit',
            appointment=appointment,
            subject_identifier=consent.subject_identifier,
            reason=SCHEDULED,)

        self.data = {
            'subject_visit': subject_visit,
            'age': 21,
            'sex': MALE,
            'is_of_age': YES,
            'meningitis_diagoses_by_csf_or_crag': YES,
            'consent_to_hiv_test': YES,
            'willing_to_give_informed_consent': YES,
            'pregrancy_or_lactation': YES,
            'previous_adverse_drug_reaction': NO,
            'medication_contraindicated_with_study_drug': NO,
            'two_days_amphotericin_b': NO,
            'two_days_fluconazole': YES,
            'patient_eligible': NO,
            'consent_given': YES,
            'hospital_admission_date': timezone.now().date(),
            'inclusion_date': timezone.now().date(),
            'abnormal_mental_status': YES,
            'already_on_arvs': YES,
            'arv_start_date': timezone.now().date(),
            'randomization_number': AMS_N3,
            'consent_form_signed': YES,
            'regimen': SINGLE_DOSE}

    def test_valid_form(self):
        form = SubjectRandomizationForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_arv_start_date_required(self):
        self.data.update(
            arv_start_date=None)
        form = SubjectRandomizationForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_arv_start_date_not_required(self):
        self.data.update(
            already_on_arvs=NO,
            arv_start_date=timezone.now().date())
        form = SubjectRandomizationForm(data=self.data)
        self.assertFalse(form.is_valid())
