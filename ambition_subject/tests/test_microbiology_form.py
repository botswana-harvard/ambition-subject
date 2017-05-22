from django.test import TestCase
from model_mommy import mommy

from edc_base.utils import get_utcnow
from edc_constants.constants import NO, NOT_APPLICABLE, OTHER, POS, YES
from edc_visit_tracking.constants import SCHEDULED

from ..constants import HISTOPATHOLOGY_REPORT, VIBRIO
from ..forms import MicrobiologyForm
from ..models import Appointment


class TestMicrobiology(TestCase):

    def setUp(self):
        screening = mommy.make_recipe('ambition_subject.subject_screening')
        consent = mommy.make_recipe(
            'ambition_subject.subject_consent',
            consent_datetime=get_utcnow,
            subject_screening=screening)
        appointment = Appointment.objects.get(
            visit_code='1000')
        subject_visit = mommy.make_recipe(
            'ambition_subject.subjectvisit',
            appointment=appointment,
            subject_identifier=consent.subject_identifier, reason=SCHEDULED,)

        self.data = {
            'subject_visit': subject_visit.id,
            'report_datetime': get_utcnow(),
            'urine_culture_performed': YES,
            'urine_culture_results': POS,
            'urine_culture_organism': OTHER,
            'urine_culture_organism_other': VIBRIO,
            'blood_culture_performed': YES,
            'blood_culture_results': POS,
            'study_day_positive_blood_taken': 28,
            'blood_culture_organism': OTHER,
            'blood_culture_organism_other': VIBRIO,
            'sputum_results_afb': POS,
            'sputum_results_culture': POS,
            'sputum_results_if_positive': VIBRIO,
            'sputum_result_genexpert': POS,
            'tissue_biopsy_taken': YES,
            'tissue_biopsy_results': POS,
            'tissue_biopsy_organism': OTHER,
            'tissue_biopsy_organism_other': VIBRIO,
            'histopathology_report': HISTOPATHOLOGY_REPORT,
            'study_day_positive_biopsy_taken': 7}

    def test_valid_form(self):
        form = MicrobiologyForm(data=self.data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_urine_culture_no_results_invalid(self):
        self.data.update(urine_culture_results=NOT_APPLICABLE)
        form = MicrobiologyForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_urine_culture_no_organism_invalid(self):
        self.data.update(urine_culture_organism=NOT_APPLICABLE,
                         urine_culture_organism_other=None)
        form = MicrobiologyForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_urine_culture_no_organism_other_invalid(self):
        self.data.update(urine_culture_organism=OTHER,
                         urine_culture_organism_other=None)
        form = MicrobiologyForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_urine_culture_not_performed_valid(self):
        self.data.update(urine_culture_performed=NO,
                         urine_culture_results=NOT_APPLICABLE,
                         urine_culture_organism=NOT_APPLICABLE,
                         urine_culture_organism_other=None)
        form = MicrobiologyForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_blood_culture_no_results_invalid(self):
        self.data.update(blood_culture_results=NOT_APPLICABLE)
        form = MicrobiologyForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_blood_culture_no_study_day_invalid(self):
        self.data.update(study_day_positive_blood_taken=NOT_APPLICABLE)
        form = MicrobiologyForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_blood_culture_no_organism_invalid(self):
        self.data.update(blood_culture_organism=NOT_APPLICABLE,
                         blood_culture_organism_other=None)
        form = MicrobiologyForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_blood_culture_no_organism_other_invalid(self):
        self.data.update(blood_culture_organism=OTHER,
                         blood_culture_organism_other=None)
        form = MicrobiologyForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_blood_culture_not_performed_valid(self):
        self.data.update(blood_culture_performed=NO,
                         blood_culture_results=NOT_APPLICABLE,
                         blood_culture_organism=NOT_APPLICABLE,
                         blood_culture_organism_other=None,
                         study_day_positive_blood_taken=None)
        form = MicrobiologyForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_tissue_biopsy_no_results_invalid(self):
        self.data.update(tissue_biopsy_results=None)
        form = MicrobiologyForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_tissue_biopsy_no_organism_invalid(self):
        self.data.update(tissue_biopsy_organism=None,
                         tissue_biopsy_organism_other=None)
        form = MicrobiologyForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_tissue_biopsy_no_organism_other_invalid(self):
        self.data.update(tissue_biopsy_organism=OTHER,
                         tissue_biopsy_organism_other=None)
        form = MicrobiologyForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_tissue_biopsy_not_taken_valid(self):
        self.data.update(tissue_biopsy_taken=NO,
                         tissue_biopsy_results=NOT_APPLICABLE,
                         tissue_biopsy_organism=NOT_APPLICABLE,
                         tissue_biopsy_organism_other=None,
                         study_day_positive_biopsy_taken=None)
        form = MicrobiologyForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_biopsy_culture_no_study_day_invalid(self):
        self.data.update(tissue_biopsy_results=POS,
                         study_day_positive_biopsy_taken=None)
        form = MicrobiologyForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_pos_sputum_no_results_invalid(self):
        self.data.update(sputum_results_culture=POS,
                         sputum_results_if_positive=None)
        form = MicrobiologyForm(data=self.data)
        self.assertFalse(form.is_valid())
