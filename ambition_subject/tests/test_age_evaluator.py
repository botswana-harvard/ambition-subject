from django.apps import apps as django_apps
from django.test import TestCase, tag

from ..eligibility import AgeEvaluator


@tag('2')
class TestAgeEvaluator(TestCase):

    def setUp(self):
        django_apps.app_configs[
            'ambition_subject'].screening_age_adult_upper = 99
        django_apps.app_configs[
            'ambition_subject'].screening_age_adult_lower = 18

    def test_eligibility_invalid_age_in_years(self):
        age_evaluator = AgeEvaluator(age=17)
        self.assertFalse(age_evaluator.eligible)
        age_evaluator = AgeEvaluator(age=18)
        self.assertTrue(age_evaluator.eligible)
        age_evaluator = AgeEvaluator(age=99)
        self.assertTrue(age_evaluator.eligible)
        age_evaluator = AgeEvaluator(age=100)
        self.assertFalse(age_evaluator.eligible)

    def test_eligibility_invalid_age_in_years_reasons_ineligible(self):
        age_evaluator = AgeEvaluator(age=17)
        self.assertIn('age<18.', age_evaluator.reasons_ineligible)
        age_evaluator = AgeEvaluator(age=100)
        self.assertIn('age>99.', age_evaluator.reasons_ineligible)
