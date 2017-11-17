from django.test import TestCase, tag

from ..eligibility import EarlyWithdrawalEvaluator


@tag('5')
class TestEarlyWithdrawalEvaluator(TestCase):

    def test_early_withdrawal_criteria_no(self):
        opts = dict(alt=None, pmns=None, platlets=None)
        obj = EarlyWithdrawalEvaluator(**opts)
        self.assertFalse(obj.eligible)

    def test_early_withdrawal_criteria_with_none(self):
        opts = dict(alt=None, pmns=None, platlets=None, allow_none=True)
        obj = EarlyWithdrawalEvaluator(**opts)
        self.assertTrue(obj.eligible)

    def test_early_withdrawal_criteria_ok(self):
        opts = dict(alt=200, pmns=500, platlets=50, allow_none=True)
        obj = EarlyWithdrawalEvaluator(**opts)
        self.assertTrue(obj.eligible)
