
class EarlyWithdrawalEvaluator:

    def __init__(self, alt=None, pmns=None, platlets=None, allow_none=None, **kwargs):
        self.reasons_ineligible = {}
        if (not alt and not pmns and not platlets and allow_none):
            self.eligible = True
        elif not alt and not pmns and not platlets and not allow_none:
            self.eligible = False
        else:
            failed = []
            if alt and int(alt) > 200:
                self.reasons_ineligible.update(alt='ALT>200 IU/mL.')
                failed.append(1)
            if pmns and int(pmns) < 500:
                self.reasons_ineligible.update(pmns='PMNs<500x10^6/L.')
                failed.append(1)
            if platlets and int(platlets) < 50:
                self.reasons_ineligible.update(platlets='Platelets<50x10^9/L.')
                failed.append(1)
            self.eligible = True if not failed else False
