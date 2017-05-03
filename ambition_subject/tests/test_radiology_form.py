from django.test import TestCase
from model_mommy import mommy

from edc_constants.constants import NO, YES, OTHER

from ..constants import (
    INFILTRATE_LOCATION, DIFFUSE, CXR_DESCRIPTION, NEW_NEUROLOGY,
    CEREBRAL_OEDEMA)
from ..forms import RadiologyForm


class TestRadiologyForm(TestCase):

    def setUp(self):

        self.data = {
            #'subject_visit': mommy.make_recipe('ambition_subject.subjectvisit'),
            'is_cxr_done': YES,
            'cxr_type': INFILTRATE_LOCATION,
            'infiltrate_location': DIFFUSE,
            'cxr_description': CXR_DESCRIPTION,
            'is_ct_performed': YES,
            'is_scanned_with_contrast': YES,
            'brain_imaging_reason': NEW_NEUROLOGY,
            'brain_imaging_reason_other': None,
            'are_results_abnormal': YES,
            'abnormal_results_reason': CEREBRAL_OEDEMA,
            'abnormal_results_reason_other': None,
            'if_infarcts_location': None}

    def test_valid_form(self):
        form = RadiologyForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_cxr_not_done_while_cxr_type_is_specified(self):
        self.data.update(
            is_cxr_done=NO,
            infiltrate_location=None,
            cxr_type=INFILTRATE_LOCATION,
            cxr_description=None,
            are_results_abnormal=None,
            abnormal_results_reason=None)
        form = RadiologyForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_cxr_not_done_while_cxr_type_is_not_specified(self):
        self.data.update(
            is_cxr_done=NO,
            cxr_type=None,
            infiltrate_location=None,
            cxr_description=None,
            are_results_abnormal=None,
            abnormal_results_reason=None)
        form = RadiologyForm(data=self.data)
        self.assertTrue(form.is_valid())
