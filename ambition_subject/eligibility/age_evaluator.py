from django.apps import apps as django_apps


class AgeEvaluator:

    def __init__(self, age=None, adult_lower=None, adult_upper=None, **kwargs):
        app_config = django_apps.get_app_config('ambition_subject')
        adult_lower = adult_lower or app_config.screening_age_adult_lower
        adult_upper = adult_upper or app_config.screening_age_adult_upper

        self.eligible = False
        self.reasons_ineligible = None
        try:
            if adult_lower <= age <= adult_upper:
                self.eligible = True
        except TypeError:
            self.reasons_ineligible = f'{age} is an invalid age.'
        if not self.eligible and age:
            if age < adult_lower:
                self.reasons_ineligible = f'age<{adult_lower}.'
            elif age > adult_upper:
                self.reasons_ineligible = f'age>{adult_upper}.'
