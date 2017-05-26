from django.test import TestCase
from model_mommy import mommy

from edc_constants.constants import NO, YES, NOT_APPLICABLE

from ..forms import RadiologyForm
from ..models import Radiology


class TestRadiologyForm(TestCase):

    def test_valid_form(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower)
        form = RadiologyForm(data=obj.__dict__)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_cxr_done_while_cxr_type_is_specified(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_cxr_done=YES,
                                   cxr_type='normal')
        form = RadiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_cxr_not_done_while_cxr_type_is_not_specified(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_cxr_done=NO,
                                   cxr_type=NOT_APPLICABLE)
        form = RadiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_cxr_done_while_cxr_type_is_blank(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_cxr_done=YES,
                                   cxr_type=None)
        form = RadiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

    def test_cxr_not_done_while_cxr_type_is_specified(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_cxr_done=NO,
                                   cxr_type='normal')
        form = RadiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())


