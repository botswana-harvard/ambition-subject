from django.test import TestCase
from model_mommy import mommy

from edc_base.utils import get_utcnow
from edc_constants.constants import NO, YES, NOT_APPLICABLE, OTHER, NORMAL

from ..forms import RadiologyForm
from ..models import Radiology


class TestRadiologyForm(TestCase):

    def test_valid_form(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower)
        form = RadiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def test_cxr_done_while_cxr_type_is_specified(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_cxr_done=YES,
                                   cxr_type=NORMAL,
                                   cxr_description='Description',
                                   are_results_abnormal=NO,
                                   when_cxr_done=get_utcnow())
        form = RadiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def test_cxr_not_done_while_cxr_type_is_not_specified(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_cxr_done=NO,
                                   cxr_type=NOT_APPLICABLE,
                                   are_results_abnormal=NOT_APPLICABLE,
                                   abnormal_results_reason=NOT_APPLICABLE,
                                   abnormal_results_reason_other=None)
        form = RadiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def test_cxr_done_while_cxr_type_is_na(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_cxr_done=YES,
                                   cxr_type=NOT_APPLICABLE,
                                   when_cxr_done=get_utcnow())
        form = RadiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

    def test_cxr_done_while_cxr_type_is_blank(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_cxr_done=YES,
                                   cxr_type=None,
                                   when_cxr_done=get_utcnow())
        form = RadiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

    def test_is_cxr_done_cxr_description(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_cxr_done=YES,
                                   cxr_description='Description',
                                   cxr_type=NORMAL,
                                   are_results_abnormal=NO,
                                   abnormal_results_reason_other=None,
                                   when_cxr_done=get_utcnow())
        form = RadiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def test_cxr_not_done_while_cxr_type_is_specified(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_cxr_done=NO,
                                   cxr_type=NORMAL)
        form = RadiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

    def test_cxr_not_done_while_date_done_specified(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_cxr_done=NO,
                                   when_cxr_done=get_utcnow())
        form = RadiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

    def test_chest_xray_result_infiltrate_location_na(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   cxr_type='infiltrate_location',
                                   infiltrate_location=NOT_APPLICABLE,
                                   when_cxr_done=get_utcnow())
        form = RadiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

    def test_chest_xray_result_infiltrate_location_specified(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_cxr_done=YES,
                                   cxr_type='infiltrate_location',
                                   infiltrate_location='lul',
                                   cxr_description='Description',
                                   are_results_abnormal=NO,
                                   abnormal_results_reason_other=None,
                                   when_cxr_done=get_utcnow())
        form = RadiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def test_ct_performed_and_is_scanned_with_no_contrast(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_ct_performed=YES,
                                   is_scanned_with_contrast=NO)
        form = RadiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def test_ct_performed_and_is_scanned_with_none_contrast(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_ct_performed=YES,
                                   is_scanned_with_contrast=None)
        form = RadiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

    def test_ct_performed_and_date_specified(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_ct_performed=YES,
                                   date_ct_performed=get_utcnow())
        form = RadiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def test_ct_performed_and_no_date_specified(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_ct_performed=YES,
                                   date_ct_performed=None)
        form = RadiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

    def test_ct_performed_and_brain_imaging_reason(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_ct_performed=YES,
                                   date_ct_performed=get_utcnow(),
                                   are_results_abnormal=NOT_APPLICABLE,
                                   abnormal_results_reason=NOT_APPLICABLE,
                                   abnormal_results_reason_other=None,
                                   brain_imaging_reason='reduction_in_gcs')
        form = RadiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def brain_imaging_reason_and_other_given(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   brain_imaging_reason=OTHER,
                                   brain_imaging_reason_other='results')
        form = RadiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def brain_imaging_reason_and_none_other_given(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   brain_imaging_reason=OTHER,
                                   brain_imaging_reason_other=None)
        form = RadiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

    def is_ct_performed_require_results(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_ct_performed=YES,
                                   brain_imaging_reason='reduction_in_gcs')
        form = RadiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def is_ct_performed_with_no_results(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_ct_performed=YES,
                                   brain_imaging_reason=None)
        form = RadiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

    def is_cxr_done_are_results_abnormal_yes(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_cxr_done=YES,
                                   are_results_abnormal=YES)
        form = RadiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def is_cxr_done_are_without_results_abnormal_yes(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   is_cxr_done=YES,
                                   are_results_abnormal=NOT_APPLICABLE)
        form = RadiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

    def are_results_abnormal_abnormal_results_reason(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   are_results_abnormal=YES,
                                   abnormal_results_reason='cerebral_oedema')
        form = RadiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def are_results_abnormal_abnormal_results_reason_none(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   are_results_abnormal=YES,
                                   abnormal_results_reason=None)
        form = RadiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

    def are_results_abnormal_abnormal_results_reason_other(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   are_results_abnormal=OTHER,
                                   abnormal_results_reason_other='Description')
        form = RadiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def are_results_abnormal_abnormal_results_reason_other_none(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   are_results_abnormal=OTHER,
                                   abnormal_results_reason_other=None)
        form = RadiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())

    def are_results_abnormal_abnormal_results_reason_infarcts(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   abnormal_results_reason='infarcts',
                                   if_infarcts_location='Description')
        form = RadiologyForm(data=obj.__dict__)
        self.assertTrue(form.is_valid())

    def are_results_abnormal_abnormal_results_reason_infarcts_blank(self):
        obj = mommy.prepare_recipe(Radiology._meta.label_lower,
                                   abnormal_results_reason='infarcts',
                                   if_infarcts_location=None)
        form = RadiologyForm(data=obj.__dict__)
        self.assertFalse(form.is_valid())
