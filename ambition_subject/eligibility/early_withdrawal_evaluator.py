
class EarlyWithdrawalEvaluator:

    def __init__(self, alt=None, pmns=None, platlets=None, **kwargs):
        reasons_ineligible = {}
        self.eligible = True
        if alt and alt > 200:
            reasons_ineligible.update(alt='ALT>200 IU/mL.')
            self.eligible = False
        if pmns and pmns < 500:
            reasons_ineligible.update(pmns='PMNs<500x10^6/L.')
            self.eligible = False
        if platlets and platlets < 50:
            reasons_ineligible.update(platlets='Platelets<50x10^9/L.')
            self.eligible = False
        if reasons_ineligible:
            self.reasons_ineligible = ','.join([v for v in reasons_ineligible])
        else:
            self.reasons_ineligible = None
