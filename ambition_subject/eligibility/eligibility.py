from .age_evaluator import AgeEvaluator
from .gender_evaluator import GenderEvaluator
from ambition_subject.eligibility.early_withdrawal_evaluator import EarlyWithdrawalEvaluator


class EligibilityError(Exception):
    pass


class Eligibility:

    """Eligible if all criteria evaluate True.

    Any key in kwargs has value True if eligible.
    """

    def __init__(self, age=None, gender=None, pregnant=None, breast_feeding=None,
                 alt=None, pmn=None, platlets=None, **kwargs):

        self.reasons_ineligible = None

        self.age_evaluator = AgeEvaluator(age=age)
        self.gender_evaluator = GenderEvaluator(
            gender=gender, pregnant=pregnant, breast_feeding=breast_feeding)
        self.early_withdrawal_evaluator = EarlyWithdrawalEvaluator(
            alt=alt, pmn=pmn, platlets=platlets)

        self.criteria = dict(**kwargs)
        if len(self.criteria) == 0:
            raise EligibilityError('No criteria provided.')

        self.criteria.update(age=self.age_evaluator.eligible)
        self.criteria.update(gender=self.gender_evaluator.eligible)
        self.criteria.update(
            early_withdrawal=self.early_withdrawal_evaluator.eligible)

        # eligible if all criteria are True
        self.eligible = all([v for v in self.criteria.values()])

        if not self.eligible:
            self.reasons_ineligible = {
                k: v for k, v in self.criteria.items() if not v}
            self.reasons_ineligible.update(
                age=self.age_evaluator.reasons_ineligible)
            self.reasons_ineligible.update(
                gender=self.gender_evaluator.reasons_ineligible)
            self.reasons_ineligible.update(
                early_withdrawal=self.early_withdrawal_evaluator.reasons_ineligible)
            for k, v in self.custom_reasons_dict.items():
                if v:
                    self.reasons_ineligible.update({k: v})

    def __str__(self):
        return self.eligible

    @property
    def custom_reasons_dict(self):
        """Returns a dictionary of custom reasons for named criteria.
        """
        custom_reasons_dict = dict(
            no_drug_reaction='Previous adverse drug reaction to the study medication.',
            no_concomitant_meds='Patient on Contraindicated Meds.',
            meningitis_dx='Previous Hx of Cryptococcal Meningitis.',
            no_amphotericin='> 0.7mg/kg of Amphotericin B.',
            no_fluconazole='> 48hrs of Fluconazole.',
            will_hiv_test='HIV unknown, not willing to consent.')
        for k in custom_reasons_dict:
            if k in custom_reasons_dict and k not in self.criteria:
                raise EligibilityError(
                    f'Custom reasons refer to invalid named criteria, Got \'{k}\'. '
                    f'Expected one of {list(self.criteria)}. '
                    f'See {repr(self)}.')
        return custom_reasons_dict
