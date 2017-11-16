from django.test import TestCase, tag
from edc_constants.constants import FEMALE

from ..eligibility import Eligibility, EligibilityError
from copy import copy


@tag('2')
class TestEligibility(TestCase):

    def setUp(self):
        self.evaluator_criteria = dict(
            age=18,
            gender=FEMALE,
            pregnant=False,
            breast_feeding=False,
            alt=None,
            pmn=None,
            platlets=None)

        self.criteria = dict(
            consent_ability=True,
            meningitis_dx=True,
            not_mentally_abnormal=True,
            no_amphotericin=True,
            no_concomitant_meds=True,
            no_drug_reaction=True,
            no_fluconazole=True,
            will_hiv_test=True)

    def test_eligibility_without_criteria(self):
        self.assertRaises(
            EligibilityError,
            Eligibility)

    def test_eligibility_ok(self):
        obj = Eligibility(**self.evaluator_criteria, **self.criteria)
        self.assertTrue(obj.eligible)
        self.assertIsNone(obj.reasons_ineligible)

    def test_not_eligible(self):
        criteria = copy(self.criteria)
        criteria.update(no_amphotericin=False)
        for k in self.criteria:
            criteria = copy(self.criteria)
            criteria.update({k: False})
            obj = Eligibility(**self.evaluator_criteria, **criteria)
            self.assertFalse(obj.eligible)
            self.assertIn(k, obj.reasons_ineligible)
