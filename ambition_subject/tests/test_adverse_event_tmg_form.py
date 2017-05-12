from dateutil.relativedelta import relativedelta

from django.test import TestCase

from model_mommy import mommy

from edc_base.utils import get_utcnow
from edc_constants.constants import NO, YES

from ..forms import AdverseEventTMGForm


class TestAdverseEventTMGForm(TestCase):

    def setUp(self):
        ae_classification = mommy.make_recipe(
            'ambition_subject.ae_classification',)

        self.data = {
            'report_datetime': get_utcnow(),
            'ae_form_received_datetime': get_utcnow(),
            'clinical_review_datetime': None,
            'investigator_comments': None,
            'ae_classification': [ae_classification.id],
            'investigator_ae_description': (get_utcnow() - relativedelta(months=1)).date(),
            'regulatory_officials_notified_datetime': (get_utcnow() - relativedelta(days=1)).date(),
            'local_investigator_returned_datetime': get_utcnow(),
        }

    def test_valid_form(self):
        form = AdverseEventTMGForm(data=self.data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())
