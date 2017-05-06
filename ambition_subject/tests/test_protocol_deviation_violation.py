from dateutil.relativedelta import relativedelta

from django.test import TestCase

from edc_base.utils import get_utcnow
from edc_constants.constants import NO, YES

from ..forms import ProtocolDeviationViolationForm


class TestProtocolDeviationViolation(TestCase):

    def setUp(self):

        self.data = {
            'report_datetime': get_utcnow(),
            'participant_safety_impact': NO,
            'participant_safety_impact_details': None,
            'study_outcomes_impact': NO,
            'study_outcomes_impact_details': None,
            'date_violation_datetime': (get_utcnow() - relativedelta(months=1)).date(),
            'protocol_violation_type': 'procedure_not_completed',
            'other_protocol_violation_type': None,
            'violation_description': 'The procedure was not completed',
            'violation_reason': 'Emergency reasons ',
            'corrective_action_datetime': (get_utcnow() - relativedelta(months=1)).date(),
            'corrective_action': 'procedure_redone',
            'preventative_action_datetime': get_utcnow(),
            'preventative_action': 'not_sure_what_goes_here',
            'action_required': 'patient_remains_on_study',
        }

    def test_valid_form(self):
        form = ProtocolDeviationViolationForm(data=self.data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_safety_impact_no_details_invalid(self):
        self.data.update(participant_safety_impact=YES,
                         participant_safety_impact_details=None)
        form = ProtocolDeviationViolationForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_study_impact_no_details_invalid(self):
        self.data.update(study_outcomes_impact=YES,
                         study_outcomes_impact_details=None)
        form = ProtocolDeviationViolationForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_violation_type_no_details_invalid(self):
        self.data.update(protocol_violation_type=None,
                         other_protocol_violation_type=None)
        form = ProtocolDeviationViolationForm(data=self.data)
        self.assertFalse(form.is_valid())
