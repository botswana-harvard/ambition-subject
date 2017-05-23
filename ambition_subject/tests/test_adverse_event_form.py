from django.test import TestCase, tag

from model_mommy import mommy

from edc_constants.constants import NO, YES

from ..models import AdverseEvent
from ..forms import AdverseEventForm


@tag('d')
class TestAdverseEventForm(TestCase):

    def test_default_mommy_recipe(self):
        obj = mommy.prepare_recipe(AdverseEvent._meta.label_lower)
        form = AdverseEventForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_other_a_event_reason(self):
        """Assert cause was specified if other_ae_event_cause is YES.
        """
        obj = mommy.prepare_recipe(AdverseEvent._meta.label_lower)
        obj.ae_cause = YES
        obj.ae_cause_other = None
        form = AdverseEventForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj.ae_cause_other = 'blahblah'
        obj.recurrence_cm_symptoms = NO
        form = AdverseEventForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def test_ae_study_drug_relation_possibility(self):
        obj = mommy.prepare_recipe(AdverseEvent._meta.label_lower)
        obj.ae_study_relation_possibility = NO
        obj.possiblity_detail = None
        form = AdverseEventForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

        obj.ae_study_relation_possibility = YES
        obj.possiblity_detail = None
        form = AdverseEventForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def test_ae_study_drug_relation_ambisome(self):
        obj = mommy.prepare_recipe(AdverseEvent._meta.label_lower)
        obj.ae_study_relation_possibility = YES
        obj.ambisome_relation = None
        form = AdverseEventForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

    def test_ae_study_drug_relation_fluconazole(self):
        obj = mommy.prepare_recipe(AdverseEvent._meta.label_lower)
        obj.ae_study_relation_possibility = YES
        obj.fluconazole_relation = None
        form = AdverseEventForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

    def test_ae_study_drug_relation_amphotericin(self):
        obj = mommy.prepare_recipe(AdverseEvent._meta.label_lower)
        obj.ae_study_relation_possibility = YES
        obj.amphotericin_b_relation = None
        form = AdverseEventForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())
