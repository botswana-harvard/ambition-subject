from django.test import TestCase, tag

from model_mommy import mommy

from edc_base.utils import get_utcnow
from edc_constants.constants import NOT_APPLICABLE, NO, YES

from ..models import AdverseEvent
from ..forms import AdverseEventForm


class TestAdverseEventForm(TestCase):

    @tag('default')
    def test_default_mommy_recipe(self):
        obj = mommy.prepare_recipe(AdverseEvent._meta.label_lower)
        form = AdverseEventForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    @tag('a_event_reason')
    def test_other_a_event_reason(self):
        """Assert cause was specified if other_ae_event_cause is YES.
        """
        obj = mommy.prepare_recipe(AdverseEvent._meta.label_lower)
        obj.ae_cause_other = YES
        obj.ae_cause_other_specify = None
        form = AdverseEventForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj.ae_cause_other_specify = 'blahblah'
        obj.recurrence_cm_symptoms = NO
        form = AdverseEventForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    @tag('a_event_recurrence')
    def test_a_event_recurrence_symptoms(self):
        """Assert reccurence symptoms were specified if
            other_ae_event_cause is YES.
        """
        obj = mommy.prepare_recipe(AdverseEvent._meta.label_lower)
        obj.ae_cause_other = YES
        obj.recurrence_cm_symptoms = NOT_APPLICABLE
        form = AdverseEventForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj.ae_cause_other = YES
        obj.ae_cause_other_specify = 'blahblah'
        obj.recurrence_cm_symptoms = NO
        form = AdverseEventForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    @tag('sa_event_reason')
    def test_is_sa_event_reason(self):
        """Assert reason was provided for sae event.
        """
        obj = mommy.prepare_recipe(AdverseEvent._meta.label_lower)
        obj.is_sa_event = YES
        obj.sa_event_reason = NOT_APPLICABLE
        form = AdverseEventForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj.is_sa_event = YES
        obj.sa_event_reason = 'life_threatening'
        form = AdverseEventForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    @tag('susar_reported')
    def test_is_susar_reported(self):
        """Assert if susar then it is reported.
        """
        obj = mommy.prepare_recipe(AdverseEvent._meta.label_lower)
        obj.is_susar = YES
        obj.susar_reported = NOT_APPLICABLE
        form = AdverseEventForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj.is_susar = YES
        obj.susar_reported = NO
        form = AdverseEventForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    @tag('susar_reported_date')
    def test_susar_reported_date(self):
        """Assert susar reported with datetime provided.
        """
        obj = mommy.prepare_recipe(AdverseEvent._meta.label_lower)
        obj.is_susar = YES
        obj.susar_reported = YES
        obj.susar_reported_datetime = None
        form = AdverseEventForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj.is_susar = YES
        obj.susar_reported = YES
        obj.susar_reported_datetime = get_utcnow()
        form = AdverseEventForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
