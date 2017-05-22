from django.test import TestCase, tag

from model_mommy import mommy

from ..forms import AdverseEventTMGForm
from ..models import AdverseEventTMG


class TestAdverseEventTMGForm(TestCase):

    @tag('tmg')
    def test_default_mommy_recipe(self):
        obj = mommy.prepare_recipe(AdverseEventTMG._meta.label_lower)
        form = AdverseEventTMGForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())
