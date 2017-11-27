

class EarlyWithdrawalEvaluator:

    def __init__(self, alt=None, pmn=None, platlets=None, allow_none=None):
        self.reasons_ineligible = {}
        if (not alt and not pmn and not platlets and allow_none):
            self.eligible = True
        elif not alt and not pmn and not platlets and not allow_none:
            self.eligible = False
        else:
            failed = []
            if alt and int(alt) > 200:
                self.reasons_ineligible.update(alt='ALT>200 IU/mL.')
                failed.append(1)
            if pmn and float(pmn) < 0.5:
                self.reasons_ineligible.update(pmns='PMNs<0.5x10^9/L.')
                failed.append(1)
            if platlets and int(platlets) < 50:
                self.reasons_ineligible.update(platlets='Platelets<50x10^9/L.')
                failed.append(1)
            self.eligible = True if not failed else False
