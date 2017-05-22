from dateutil.relativedelta import relativedelta

from django.test import TestCase, tag
from model_mommy import mommy


from edc_base.utils import get_utcnow
from edc_constants.constants import OTHER, NO, YES

from ..forms import ProtocolDeviationViolationForm
from ..models import ProtocolDeviationViolation


class TestProtocolDeviationViolation(TestCase):

    @tag('pdv')
    def test_default_mommy_recipe(self):
        obj = mommy.prepare_recipe(ProtocolDeviationViolation._meta.label_lower)
        form = ProtocolDeviationViolationForm(data=obj.__dict__)
        print(form.errors)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_safety_impact_no_details_invalid(self):
        obj = mommy.prepare_recipe(ProtocolDeviationViolation._meta.label_lower,
                                   participant_safety_impact=YES,
                                   participant_safety_impact_details=None)
        form = ProtocolDeviationViolationForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(ProtocolDeviationViolation._meta.label_lower,
                                   participant_safety_impact=YES,
                                   participant_safety_impact_details='blahblah')
        form = ProtocolDeviationViolationForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def test_study_impact_no_details_invalid(self):
        obj = mommy.prepare_recipe(ProtocolDeviationViolation._meta.label_lower,
                                   study_outcomes_impact=YES,
                                   study_outcomes_impact_details=None)
        form = ProtocolDeviationViolationForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(ProtocolDeviationViolation._meta.label_lower,
                                   study_outcomes_impact=YES,
                                   study_outcomes_impact_details='blahblah')
        form = ProtocolDeviationViolationForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def test_violation_type_no_details_invalid(self):
        obj = mommy.prepare_recipe(ProtocolDeviationViolation._meta.label_lower,
                                   protocol_violation_type=OTHER,
                                   other_protocol_violation_type=None)
        form = ProtocolDeviationViolationForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj = mommy.prepare_recipe(ProtocolDeviationViolation._meta.label_lower,
                                   protocol_violation_type=OTHER,
                                   other_protocol_violation_type='blahblah')
        form = ProtocolDeviationViolationForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
