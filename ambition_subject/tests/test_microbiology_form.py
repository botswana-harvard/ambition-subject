from django.test import TestCase

from edc_constants.constants import YES, NO, OTHER

from ..constants import HISTOPATHOLOGY_REPORT, POSITIVE, VIBRIO
from ..forms import MicrobiologyForm


class TestMicrobiology(TestCase):

    def setUp(self):

        self.data = {
            'urine_culture_performed': YES,
            'urine_culture_results': POSITIVE,
            'urine_culture_organism': OTHER,
            'urine_culture_organism_other': VIBRIO,
            'blood_culture_performed': YES,
            'blood_culture_results': POSITIVE,
            'study_day_positive_blood_taken': 28,
            'blood_culture_organism': OTHER,
            'blood_culture_organism_other': VIBRIO,
            'sputum_results_afb': POSITIVE,
            'sputum_results_culture': POSITIVE,
            'sputum_results_if_positive': VIBRIO,
            'sputum_result_genexpert': POSITIVE,
            'tissue_biopsy_taken': YES,
            'tissue_biopsy_results': POSITIVE,
            'study_day_positive_biopsy_taken': 28,
            'tissue_biopsy_organism': OTHER,
            'tissue_biopsy_organism_other': VIBRIO,
            'histopathology_report': HISTOPATHOLOGY_REPORT}

    def test_valid_form(self):
        form = MicrobiologyForm(data=self.data)
        self.assertTrue(form.is_valid())
