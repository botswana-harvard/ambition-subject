
class EarlyWithdrawalEvaluator:

    def __init__(self, alt=None, pmns=None, platlets=None, allow_none=None, **kwargs):
        reasons_ineligible = {}
        self.eligible = False
        if not alt and not pmns and not platlets and allow_none:
            self.eligible = True
        else:
            self.eligible = True
            if alt and int(alt) > 200:
                reasons_ineligible.update(alt='ALT>200 IU/mL.')
                self.eligible = False
            if pmns and int(pmns) < 500:
                reasons_ineligible.update(pmns='PMNs<500x10^6/L.')
                self.eligible = False
            if platlets and int(platlets) < 50:
                reasons_ineligible.update(platlets='Platelets<50x10^9/L.')
                self.eligible = False
        if not self.eligible:
            self.reasons_ineligible = ','.join(
                [v for v in reasons_ineligible.values()])
        else:
            self.reasons_ineligible = None
