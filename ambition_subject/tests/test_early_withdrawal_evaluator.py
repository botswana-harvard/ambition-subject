from django.test import TestCase, tag
from edc_constants.constants import YES, NO

from ..constants import RESULTS_UNKNOWN

from ..eligibility import EarlyWithdrawalEvaluator


@tag('2')
class TestEarlyWithdrawalEvaluator(TestCase):

    def test_early_withdrawal_criteria_no(self):
        opts = dict(alt=None, pmns=None, platlets=None)
        obj = EarlyWithdrawalEvaluator(**opts)
        self.assertFalse(obj.eligible)

    def test_early_withdrawal_criteria_results_unknown(self):
        withdrawal_criteria = EarlyWithdrawalEvaluator(
            withdrawal_criteria=RESULTS_UNKNOWN)
        self.assertTrue(withdrawal_criteria.eligible)

    def test_early_withdrawal_criteria_yes(self):
        withdrawal_criteria = EarlyWithdrawalEvaluator(
            withdrawal_criteria=YES)
        self.assertFalse(withdrawal_criteria.eligible)
