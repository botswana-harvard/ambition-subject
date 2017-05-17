from dateutil.relativedelta import relativedelta

from django.test import TestCase

from edc_base.utils import get_utcnow
from edc_constants.constants import NOT_APPLICABLE, NO, YES

from ..forms import AdverseEventForm


class TestAdverseEventForm(TestCase):

    def setUp(self):

        self.data = {
            'ae_awareness_date': (get_utcnow() - relativedelta(years=1)).date(),
            'description': 'Description here',
            'ae_start_date': (get_utcnow() - relativedelta(years=1)).date(),
            'ae_severity': 'grade_3',
            'ae_intensity': 'moderate',
            'patient_treatment_group': 'regimen_1',
            'incident_study_relationship': NO,
            'incident_drug_relationship_ambisome': 'unlikely_related',
            'incident_drug_relationship_fluconozole': 'unlikely_related',
            'last_implicated_medication_administered_datetime': (get_utcnow() + relativedelta(years=1)).date(),
            'last_implicated_medication': 'flucazone',
            'last_implicated_medication_dose': '2mg',
            'last_implicated_medication_route': 'not_sure_what_goes_here',
            'other_ae_event_cause': NO,
            'action_taken_treatment': 'action treatment',
            'recurrence_cm_symptoms': NOT_APPLICABLE,
            'is_sae_event': NO,
            'sae_event_reason': NOT_APPLICABLE,
            'is_susar': NO,
            'susar_reported': NOT_APPLICABLE,
            'susar_reported_datetime': None,
        }

    def test_valid_form(self):
        form = AdverseEventForm(data=self.data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_other_ae_event_no_reason_invalid(self):
        """Assert cause was specified if other_ae_event_cause is YES.
        """
        self.data.update(other_ae_event_cause=YES,
                         other_ae_event_cause_specify=None)
        form = AdverseEventForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_ae_event_no_recurrence_symptoms_invalid(self):
        """Assert reccurence symptoms were specified if
            other_ae_event_cause is YES.
        """
        self.data.update(other_ae_event_cause=YES,
                         recurrence_cm_symptoms=NOT_APPLICABLE)
        form = AdverseEventForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_is_sae_event_no_reason_invalid(self):
        """Assert reason was provided for sae event.
        """
        self.data.update(is_sae_event=YES,
                         sae_event_reason=NOT_APPLICABLE)
        form = AdverseEventForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_is_susar_not_reported_invalid(self):
        """Assert if susar then it is reported.
        """
        self.data.update(is_susar=YES,
                         susar_reported=NOT_APPLICABLE)
        form = AdverseEventForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_susar_reported_no_report_date_invalid(self):
        """Assert susar reported with datetime provided.
        """
        self.data.update(susar_reported=YES,
                         susar_reported_datetime=None)
        form = AdverseEventForm(data=self.data)
        self.assertFalse(form.is_valid())
